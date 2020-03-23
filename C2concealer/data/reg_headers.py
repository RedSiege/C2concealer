'''

##################################################################################
Data set containing common headers + values, including:
servers, user-agents, common cookie prefixes and suffixes, 
accept, accept values for the http-stager (meaning all .gif,.png,.jpg type values)
accept_encoding, and accept_language.
##################################################################################

'''
#CUSTOMIZE WITH YOUR OWN SERVER STRINGS#
server = ['Apache','nginx','apache', 'ESF','cloudflare','golfe2','Pagely Gateway/1.5.1']

#CUSTOMIZE WITH YOUR OWN COOKIE NAMES#
cookie_prefixes = ['LSID', 'HSID', 'SSID', 'made_write_conn', 'reg_fb_gate', 'lu', 'affiliate_id', 'wordpress_52238558e930f1ec699e4f12ab015a4f',
'wordpress_ed1f617bbd6c004cc09e046f3c1b7148', 'wordpress_d6c0405e0d7ab18fd4e6a0b74fce40b0', 'wordpress_logged_in',
'wordpress_logged_in_1870a829d9bc69abf500eca6f00241fe', 'woocommerce_cart_hash', 'woocommerce_items_in_cart',
'wp_woocommerce_session_']

cookie_suffixes = ['secure', 'path=/', 'HttpOnly']

#CUSTOMIZE WITH YOUR OWN ENVIRONMENT RELEVANT USER AGENT STRINGS#
#*Note: some of these non-windows strings probably won't make sense for your target env*#
user_agent = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202",
"Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0",
"Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko)",
"Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
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
