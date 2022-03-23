import requests

#send to post requset
r = requests.get('http://*.put_url', data={'key': 'please'})
print(r.text)

#with curl curl -X GET http://*.put_url  --data "key=please" 