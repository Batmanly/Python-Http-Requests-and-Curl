import requests

re = requests.post('http://*.put_url', data={'key': 'please','key': 'please'})
print(re.text)

#with curl curl -X POST http://*.put_url --data 'key=please&key=please'