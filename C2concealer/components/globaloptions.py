import uuid
import random
from ..data import reg_headers

class globalOptions(object):

	'''
	Class for the global options section of the profile. 

	Profile options include:
	- sample_name
	- sleeptime
	- jitter
	- tcp_port
	- user_agent

	For more details visit:
	https://www.cobaltstrike.com/help-malleable-c2

	'''

	def __init__(self):
		self.sample_name = None
		self.sleeptime = None
		self.jitter = None
		self.tcp_port = None
		self.useragent = None

	def randomizer(self):
		
		'''
		Method to generate random globalOptions values.
		
		1. sample_name set to first 8 chars from the uuid.uuid4() func
		2. sleeptime is set to a random integer between 55000ms and 65000ms
		3. jitter is set to an odd number between 37 and 45 (%)
		4. tcp_port is randomly selected between 1024-10000 (not 4443-4446)
		5. User agent is randomly selected 

		Output: globalOptions instance attributes are populated with random data.

		'''
		
		self.sample_name = str(uuid.uuid4())[:8]
		self.sleeptime = str(random.randint(55000,65000))
		self.jitter = str(random.randrange(37,45,2))
		self.tcp_port = str(random.choice((list(range(1024,4442))+list(range(4447,10000)))))
		self.useragent = random.choice(reg_headers.user_agent)

	def printify(self):

		'''
		Method to print global options attributes to string formatted to Cobalt Strike recs.

		Output: returns a string with attribute values, headers and appropriate 
		indentation/line-breaks formatted for the global options section of the profile.

		Example:

		set sample_name "UUID-UUID";
		set sleeptime "60";
		set jitter "50";
		set tcp_port 34857;
		set useragent "Mozilla 5.0";

		'''

		profileString = ''
		for attr, value in self.__dict__.items():
			profileString += 'set ' + attr + ' "' + value + '";\n'
		profileString += '\n'
		return profileString 
