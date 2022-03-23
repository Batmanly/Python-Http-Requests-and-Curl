import requests
import json
#send post request with body

data = json.dumps({"key": "please"})
header = {'Content-Type': 'application/json'}
re = requests.get('http://*.put_url', data=data,headers=header)
print(re.text)


#with curl curl -X GET http://*.put_url --data '{"key": "please"}' --header 'Content-Type: application/json'