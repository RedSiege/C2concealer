import string
import os, re, readline, glob
import fnmatch
import sys
from .profile import Profile
import getpass
import subprocess

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

def sslOptionSelection():
	'''
	Function for user to select 1, 2, 3 or 4 input.
	'''

	while True:
		try:
			ssl_choice = int(input("[?] Option [1/2/3/4]: "))
			if not ssl_choice in [1,2,3,4]:
				print("[x] Invalid number. Only 1, 2, 3 or 4.")
				continue
			return ssl_choice
		except ValueError:
			print("[x] Invalid SSL choice. Must be an integer. Try again.")
		

def variantCountSelection():
	'''
	Function for user to select variant count.

	Max 10.
	'''
	while True:
		try:
			variant_count = int(input("[?] How many HTTP variants: "))
			if not variant_count in [0,1,2,3,4,5,6,7,8,9,10]:
				print("[x] Invalid number. Only 0 - 10.")
				continue
			return variant_count
		except ValueError:
			print("[x] Invalid variant count choice. Must be an integer (0-10). Try again.")


def userInputNoPunct(inputQuestion):
	'''
	Function that does not accept punctuation from user input.
	'''
	invalidChars = set(string.punctuation)
	while True:
		output = input(inputQuestion)
		if any(char in invalidChars for char in output):
			print("\n[i] No special characters allowed. Re-enter.")
			continue
		return output

def userInputOnlyNum(inputQuestion):
	'''
	Function that only accepts ints from user input.
	'''
	while True:
		try:
			validity = str(int(input(inputQuestion)))
			return validity
		except ValueError:
			print("\n[i] Validity must be an integer. Re-enter.")

def buildSelfSignedSSL():
	'''

	Function that builds a self-signed SSL cert. User is prompted to 
	provide the common_name, organization, country, locality, state and validity.

	Output: a dictionary object containing the self-signed SSL cert info 

	'''
	while True:
		print("Certificate Details:")
		common_name = input("What is the host? (ex: google.com)\n> ")
		organization = userInputNoPunct("What is the organization? (ex: Google)\n> ")
		country = userInputNoPunct("What is the country abbr? (ex: US)\n> ")
		locality = userInputNoPunct("What is the city? (ex: Mountainview)\n> ")
		state = userInputNoPunct("What is the state? (ex: CA)\n> ")
		validity = userInputOnlyNum("How long is it valid (in days)? (ex: 365)\n> ")
		print("")
		print("[i] Here's how your certificate will read")
		print("\tCommon Name: {}".format(common_name))
		print("\tOrganization: {}".format(organization))
		print("\tCity: {}".format(locality))
		print("\tState: {}".format(state))
		print("\tCountry: {}".format(country))
		print("\tValidity: {}".format(validity))
		correct_SSL = input("\n[?] Is this correct? [y/n] ")
		if correct_SSL == 'y' or correct_SSL == '':
			self_ssl_dict = {
			'CN':common_name,
			'O':organization,
			'L':locality,
			'ST':state,
			'C':country,
			'validity':validity,
			}
			print('')
			return self_ssl_dict

def letsEncrypt():
	'''

	Function that runs LetsEncrypt's ACME protocol to verify domain ownership
	and then issue a signed SSL cert for that domain. The script first checks to 
	make sure the user has certain software installed, then opens an Apache service 
	on port 80, calls the CertBot API to issue a certificate, packages the certificate
	into a java keystore in the current working directory, then tears down the Apache service.

	Shoutout to: @KillSwitch-GUI for building this script. We use a modified version in this tool. 

	Output: a keystore.store file in the current working directory

	Returns: the name of the keystore and password

	Note: the bash file that runs the bulk of the LetsEncrypt API via CertBot needs to be
	executable, so there is an OS call to make it executable.

	'''
	print("")
	print("Certificate Details:")
	domain = input("What is the domain? (ex: google.com)\n> ")
	password = getpass.getpass("Enter a password for securing the keystore?\n> ")
	keystore = domain+".store"
	generate_cert_path = os.path.dirname(os.path.abspath(__file__)) + '/generate-cert.sh'
	subprocess.call(['chmod','u+x',generate_cert_path])
	subprocess.check_call([generate_cert_path,domain,password,keystore])
	print("")
	print("[i] Here's your certificate details:")
	print("Domain: {}".format(domain))
	print("Keystore: {}".format(keystore))
	print("[i] SSL Certificate Generated Successfully.")
	return keystore, password

