import random
import base64
import uuid
from ..data import reg_headers, params, transform


class postServer(object):

	'''
	Class for the http-post server component of the C2 profile.

	Profile options include:
	- Status
	- Connection 
	- Server

	You can always include more in here, like Content-Type and other headers

	'''

	def __init__(self):
		self.Status = None
		self.Connection = 'close'
		self.Server = None

		self.headerList = ['Status','Connection','Server']

		self.output = []

	def randomizer(self):
		
		'''
		Method to generate random postServer values.
		
		Will first check to see if value exists prior to generating new data.

		Output: postServer instance attributes are populated with random data.

		'''
		
		self.Status = str(200)
		self.Server = random.choice(reg_headers.server)
		self.output.append('base64')
		self.output.append('print')

	def printify(self):

		'''
		Method to print postServer attributes to string formatted to Cobalt Strike recs.

		Output: returns a string with attribute values, headers and appropriate 
		indentation/line-breaks formatted for the http-post server section of the profile.

		Example:

			server {
	
				output {
	
					netbios;
					base64;
					print;

				}

			}

		} #included to close the entire http-post section
		
		'''

		profileString = ''
		
		profileString += '\tserver {\n\n'

		for header in self.headerList:
			headerValue = getattr(self, header)
			if headerValue == None:
				continue
			if "_" in header:
				header = header.replace("_","-")
			profileString += '\t\theader "' + header + '" "' + headerValue + '";\n'

		profileString += '\n'

		profileString += '\t\toutput {\n'
		for item in self.output:
			profileString += '\t\t\t' + item + ';\n'
		profileString += '\t\t}\n\n'

		profileString += '\t}\n\n'
		profileString += '}\n'
		
		return profileString 