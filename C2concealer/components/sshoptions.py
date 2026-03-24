import random
from ..data import ssh

class sshOptions(object):

	'''
	Class for the ssh options section of the profile.

	Profile options include:
	- ssh_pipename

	For more info:
	https://www.cobaltstrike.com/help-malleable-c2

	Ctrl-f smb ... and you'll see a table explaining these two values

	'''

	def __init__(self):
		self.ssh_pipename = None


	def randomizer(self):
		
		'''
		Method to generate random smbOptions values.
		
		1. ssh_pipename chooses a random pipename from list in /data/ssh.py

		Output: sshOptions instance attributes are populated with random data.

		'''

		#pipenames = random.sample(ssh.pipenames, 1)
		self.ssh_pipename = str(random.sample(ssh.pipenames, 1)[0])


	def printify(self):

		'''
		Method to print ssh options attributes to string formatted to Cobalt Strike recs.

		Output: returns a string with attribute values, headers and appropriate 
		indentation/line-breaks formatted for the smb options section of the profile.

		Example:

		set ssh_pipename "value_##";

		'''

		profileString = ''
		for attr, value in self.__dict__.items():
			profileString += 'set ' + attr + ' "' + value + '";\n'
		profileString += '\n'
		return profileString 