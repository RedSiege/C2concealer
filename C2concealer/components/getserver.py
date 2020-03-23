import random
import base64
import uuid
import re
from ..data import reg_headers, params, transform, file_type_prepend


class getServer(object):

	'''
	Class for the http-get server component of the C2 profile.

	Profile options include:
	-Status
	-Connection
	-Content-Type
	-Server
	-Output (method for transforming beacon tasking within http server response)
	See all output options here: https://www.cobaltstrike.com/help-malleable-c2
	Ctrl-f Data Transform Language ... and you'll find it	


	'''

	def __init__(self):
		self.Status = None
		self.Connection = 'close'
		self.Content_Type = None 
		self.Server = None

		self.headerList = ['Status','Connection','Content_Type','Server']

		self.output = []

	def randomizer(self, uris):
		
		'''
		Method to generate random getServer values.

		Output: getServer instance attributes are populated with random data.

		'''

		self.status = str(200)
		self.Server = random.choice(reg_headers.server)
		

		self.output.append(random.choice(transform.transformations))
		self.output.append('base64')
		

		uris = "/" + " /".join(uris)
		regexp = re.compile(r'\.js\s')
		if regexp.search(uris) is not None:
			self.output.append('prepend "' + random.choice(file_type_prepend.js) + '"')
			self.Content_Type = 'application/javascript'
		elif '.css' in uris:
			self.output.append('prepend "' + random.choice(file_type_prepend.css) + '"')
			self.Content_Type = 'text/css'
		else:
			self.output.append('prepend "' + random.choice(file_type_prepend.html) + '"')
			self.Content_Type = 'text/html'
		
		
		self.output.append('print')

	def printify(self):

		'''
		Method to print getServer attributes to string formatted to Cobalt Strike recs.

		Output: returns a string with attribute values, headers and appropriate 
		indentation/line-breaks formatted for the http-get server section of the profile.

		Example:

			server {
	
				header "Content-Type" "text/html";

				output {
	
					netbios;
					base64;
					print;

				}

			}

		} #included to close the entire http-get section
		
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
