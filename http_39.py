from time import process_time_ns
import requests

import json
#send post with body json data

header = {'Content-Type':'application/json'}
#data = {'key': 'please"'}

data = {'key': 'please"'}
print(data)
re = requests.post('http://*.put_url',headers=header,json=data)

print(re.text)


#with curl curl -X POST http://*.put_url -d '{"key": "please\""}' -H 'Content-Type: application/json'