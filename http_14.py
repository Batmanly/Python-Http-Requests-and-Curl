import requests
import urllib.parse

"""
Having the same parameter twice in a request can trigger weird behaviour in an application, especially if multiple levels of proxying are used.


"""
#make url encoding

value = urllib.parse.quote("?key", safe="")
print(value)


re = requests.get(f'http://*.put_url?{value}=please')
print(re.text)


# curl 'http://*.put_url?%3Fkey=please'