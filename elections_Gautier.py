#Michelle Gautier
#Test - This is the happy path test
#  Test structure of data, values of data and how many election records are in the json

import urllib.request, urllib.parse, urllib.error
import json
import ssl
print('BEGIN of First Test')
api_key = 'AIzaSyAkYRV9uWW5NjXSWQ9t8rO884LhcBwkE9o'
serviceurl = 'https://www.googleapis.com/civicinfo/v2/elections?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

parms = dict()
parms['key'] = api_key

url = serviceurl + urllib.parse.urlencode(parms)

try:
    uh = urllib.request.urlopen(url, context=ctx)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read())

data = uh.read().decode()

try:
     js = json.loads(data)
except:
    js = None

if not js:
    print('==== Failure To Retrieve ====')
    print(data)

# This is to test the # of elections we expect in the response are there
if len(js['elections']) == 3:
    print('SUCCESS:  Length of data matches expectation (3 records)')
else:
    print('FAILED:  Length of data does not match expectation (expect 3 records)')

for election in js['elections']:
    print('***********New Election - going through the file*************')
    # This is to test to ensure the fields we expect in the response are there (my example: id)
    if 'id' not in election:
        print('   * No election id found')
        continue
    else:
        print('SUCCESS:  id field was found')

# This is to test to ensure the values we expect in the response are there (my excample: name)
    if election['name'] != 'VIP Test Election':
        print('FAILED:  name is not correct - should get on the second and third one')
    else:
        print('SUCCESS:  name is correct - should get on the first one')


