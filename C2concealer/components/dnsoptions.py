import random
from ..data import dns

class dnsOptions(object):

    '''
    Class for the dns options section of the profile. 

    Profile options include:
    - dns_idle
    - dns_stager_subhost
    - dns_stager_prepend
    - maxdns
    - dns_sleep
    - dns_ttl
    - dns_max_txt

    Learn more about these values here:
    https://www.cobaltstrike.com/help-malleable-c2
    > Ctrl-f dns_ and you'll find it

    '''

    def __init__(self, name):
        self.dns_idle = None
        self.dns_stager_subhost = None
        #self.dns_stager_prepend = None
        self.maxdns = None
        self.dns_sleep = None
        self.dns_ttl = None
        self.dns_max_txt = None
        #These are added in 4.3
        self.beacon = None
        self.get_A = None
        self.get_AAAA = None
        self.get_TXT = None
        self.put_metadata = None
        self.put_output = None
        self.ns_response = "zero"
        self.name = name

    def randomizer(self):
        
        '''
        Method to generate random dnsOptions values.
        
        1. dns_idle any valid IP address not starting with 0, 10, 172, 192 or 255
        2. dns_stager_subhost - pull a random subdomain from list in /data/dns.py & add a "."
        3. maxdns = random integer between 240 and 255
        4. dns_sleep = random integer between 100 and 150 (ms)

        #static
        1. dns_ttl static and set to 3600
        2. dns_max_txt static and set to 252

        Output: dnsOptions instance attributes are populated with random data.

        '''
        
        ip_num = list(range(1,9)) + list(range(11,171)) + list(range(173,191)) + list(range(193,254))
        self.dns_idle = ".".join(map(str, (random.choice(ip_num) for _ in range(4))))
        self.dns_stager_subhost = str(random.choice(dns.subdomains)) + "."
        self.maxdns = str(random.randint(240,255))
        self.dns_sleep = str(random.randint(100,150))

        #static
        self.dns_max_txt = str(252)
        self.dns_ttl = str(3600)

        # After 4.3
        self.beacon = str(random.choice(dns.normal_subdomains)) + "."
        self.get_A = str(random.choice(dns.normal_subdomains)) + "."
        self.get_AAAA = str(random.choice(dns.normal_subdomains)) + "."
        self.get_TXT = str(random.choice(dns.normal_subdomains)) + "."
        self.put_metadata = str(random.choice(dns.normal_subdomains)) + "."
        self.put_output = str(random.choice(dns.normal_subdomains)) + "."


    def printify(self):

        '''
        Method to print dns options attributes to string formatted to Cobalt Strike recs.

        Output: returns a string with attribute values, headers and appropriate 
        indentation/line-breaks formatted for the dns options section of the profile.

        Example:

        set dns_idle "8.8.8.8";
        set maxdns "245";
        set dns_sleep "0";

        '''

        profileString = ''
        profileString += 'dns-beacon "' + self.name + '" {\n\n'
        for attr, value in self.__dict__.items():
            if (attr == 'name'): continue
            profileString += '\tset ' + attr + ' "' + value + '";\n'
        profileString += '\n'
        profileString += '}\n\n'
        return profileString
