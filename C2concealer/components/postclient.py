import random
import base64
import uuid
from ..data import urls, transform, reg_headers, params

class postClient(object):

	'''
	Class for the http-post client component of the C2 profile.

	Profile options include:
	- uri
	- hostname
	- connection header
	- output (aka how to transform and store C2 client payload)
	- id (a session id to associate output with the right session)
	
	Note: 
	- The http-post level attribute "URI" is instantiated here.

	'''

	def __init__(self, name, host):
		self.uri = []
		self.Host = host
		#self.Accept = None
		self.Accept_Encoding = None
		self.Accept_Language = None
		self.Connection = 'close'
		self.Content_Type = None
		self.optionalHeaders = ['Accept_Encoding', 'Accept_Language']
		self.headerList = ['Host', 'Connection', 'Accept_Encoding', 'Accept_Language', 'Content_Type']
		self.output = []
		self.id = []
		self.name = name

	def randomizer(self):
		
		'''
		Method to generate random postClient values.
		
		1. Choose 1-3 uris, optionally include a specific file type in uri.
		2. Choose 0-2 optional headers and generate random values.
		3. Create a session ID and store it in the cookie field
		4. Choose a type of form-upload and store output in there.

		NOTE: originally included multipart/form-data as a data output option, but
		it was consistently failing c2lint. code is below:

			boundary = "-"*random.randint(3,5) + str(uuid.uuid4())[:random.randint(5,9)].replace("-","")
			self.Content_Type = 'multipart/form-data; boundary=' + boundary
			self.output.append('prepend "Content-Disposition: form-data; name=\'' + \
								random.choice(params.secret_params) + '\'\\r\\n\\r\\n"')
			self.output.append('prepend "--' + boundary + '\\r\\n"')
			self.output.append('append "--' + boundary + '--\\r\\n"')

		NOTE: removed the accept header since it was causing size issues + not sure it mattered that much

		Output: postClient instance attributes are populated with random data.

		'''
		uris = random.sample(urls.urls, random.randint(1,3))
		if(random.randint(0,1)):
			for uri in uris:
				uri +=  "." + random.choice(urls.file_types)
		self.uri = uris

		optional = random.sample(self.optionalHeaders, random.randint(0,1))
		for header in optional:
			if header == 'Accept_Encoding':
				self.Accept_Encoding = random.choice(reg_headers.accept_encoding)
			elif header == 'Accept_Language':
				self.Accept_Language = random.choice(reg_headers.accept_language)

		self.id.append('base64')
		#CUSTOMIZE this prepend value#
		self.id.append('prepend "__session__id="')
		self.id.append('header "Cookie"')

		self.output.append(random.choice(transform.transformations))
		self.output.append('base64')

		form_type = random.randint(1,2)

		if(form_type == 1):
			self.Content_Type = 'application/x-www-form-urlencoded'
			self.output.append('prepend "' + random.choice(params.common_params) + '="')
		else:
			self.Content_Type = 'text/plain'
		self.output.append('print')

	def printify(self):

		'''
		Method to print postClient attributes to string formatted to Cobalt Strike recs.

		Output: returns a string with attribute values, headers and appropriate 
		indentation/line-breaks formatted for the http-post client section of the profile.

		Example:

			http-post "default" {
		
				set uri "/some/uri";

				client {
		
					header "Host" "somehost.com";
					header "Connection" "close";

					output {
		
						base64;
						print;

					}

					id {
		
						netbios;
						base64;
						prepend="__session__id=";
						header "Cookie";

					}

				}
			}
		
		'''

		profileString = ''
		profileString += 'http-post "' + self.name + '" {\n\n'

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

		profileString += '\t\toutput {\n'
		for item in self.output:
			profileString += '\t\t\t' + item + ';\n'
		profileString += '\t\t}\n\n'

		profileString += '\t\tid {\n'
		for item in self.id:
			profileString += '\t\t\t' + item + ';\n'
		profileString += '\t\t}\n\n'

		profileString += '\t}\n'
		
		return profileString 
