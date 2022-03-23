import requests
import html

#send xml post request with body

value = html.escape('"please')
print(value)

xml = f'<key value="{value}"></key>'


header = {'Content-Type': 'application/xml'}

re = requests.post('http://*.put_url', data=xml,headers=header)
print(re.text)

#with curl -X POST http://*.put_url --data '<key value="&quot;please"></key>' --header 'Content-Type: application/xml'