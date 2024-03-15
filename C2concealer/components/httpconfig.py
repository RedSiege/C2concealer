import random
from ..data import reg_headers

class httpConfig(object):

	'''
	Class for the http config component of the C2 profile.

	Profile options include:
	- Server (this can be overridden in sub-components, in fact, the stager will
	  almost always have a varied server to avoid blue teams linking stager to redirector)
	- Trust_X_Forwarded_for (you could add this in if you want)

	From CS documentation (https://www.cobaltstrike.com/help-malleable-c2):
	"The set trust_x_forwarded_for option decides if Cobalt Strike uses the X-Forwarded-For 
	HTTP header to determine the remote address of a request. Use this option if your 
	Cobalt Strike server is behind an HTTP redirector."

        We've left it out and haven't had any issues. You'll want to use it if your team server
        is behind a redirector. If you are behind a redirect and don't set this to "true",
        the IP address you'll see for your beacons will be that of your redirector and not the
        beacon's egress IP.

	'''

	def __init__(self):
		self.Server = None
		self.attrList = ['Server']

	def randomizer(self):
		
		'''
		Method to generate random http config values.
		
		1. Choose random server value from /data/reg_headers

		Output: httpConfig instance attributes are populated with random data.

		'''
		
		self.Server = random.choice(reg_headers.server)

	def printify(self):
		
		'''
		Method to print httpConfig attributes to string formatted to Cobalt Strike recs.

		Output: returns a string with attribute values, headers and appropriate 
		indentation/line-breaks formatted for the http config section of the profile.

		Example:

		http-config {
	
			header "Server" "Apache";

		}
		
		'''
		profileString = ''
		profileString += 'http-config {\n'
		for attr in self.attrList:
			attrValue = getattr(self, attr)
			if "_" in attr:
				attr = attr.replace('_','-')
			profileString += '\theader "' + attr + '" "' + attrValue + '";\n'
		profileString += '}\n\n'
		return profileString 
