import random
from ..data import post_ex

class postEx(object):

	'''
	Class for the post-ex block component of the C2 profile.

	Profile options include:
	- spawnto-x86
	- spawnto-x64
	- obfuscate
	- smartinject
	- amsi-disable

	For more information:
	https://www.cobaltstrike.com/help-malleable-postex
	

	'''

	def __init__(self):
		self.spawnto_x86 = None
		self.spawnto_x64 = None
		self.obfuscate = None
		self.smartinject = None
		self.amsi_disable = None

	def randomizer(self):
		
		'''
		Method to generate random post-ex block values.
		
		1. Choose a random exe from list in /data/post-ex.py for spawnto attrs

		Output: postEx instance attributes are populated with random data.

		'''
		proc = str(random.choice(post_ex.spawn_processes))
		self.spawnto_x86 = "%windir%\\\\syswow64\\\\" + proc
		self.spawnto_x64 = "%windir%\\\\sysnative\\\\" + proc
		
		#Static
		self.obfuscate = "true"
		self.smartinject = "true"
		self.amsi_disable = "true"


	def printify(self):
		
		'''
		Method to print postEx attributes to string formatted to Cobalt Strike recs.

		Output: returns a string with attribute values, headers and appropriate 
		indentation/line-breaks formatted for the post-ex block section of the profile.

		Example:

		post-ex {

		    set spawnto_x86 "%windir%\\syswow64\\rundll32.exe";
		    set spawnto_x64 "%windir%\\sysnative\\rundll32.exe";
		    set obfuscate "true";
		    set smartinject "true";
		    set amsi_disable "true";

		}
		
		'''
		profileString = ''
		profileString += 'post-ex {\n'
		for attr, value in self.__dict__.items():
			profileString += '\tset ' + attr + ' "' + value + '";\n'
		profileString += '}\n\n'
		return profileString 
