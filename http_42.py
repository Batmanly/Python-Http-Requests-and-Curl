import requests
#create session
session = requests.Session()

session.auth = ('key', 'please')

re = session.get('http://*.put_url')
print(re.text)


#with curl curl -X GET http://*.put_url --header Authorization: Basic a2V5OnBsZWFzZQ=='