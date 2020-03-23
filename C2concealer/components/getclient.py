import random
import base64
import uuid
from ..data import urls, transform, reg_headers, params

class getClient(object):

	'''
	Class for the http-get client component of the C2 profile.

	Profile options include:
	- uri
	- host
	- connection
	- Accept
	- Accept-Encoding
	- Accept-Language
	- metadata (aka how to transform and store C2 client payload)
	- http-get parameters
	
	'''

	def __init__(self, name, host):
		self.uri = []
		self.Host = host
		self.Accept = None
		self.Accept_Encoding = None
		self.Accept_Language = None
		self.Connection = 'close'
		self.optionalHeaders = ['Accept', 'Accept_Encoding', 'Accept_Language']
		self.headerList = ['Host', 'Connection','Accept', 'Accept_Encoding', 'Accept_Language']
		self.metadata = []
		self.parameters = {}
		self.name = name

	def randomizer(self):
		
		'''
		Method to generate random getClient values.
		
		1. For uri, grab a url path from /data/urls
		2. Choose 0 - 2 headers from among Accept, Accept-Encoding, Accept-Language
		3. Randomly choose 1 transformation for metadata, base64 encode it, then append a cookie_prefix from /data/reg_headers
		and then throw into the Cookie header.
		4. Generate random params

		Output: getClient instance attributes are populated with random data.

		'''

		uris = random.sample(urls.urls, random.randint(1,3))
		new_uris = []
		if(random.randint(0,1)):
			file_type = random.choice(urls.file_types)
			for uri in uris:
				new_uris.append(uri + "." + file_type)
		else:
			new_uris = uris
		self.uri = new_uris		 

		optional = random.sample(self.optionalHeaders, random.randint(0,2))
		for header in optional:
			if header == 'Accept':
				self.Accept = random.choice(reg_headers.accept_stager)
			elif header == 'Accept_Encoding':
				self.Accept_Encoding = random.choice(reg_headers.accept_encoding)
			elif header == 'Accept_Language':
				self.Accept_Language = random.choice(reg_headers.accept_language)
		
		self.metadata.append(random.choice(transform.transformations))
		self.metadata.append('base64')
		self.metadata.append('prepend "' + random.choice(reg_headers.cookie_prefixes) + '="')
		self.metadata.append('header "Cookie"')

		common_params = random.sample(params.common_params,random.randint(0,1))
		for param in common_params:
			#CUSTOMIZE THIS LIST OF PARAM VALUES (doesn't have any impact on performance)#
			paramVal = random.choice(['true','false',])
			self.parameters[param] = paramVal

	def printify(self):

		'''
		Method to print getClient attributes to string formatted to Cobalt Strike recs.

		Output: returns a string with attribute values, headers and appropriate 
		indentation/line-breaks formatted for the http-get client section of the profile.

		Example:

			http-get "default" {
		
				set uri "/some/uri";

				client {
		
					header "Host" "somehost.com";
					header "Connection" "close";

					metadata {
		
						base64;
						header "Cookie";

					}

					parameter "apple" "green";

				}
			}
		
		'''

		profileString = ''
		profileString += 'http-get "' + self.name + '" {\n\n'

		profileString += '\tset uri "/' + " /".join(self.uri) + '";\n\n' 

		profileString += '\tclient {\n\n'

		for header in self.headerList:
			headerValue = getattr(self, header)
			if headerValue == None:
				continue
			if "_" in header:
				header = header.replace("_","-")
			profileString += '\t\theader "' + header + '" "' + headerValue + '";\n'

		profileString += '\n'

		profileString += '\t\tmetadata {\n'
		for item in self.metadata:
			profileString += '\t\t\t' + item + ';\n'
		profileString += '\t\t}\n\n'

		for param, value in self.parameters.items():
			profileString += '\t\tparameter "' + param + '" "' + value + '";\n'
		profileString += '\n'

		profileString += '\t}\n'
		
		return profileString 
