import argparse
import sys
import os
import fnmatch
import hashlib
from c2concealer.profile import Profile

def find(pattern, path):
	'''
	Simple function for finding the abs path of a file on unix

	'''

	result = []
	for root, dirs, files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name,pattern):
				result.append(os.path.join(root,name))
	return result

def _test_1000_generation():

	'''
	Basic testing function to see if we can create 1000 profiles 
	that will pass c2lint.
	'''

	if(os.path.exists('/usr/share/cobaltstrike/c2lint')):
		path = '/usr/share/cobaltstrike/c2lint'
		print("[i] Found c2lint in the /usr/share/cobaltstrike directory.")
	else:
		print("[i] Searching for the c2lint tool on your system. Might take some time.")
		paths = find('c2lint','/')
		if(paths):
			path = paths[0]
		else:
			print("[-] Can't find cobaltstrike's c2lint profile validator.")
			print("[!] Please install cobaltstrike's c2lint tool.")
			sys.exit()

	totalCount = 0
	print("[i] Starting generation test: can we build 1,000 profiles successfully?")
	ssl_dict = {'self': None, 'keystore': None, 'password': None}
	while(totalCount < 1000):
		retryCount = 0
		while(retryCount < 10):
			profile = Profile(ssl_dict)
			profile.randomizer()
			profile.consistencyCheck()
			profile.buildMainProfile()
			for i in range(9):
				varname = "variant_" + str(i+1)
				variant = Profile(ssl_dict, varname)
				variant.randomizer()
				variant.consistencyCheck()
				variant.buildVariant()
				profile.profileString += variant.profileString
			profile.outputProfile()
			passed, lintResults = profile.c2LintCheck(path)
			if passed:
				totalCount+=1
				os.remove((os.getcwd() + '/' + profile.globalOptions.sample_name + '.profile'))	
				print("Completed profile #{} with {} retries".format(totalCount,retryCount))
				break
			else:
				retryCount+=1	
				if retryCount == 5:
					print("[x] Failed generation test after {} profiles.".format(totalCount))
					for line in lintResults:
						print(line.rstrip())
					os.remove((os.getcwd() + '/' + profile.globalOptions.sample_name + '.profile'))
					sys.exit()
				os.remove((os.getcwd() + '/' + profile.globalOptions.sample_name + '.profile'))


def _test_100000_unique():

	'''
	Basic testing function to see if we can create 100,000 unique profiles 
	based off of the random data included in the /data subfolder.
	'''

	profile_set = set()
	print("[i] Starting uniqeness test: can we build unique 100,000 profiles?")
	totalCount = 0
	ssl_dict = {'self': None, 'keystore': None, 'password': None}
	while(totalCount < 100000):
		profile = Profile(ssl_dict)
		profile.randomizer()
		profile.consistencyCheck()
		profile._test_buildProfile()
		totalCount+=1
		profile_hash = hashlib.md5(profile.profileString.encode()).hexdigest()
		if profile_hash in profile_set:
			print("[x] Failed uniqueness test. There is a duplicate!")
			sys.exit()
		profile_set.add(profile_hash)
		print("Completed profile #{}".format(totalCount))
		

if __name__ == '__main__':
	_test_1000_generation()
	_test_100000_unique()
	print("[+] Successfully passed sanity check.")
