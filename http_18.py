import requests
import urllib.parse


#make url encoding

value = urllib.parse.quote("\x00", safe="")
value = urllib.parse.quote(value, safe="")
print(value)


re = requests.get(f'http://*.put_url?key=please{value}')
print(re.text)


# curl 'http://*.put_url?key=please%2500'