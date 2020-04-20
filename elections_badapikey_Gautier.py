#Michelle Gautier
#Test - This tests with an invalid api_key

import urllib.request, urllib.parse, urllib.error
import json
import ssl
print()
print('BEGIN of Second Test')
api_key = 'zaSyAkYRV9uWW5NjXSWQ9t8rO884LhcBwkE9o'
serviceurl = 'https://www.googleapis.com/civicinfo/v2/elections?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

parms = dict()
parms['key'] = api_key

url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)

try:
    uh = urllib.request.urlopen(url, context=ctx)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read())
    print('PASSED.  The api_key was invalid so the error was expected')
    quit()

print('FAILED: THIS SHOULD NOT HAVE WORKED')

