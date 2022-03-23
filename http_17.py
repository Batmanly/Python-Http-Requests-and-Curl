import requests
import urllib.parse

#make url encoding

value = urllib.parse.quote("please&", safe="")
print(value)


re = requests.get(f'http://*.put_url?key={value}')
print(re.text)


# curl 'http://*.put_url?key=please%26'