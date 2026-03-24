'''

##################################################################################
Data set containing common headers + values, including:
servers, user-agents, common cookie prefixes and suffixes, 
accept, accept values for the http-stager (meaning all .gif,.png,.jpg type values)
accept_encoding, and accept_language.
##################################################################################

'''
#CUSTOMIZE WITH YOUR OWN SERVER STRINGS#
server = ['Apache','nginx','apache','Microsoft-IIS/10.0','ESF','cloudflare','openresty','LightSpeed','gws','gunicorn/25.1.0']

#CUSTOMIZE WITH YOUR OWN COOKIE NAMES#
cookie_prefixes = ['PHPSESSID','JSESSIONID','wordpress_ed1f617bbd6c004cc09e046f3c1b7148','wordpress_d6c0405e0d7ab18fd4e6a0b74fce40b0',
                   '_utma','connect.sid','remember_token','remember_me_token','_hJsession','_hjid','OptanonConsent','_stripe_mid',
                   '_stripe_sid','auth','LSID','HSID','lu','affiliate_id','XSRF-TOKEN','csrf_token']

cookie_suffixes = ['secure', 'path=/', 'HttpOnly']

#CUSTOMIZE WITH YOUR OWN ENVIRONMENT RELEVANT USER AGENT STRINGS#
#*Note: some of these non-windows strings probably won't make sense for your target env*#
user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 18_7_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 18_7_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/149.0 Mobile/15E148 Safari/605.1.15",
"Mozilla/5.0 (Linux; Android 16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.7680.154 Mobile Safari/537.36",
"Mozilla/5.0 (Android 16; Mobile; rv:68.0) Gecko/68.0 Firefox/148.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.3856.78",
"Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko",
]

#CUSTOMIZE WITH YOUR OWN ACCEPT VALUES#
accept = ["text/html",
"*/*",
]

accept_stager = ["*/*", "image/*","image/jpeg",]

#CUSTOMIZE WITH YOUR OWN ACCEPT ENCODING VALUES#
accept_encoding = ['gzip, br', 'gzip', 'br']

#CUSTOMIZE WITH YOUR OWN ACCEPT LANGUAGE VALUES#
accept_language = ['en-US', 'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5', 'en-GB;q=0.9, *;q=0.7',]

#CUSTOMIZE WITH YOUR OWN CONTENT ENCODING VALUES#
content_encoding = ['gzip', 'deflate', 'br',]
