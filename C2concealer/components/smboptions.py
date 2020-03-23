import random
from ..data import smb

class smbOptions(object):

	'''
	Class for the smb options section of the profile. 

	Profile options include:
	- pipename
	- pipename_stager

	For more info:
	https://www.cobaltstrike.com/help-malleable-c2

	Ctrl-f smb ... and you'll see a table explaining these two values

	'''

	def __init__(self):
		self.pipename = None
		self.pipename_stager = None

	def randomizer(self):
		
		'''
		Method to generate random smbOptions values.
		
		1. pipename chooses a random pipename from list in /data/smb.py
		2. pipename_stager chooses a random pipename from list in /data/smb.py

		Output: smbOptions instance attributes are populated with random data.

		'''
		
		pipenames = random.sample(smb.pipenames,2)
		self.pipename = str(pipenames[0])
		self.pipename_stager = str(pipenames[1])

	def printify(self):

		'''
		Method to print smb options attributes to string formatted to Cobalt Strike recs.

		Output: returns a string with attribute values, headers and appropriate 
		indentation/line-breaks formatted for the smb options section of the profile.

		Example:

		set pipename "value_##";
		set pipename_stager "anotervalue_##";

		'''

		profileString = ''
		for attr, value in self.__dict__.items():
			profileString += 'set ' + attr + ' "' + value + '";\n'
		profileString += '\n'
		return profileString 