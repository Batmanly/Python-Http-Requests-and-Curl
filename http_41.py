import requests
import yaml
#send post request with yaml data

header  = {'Content-Type': 'application/yaml'}

data = open('flag.yaml','rb').read()
print(data)


re = requests.post('http://*.put_url', data=data, headers=header)
print(re.text)


#curl -X POST http://*.put_url --data-binary @flag.yaml -H 'Content-Type: application/yaml' s