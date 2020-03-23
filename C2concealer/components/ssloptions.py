

class sslOptions(object):

	'''
	Class for the ssl options section of the profile. 

	Profile options include:
	- self-signed SSL cert
	- LetsEncrypt built SSL cert
	- Pre-built keystore file and password
	- No SSL cert

	'''

	def __init__(self, ssl_dict):
		self.ssl_dict = ssl_dict 

	def randomizer(self):
		
		'''
		Method included to simplify code in profile.py. Nothing happens.

		Output: n/a

		'''
		
		pass

	def printify(self):

		'''
		Method to print ssl option attributes to string formatted to Cobalt Strike recs.

		Output: returns a string with attribute values and appropriate 
		indentation/line-breaks formatted for the smb options section of the profile.

		Example:

		https-certificate {
			set CN "google.com";
			set O "Google, Inc.";
		}

		'''

		profileString = ''
		profileString = 'https-certificate {\n'

		if self.ssl_dict['keystore']:
			profileString += '\tset keystore "' + self.ssl_dict['keystore'] + '";\n'
			profileString += '\tset password "' + self.ssl_dict['password'] + '";\n'
			profileString += '}\n\n'
		elif self.ssl_dict['self']:
			profileString += '\tset CN "' + self.ssl_dict['self']['CN'] + '";\n'
			profileString += '\tset O "' + self.ssl_dict['self']['O'] + '";\n'
			profileString += '\tset L "' + self.ssl_dict['self']['L'] + '";\n'
			profileString += '\tset ST "' + self.ssl_dict['self']['ST'] + '";\n'
			profileString += '\tset C "' + self.ssl_dict['self']['C'] + '";\n'
			profileString += '\tset validity "' + self.ssl_dict['self']['validity'] + '";\n'
			profileString += '}\n\n'
		else:
			profileString = ''

		return profileString 