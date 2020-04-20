#Michelle Gautier
#Test - This is testing the data in the headers - this test will verify the content-type header
#value to ensure it is json

import urllib.request, urllib.parse, urllib.error
import json
import ssl
print()
print('BEGIN of Third Test')
api_key = 'AIzaSyAkYRV9uWW5NjXSWQ9t8rO884LhcBwkE9o'
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

data = uh.read().decode()

headers = dict(uh.getheaders())

if headers['Content-Type'] != 'application/json; charset=UTF-8':
    print('FAILED - Content Type is incorrect')
else:
    print('SUCCESS - Content Type is application/json; charset=UTF-8')
