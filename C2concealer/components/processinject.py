import random

class processInject(object):

	'''
	Class for the process inject component of the C2 profile.

	Profile options include:
	- allocator 
	- min_alloc
	- userwx
	- startrwx
	- transform-x86 nop prepend count
	- transform-x64 nop prepend count
	- execute is hardcoded, see below in printify()

	For more information:
	https://www.cobaltstrike.com/help-malleable-postex
	https://blog.cobaltstrike.com/2019/08/21/cobalt-strikes-process-injection-the-details/
	
	'''

	def __init__(self):
		self.allocator = None
		self.min_alloc = None
		self.userwx = None
		self.startrwx = None
		

	def randomizer(self):
		
		'''
		Method to generate random process inject values.
		
		1. All static except min_alloc which is an integer larger than 4096, max 32000, not 16384

		Output: processInject instance attributes are populated with random data.

		'''
		
		self.allocator = "VirtualAllocEx"
		self.min_alloc = str(random.choice((list(range(4096,16383))+list(range(16385,32000)))))
		self.userwx = "false"
		self.startrwx = "false"

	def printify(self):
		
		'''
		Method to print process inject attributes to string formatted to Cobalt Strike recs.

		Output: returns a string with attribute values, headers and appropriate 
		indentation/line-breaks formatted for the process inject section of the profile.

		Example:

		process-inject {

		    set allocator "virtualallocex";		
		    set min_alloc "10374";
		    set userwx "false"; 
		    set startrwx "false";

		    transform-x86 {
				prepend "\x90\x90\x90";
		    }
		    transform-x64 {
				prepend "\x90\x90\x90";
		    }
		   
		    execute {
		        CreateThread;
		        RtlCreateUserThread;
		        CreateRemoteThread;
		    }
		}
		
		'''

		prepend_count = random.randint(3,8)

		profileString = ''
		profileString += 'process-inject {\n\n'
		for attr, value in self.__dict__.items():
			profileString += '\tset ' + attr + ' "' + value + '";\n'
		profileString += '\n'

		profileString += '\ttransform-x86 {\n'
		profileString += '\t\tprepend "' + "\\x90"*prepend_count+ '";\n'
		profileString += '\t}\n'
		profileString += '\ttransform-x64 {\n'
		profileString += '\t\tprepend "' + "\\x90"*prepend_count + '";\n'
		profileString += '\t}\n'

		profileString += '\n'

		##Hardcoded Execute block
		profileString += '\texecute {\n'
		profileString += '\t\tCreateThread;\n'
		profileString += '\t\tRtlCreateUserThread;\n'
		profileString += '\t\tCreateRemoteThread;\n'
		profileString += '\t}\n\n'
		##End execute block

		profileString += '}\n\n'
		return profileString 
