import random
import datetime
from ..data import stage

class stageBlock(object):

	'''
	Class for the stage component of the C2 profile.

	Profile options include:
	- checksum
	- userwx
	- image_size_x86
	- image_size_x64
	- sleep_mask
	- strrep DLL name and .dll file name; note that this replacement name
	   is limited to 16 chars and dll to 6 chars
	- prepend (how many nops add before?)
	- cleanup
	- stomppe
	- obfuscate
	- compile_time
	- entry_point
	- name

	Lots of stuff here. I recommend reading up on it here:
	https://www.cobaltstrike.com/help-malleable-postex
	https://blog.cobaltstrike.com/2017/03/15/cobalt-strike-3-7-cat-meet-mouse/
	
	'''

	def __init__(self):
		self.checksum = None
		self.userwx = None
		self.image_size_x86 = None
		self.image_size_x64 = None
		self.sleep_mask = None
		self.cleanup = None
		self.stomppe = None
		self.obfuscate = None
		self.compile_time = None
		self.entry_point = None
		self.name = None
		self.attrList = ['checksum', 'userwx', 'image_size_x86', 'image_size_x64', \
		'sleep_mask', 'cleanup', 'stomppe', 'obfuscate', 'compile_time', 'entry_point', 'name']
		self.transform_name = None
		self.prepend_count = None


	def randomizer(self):
		
		'''
		Method to generate random stage values.
		
		-	checksum: 1-10 integer
		-	userwx: false
		-	image_size_x86: integer between 512,001 and 576,000
		-	image_size_x64: integer between 512,001 and 576,000
		-	sleep_mask: true
		-	cleanup: true
		-	stomppe: true
		-	obfuscate: true
		-	compile_time: a random day between 30 and 120 days ago
		-	entry_point: random int between 80000 and 90000
		-	name: random choice from /data/stage.py


		Output: stageBlock instance attributes are populated with random data.

		'''
		
		#CUSTOMIZE THE CHECKSUM VALUE#
		self.checksum = str(random.randint(1,10))
		self.userwx = "false"

		#CUSTOMIZE IMAGE SIZE VALUE IN PE HEADER#
		self.image_size_x86 = str(random.randint(512001,576000))
		self.image_size_x64 = str(random.randint(512001,576000))

		self.sleep_mask = "true"
		self.cleanup = "true"
		self.stomppe = "true"
		self.obfuscate = "true"

		#CUSTOMIZE THE COMPILE TIME#
		self.compile_time = (datetime.datetime.now()-datetime.timedelta(days=random.randint(30,120))).strftime("%d %b %Y %H:%M:%S")
		
		#CUSTOMIZE THE ENTRY POINT#
		self.entry_point = str(random.randint(80000,90000))
		self.transform_name = str(random.choice(stage.transform_names))
		self.name = self.transform_name.lower() + ".dll"
		self.prepend_count = random.randint(4,8)
		


	def printify(self):
		
		'''
		Method to print stage attributes to string formatted to Cobalt Strike recs.

		Output: returns a string with attribute values, headers and appropriate 
		indentation/line-breaks formatted for the stage section of the profile.

		Example:

		stage {
	
			set checksum "10";
			set userwx "false";
			set image_size_x86 "857033";
			set image_size_x64 "937448";
			set sleep_mask "true";

			transform-x86 {
		        prepend "\x90\x90\x90\x90";
		        strrep "ReflectiveLoader" "DebugMenu";
		    }

		    transform-x64 {
		        prepend "\x90\x90\x90\x90";
		        strrep "ReflectiveLoader" "DebugMenu";
		    }

		}
		
		'''
		profileString = ''
		profileString += 'stage {\n\n'
		for item in self.attrList:
			attrValue = getattr(self, item)
			profileString += '\tset ' + item + ' "' + attrValue + '";\n'
		profileString += '\n'

		profileString += '\ttransform-x86 {\n'
		profileString += '\t\tprepend "' + '\\x90'*self.prepend_count + '";\n'
		profileString += '\t\tstrrep "ReflectiveLoader" "' + self.transform_name[:16] + '";\n'
		profileString += '\t}\n\n'

		profileString += '\ttransform-x64 {\n'
		profileString += '\t\tprepend "' + '\\x90'*self.prepend_count + '";\n'
		profileString += '\t\tstrrep "ReflectiveLoader" "' + self.transform_name[:16] + '";\n'
		profileString += '\t}\n\n'

		profileString += '}\n\n'
		return profileString 