def existingKeystore():
	'''

	Function that prompts user for existing keystore information. For more information on
	keystores, please visit: https://www.cobaltstrike.com/help-malleable-c2. 

	Returns: the name of the keystore and password

	Note: creates a copy of the keystore and adds it to the current working directory

	'''
	print("")
	print("Keystore Details:")
	while True:

		#Instantiate tabCompleter class to allow tab completion for file names
		t = tabCompleter()
		readline.set_completer_delims('\t')
		readline.parse_and_bind("tab: complete")
		readline.set_completer(t.pathCompleter)

		cwd = os.getcwd()

		keystore_path = input("Where is the keystore located? (absolute path)\n")
		
		#If relative file chosen, add in cwd path
		if not keystore_path.startswith("/"):
			keystore_path = cwd + "/" + keystore_path
		if os.path.exists(keystore_path):
			if not keystore_path.endswith(".store"):
				print("[x] File must be of .store type. Please try again.")
				continue
			keystore = keystore_path.split("/")[-1]
			os.system("cp " + keystore_path + " .")
			print("[i] Keystore file copied to current directory.")
			break
		else:
			print("[x] Invalid path. File not found. Please try again.")
	password = getpass.getpass("Enter the keystore's password:\n ")
	return keystore, password

def chooseSSL():
	print("Choose an SSL option:")
	print("1. Self-signed SSL cert (just input a few details)")
	print("2. LetsEncrypt SSL cert (requies a temporary A record for the relevant domain to be pointed to this machine)")
	print("3. Existing keystore")
	print("4. No SSL")
	print("")

	ssl_choice = sslOptionSelection()

	ssl_dict = {'self': None, 'keystore': None, 'password': None}

	if ssl_choice == 1:
		ssl_dict['self'] = buildSelfSignedSSL()
	elif ssl_choice == 2:
		ssl_dict['keystore'], ssl_dict['password'] = letsEncrypt()
	elif ssl_choice == 3:
		ssl_dict['keystore'], ssl_dict['password'] = existingKeystore()
	elif ssl_choice == 4:
		pass
	else:
		print("Invalid SSL choice. Exiting.")
		sys.exit()

	return ssl_dict

'''
The class below is borrowed for file name tab completion. Here's the original source:
https://gist.githubusercontent.com/iamatypeofwalrus/5637895/raw/550cdb53ace8dbdf9bd89340340be35b41759d52/tabCompleter.py

'''
class tabCompleter(object):
    """ 
    A tab completer that can either complete from
    the filesystem or from a list.
    
    Partially taken from:
    http://stackoverflow.com/questions/5637124/tab-completion-in-pythons-raw-input
    """

    def pathCompleter(self,text,state):
        """ 
        This is the tab completer for systems paths.
        Only tested on *nix systems
        """
        line   = readline.get_line_buffer().split()

        return [x for x in glob.glob(text+'*')][state]



#Function used for testing / debugging
# feel free to use, but it doesn't do anything special
def _debug_generateOneProfile(ssl_dict, path):
	print("[i] Building random C2 malleable profile.")
	profile = Profile(ssl_dict)
	profile.randomizer()
	profile.consistencyCheck()
	profile.buildMainProfile()
	profile.outputProfile()
	passed, lintResults = profile.c2LintCheck(path)
	for line in lintResults:
		print(line.rstrip())
	if passed:
		print("Passed!")
	else:
		print("Failed!")
