import requests
import html

xml = html.escape('<please>')
print(xml)

#send post request with body

data = f'<key><value>{xml}</value></key>'


header = {'Content-Type': 'application/xml'}
re = requests.post('http://*.put_url', data=data,headers=header)
print(re.text)


#with curl curl -X POST http://*.put_url --data '<key><value>&lt;please&gt;</value></key>' --header 'Content-Type: application/xml'