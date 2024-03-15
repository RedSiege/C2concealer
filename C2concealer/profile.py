from .components import *
import datetime
import os
import sys
import random
from .data import urls

class Profile(object):

	'''
	Primary Class for Generating C2 Malleable Profiles.

	Usage:
		profile = Profile()
		profile.randomizer() #generates random data and adds to profile attributes
		profile.buildProfile() #creates a string formatted to Cobalt Strike profile recs
		profile.outputProfile() #writes string to a file

	Output:
		A randomly generated C2 malleable profile for use with Cobalt Strike. 

	Notes:
		- Specify the order of malleable profile components in the self.componentOrder list
		- ALL class attributes are named according to how they must be represented in the
		  C2 profile. Ex: self.Host and not self.host since 'header "Host" "somehost.com"'
		  is the format used in Cobalt Strike. The only exception is when a header requires
		  a hyphen. In these cases an underscore is used in the attribute name since hyphen
		  in python means subtract. To correct these issues during the printify() methods,
		  a simple str.replace("_","-") function is applied. Ex: self.User_Agent transforms into 
		  "User-Agent" during the printify() function.
	'''

	def __init__(self, ssl_dict, name='default', hostname=None):
		self.globalOptions = globaloptions.globalOptions()
		self.dnsOptions = dnsoptions.dnsOptions() 
		self.smbOptions = smboptions.smbOptions()
		self.sslOptions = ssloptions.sslOptions(ssl_dict)
		self.httpConfig = httpconfig.httpConfig()
		self.getClient = getclient.getClient(name, hostname)
		self.getServer = getserver.getServer()
		self.postClient = postclient.postClient(name,hostname)
		self.postServer = postserver.postServer()
		self.stagerClient = stagerclient.stagerClient(name, hostname)
		self.stagerServer = stagerserver.stagerServer()
		self.stageBlock = stageblock.stageBlock()
		self.processInject = processinject.processInject()
		self.postEx = postex.postEx()
		self.componentOrder = ['globalOptions', 'dnsOptions', 'smbOptions', 'sslOptions', 'httpConfig','getClient', 'getServer',\
		'postClient', 'postServer', 'stagerClient', 'stagerServer', 'stageBlock', 'processInject', 'postEx']
		self.profileString = ""

	def randomizer(self):
		
		'''
		Method for generating random profile data and assigning 
		it to profile instance attributes. 

		This will call individual randomizer() methods for each profile component. 
		Need to provide the http-get host for the getServer randomizer() function. 
		Rest require no args.

		Output: profile instance attributes are updated with the random data
		
		'''


		for component in self.componentOrder:
			val = getattr(self,component)
			if component == "getServer":
				val.randomizer(self.getClient.uri)
			else:
				val.randomizer()


	def consistencyCheck(self):
		
		'''
		Method for checking consistency for situations where
		one indicator should dicatate another indicator's value.

		[1] In stagerclient.py add file type to URIs based on stagerserver.Content_Type
		'''

		#[1]#
		if (self.stagerServer.Content_Type == 'image/jpeg'):
			file_type = ".jpg"
		elif (self.stagerServer.Content_Type == 'image/png'):
			file_type = ".png"
		elif (self.stagerServer.Content_Type == 'image/gif'):
			file_type = '.gif'
		elif (self.stagerServer.Content_Type == 'audio/mpeg'):
			file_type = ".mp3"
		else:
			file_type = '.ico'
		self.stagerClient.uri_x86 += file_type
		self.stagerClient.uri_x64 += file_type

	def c2LintCheck(self, path):
		''''
		Method for running c2lint on generated profile.
		
		Adapted from: https://github.com/bluscreenofjeff/Mal \
		leable-C2-Randomizer/blob/master/malleable-c2-randomizer.py

		Return: True/False profile passed c2lint and the lintresults

		Note: if c2lint is in the root directory ... ie: /c2lint, then this won't work

		'''
		path_split = path.rsplit('/',1)
		lintResults = os.popen('cd ' + path_split[0] + '  &&  ./' + path_split[1] + ' ' + os.getcwd() + '/' + self.globalOptions.sample_name + '.profile' ).readlines()
		passed = True
		for outputline in lintResults:
			if 'Error(s)' in outputline or '[-]' in outputline:
				passed = False
		
		return passed, lintResults

	def outputProfile(self):

		'''
		Method for writing profile string to an output file.
		
		Method creates a new file located in the cwd named with the 8-char UUID "sample_name"
		generated in /C2generator/components/globaloptions.py. Method calls the file.write()
		function on self.profileString to write to the file.

		Output: A file written in the cwd with new profile. 

		'''

		with open(self.globalOptions.sample_name+'.profile', 'w') as file:
			file.write(self.profileString)


	def buildMainProfile(self):
		
		'''
		Method for building a C2 malleable profile for Cobalt Strike.

		Method loops through the printify() method defined in each 
		profile sub-component (located in C2generator/components/) creating
		a long string of the entire profile. 

		Output: A string filled with profile details formatted with line breaks 
		and tabs according to the Cobalt Strike C2 Malleable Profile guidelines. 
		String stored in self.profileString.

		'''
		date = datetime.datetime.now()	
		dateStr = date.strftime("%b %d, %Y [%H:%M]")

		self.profileString += '############################################################\n'
		self.profileString += '# Date Created: ' + dateStr + (58-len(dateStr)-15)*" " + "#\n"
		self.profileString += '# Profile Name: ' + self.globalOptions.sample_name + ".profile" + 27*" " + "#\n"
		self.profileString += "# Generated by Red Siege's C2concealer tool.     #\n"
		self.profileString += '############################################################\n\n'


		for component in self.componentOrder:
			val = getattr(self,component)
			self.profileString += val.printify()

	def buildVariant(self):
		
		'''
		Method for building a C2 malleable variant for Cobalt Strike.

		Method loops through the printify() method defined in each 
		profile sub-component (http-get, http-post and http-stager only) creating
		a long string of the variant profile. 

		Output: A string filled with profile details formatted with line breaks 
		and tabs according to the Cobalt Strike C2 Malleable Profile guidelines. 
		String stored in self.profileString.

		'''
		self.componentOrder = ['getClient', 'getServer','postClient', 'postServer', 'stagerClient', 'stagerServer']
		for component in self.componentOrder:
			val = getattr(self,component)
			self.profileString += val.printify()


#Test function. Not needed, but leaving in for future debugging#
	def _test_buildProfile(self):

		for component in self.componentOrder:
			val = getattr(self,component)
			if component == "globalOptions":
				self.profileString += 'set ' + 'sleeptime' + ' "' + self.globalOptions.sleeptime + '";\n'
				self.profileString += 'set ' + 'jitter' + ' "' + self.globalOptions.jitter + '";\n'
				self.profileString += 'set ' + 'tcp_port' + ' "' + self.globalOptions.tcp_port + '";\n'
				self.profileString += 'set ' + 'useragent' + ' "' + self.globalOptions.useragent + '";\n'
				self.profileString += '\n'
			else:
				self.profileString += val.printify()
		
	
