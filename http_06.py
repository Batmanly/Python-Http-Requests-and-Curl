import requests

#send to post requset
r = requests.post('http://*.put_url', data={'key': 'please'})
print(r.text)

#with curl curl -X POST http://*.put_url -H "Content-Lenght: 10" --data "key=please" 