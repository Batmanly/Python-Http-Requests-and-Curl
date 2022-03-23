import requests

#send post request with body

body = b'<key><value>please</value></key>'

re = requests.post('http://*.put_url', data=body)
print(re.text)


#with curl curl -X POST http://*.put_url --data '<key><value>please</value></key>'