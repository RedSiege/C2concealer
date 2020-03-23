import random
import base64
import uuid
from ..data import stage, reg_headers, params

class stagerServer(object):

	'''
	Class for the stager server component of the C2 profile.

	Profile options include:
	- Content-Type
	- Server
	- Connection
	- Output (for transforming and storing the payload output)

	'''

	def __init__(self):
		self.Content_Type = None 
		self.Server = None
		self.Connection = 'close'
		self.output = []
		self.headerlist = ['Content_Type','Server','Connection']

	def randomizer(self):
		
		'''
		Method to generate random stagerServer values.
		
		1. Choose a random image type to use in stager section. Apply values to Content-Type.
		2. Choose a server at random.
		3. If cookie, create a random cookie value using two random words, choose a cookie prefix and then set
		the cookie value equal to that prefix. Choose 0-2 cookie suffixes (ex: HttpOnly)
		

		Output: stagerServer instance attributes are populated with random data.

		'''
		
		img_type = random.choice(stage.binary_types)
		self.output.append('print')
		self.Content_Type = img_type['content_type']
		self.Server = random.choice(reg_headers.server)

		cookie = random.randint(0,1)
		if cookie:
			#CUSTOMIZE how the cookie_val is created and how it's encoded in the following line#
			cookie_val = random.choice(params.words) + "&" + random.choice(params.words)
			self.Set_Cookie = random.choice(params.common_params) + "=" + base64.b64encode(cookie_val.encode("utf-8")).decode()
			cookie_suffix_count = random.randint(0,1)
			cookie_suffixes = random.sample(reg_headers.cookie_suffixes,cookie_suffix_count)
			for suffix in cookie_suffixes:
				self.Set_Cookie += "; " + suffix



	def printify(self):

		'''
		Method to print stagerServer attributes to string formatted to Cobalt Strike recs.

		Output: returns a string with attribute values, headers and appropriate 
		indentation/line-breaks formatted for the stager server section of the profile.

		Example:

			server {
	
				header "Content-Type" "text/html";

				output {
	
					print;

				}

			}

		} #included to close the entire stager section
		
		'''

		profileString = ''
		
		profileString += '\tserver {\n\n'

		for header in self.headerlist:
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