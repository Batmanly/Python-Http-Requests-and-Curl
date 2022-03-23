import requests
import yaml
#send post request with yaml data

header  = {'Content-Type': 'application/yaml'}

data = b'key: please'


re = requests.post('http://*.put_url', data=data, headers=header)
print(re.text)


# curl -X POST http://*.put_url -d 'key: please' -H 'Content-Type: application/yaml'