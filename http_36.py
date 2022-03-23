import requests


#send xml post request with body

xml = '<key value="please"></key>'
header = {'Content-Type': 'application/xml'}

re = requests.post('http://*.put_url', data=xml,headers=header)
print(re.text)

#with curl -X POST http://*.put_url --data '<key value="please"></key>' --header 'Content-Type: application/xml'