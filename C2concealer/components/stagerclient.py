import random
import uuid
import base64
from ..data import params, reg_headers, urls

class stagerClient(object):

	'''
	Class for the stager client component of the C2 profile.

	Profile options include:
	- uri_x86 (uri for 32-bit payload) 
	- uri_x64 (uri for 64-bit payload)
	- host
	- connection
	- Accept
	- Accept-Encoding
	- Accept-Language
	
	Note: 
	- The stager level attribute "URI" is instantiated here.
	
	'''

	def __init__(self, name, host):
		self.uri_x86 = None
		self.uri_x64 = None
		self.Host = host 
		self.Accept = None
		self.Accept_Encoding = None
		self.Accept_Language = None
		self.Connection = 'close'
		self.optionalHeaders = ['Accept', 'Accept_Encoding', 'Accept_Language']
		self.headerList = ['Host', 'Connection', 'Accept', 'Accept_Encoding', 'Accept_Language']
		self.name = name
		

	def randomizer(self):
		
		'''
		Method to generate random stagerClient values.
		
		1. For both uri_x86 and x64, grab a url path from /data/urls
		2. Choose 0 - 2 headers from among Accept, Accept-Encoding, Accept-Language

		Note: the URI file extension is determined in the consistenceCheck() func
		located in profile.py. That's bc we first need to see what the content-type
		value is from the stageserver.py file, which isn't linked to this class at all.

		Output: stagerClient instance attributes are populated with random data.

		'''
		
		self.uri_x86 = random.choice(urls.stager_urls) + "/" + random.choice(urls.urls)
		self.uri_x64 = random.choice(urls.stager_urls) + "/" + random.choice(urls.urls)
		 
		optional = random.sample(self.optionalHeaders, random.randint(0,2))
		for header in optional:
			if header == 'Accept':
				self.Accept = random.choice(reg_headers.accept_stager)
			elif header == 'Accept_Encoding':
				self.Accept_Encoding = random.choice(reg_headers.accept_encoding)
			elif header == 'Accept_Language':
				self.Accept_Language = random.choice(reg_headers.accept_language)
		

	def printify(self):

		'''
		Method to print stagerClient attributes to string formatted to Cobalt Strike recs.

		Output: returns a string with attribute values, headers and appropriate 
		indentation/line-breaks formatted for the stager client section of the profile.

		Example:

			http-stager "default" {
		
				set uri_x86 "/32";
				set uri_x64 "/64";

				client {
		
					header "Host" "somehost.com";
					header "Connection" "close";

				}
			}
		
		'''

		profileString = ''
		profileString += 'http-stager "' + self.name + '" {\n\n'

		profileString += '\tset uri_x86 "/' + self.uri_x86 + '";\n' 
		profileString += '\tset uri_x64 "/' + self.uri_x64 + '";\n\n'

		profileString += '\tclient {\n\n'

		for header in self.headerList:
			headerValue = getattr(self, header)
			if headerValue == None:
				continue
			if "_" in header:
				header = header.replace("_","-")
			profileString += '\t\theader "' + header + '" "' + headerValue + '";\n'

		profileString += '\n'
		profileString += '\t}\n'
		
		return profileString 
