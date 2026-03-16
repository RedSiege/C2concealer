'''

##########################################
Data set containing common dns subdomains. 
##########################################

'''
#Customize this#
subdomains = ['ns0','ns1','ns2']

normal_subdomains = ['test', 'online', 'remote', 'read', 'dns', 'smtp', 'pants', 'socks', 'front', 'back', 'left', 'right', 'up', 'down', 'sub', 'relate', 'answer', 'bag', 'box', 'peg', 'chair', 'phone', 'speaker', 'remote', 'light', 'lantern', 'roller', 'vase', 'small', 'tiny', 'sauce']

doh_servers = [
    'cloudflare-dns.com',
    'mozilla.cloudflare-dns.com',
    'dns.google',
    'dns.quad9.net',
    'dns.adguard.com',
    'doh.opendns.com',
]

doh_useragents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
    'curl/8.4.0',
    'dnscrypt-proxy/2.1.5',
]