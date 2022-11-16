import requests

api_id='12345'
api_key='XXXXX'

headers = {
    "x-xdr-auth-id": str(api_id),
    "Authorization": api_key
}
parameters = {}
res = requests.post(url="https://api-XXX.xdr.sg.paloaltonetworks.com/public_api/v1/endpoints/get_endpoints/",
                    headers=headers,
                    json=parameters)

# importing the module
import re

# opening and reading the file
fstring = str(res.json())
fstring = fstring.replace(',','\n')
ipString=re.findall(r'(?:\d{1,3}\.)+(?:\d{1,3})',fstring)

for i in range(len(ipString)):
    print (ipString[i])
