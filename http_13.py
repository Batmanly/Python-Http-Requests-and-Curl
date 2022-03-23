import requests
import urllib.parse

"""
Having the same parameter twice in a request can trigger weird behaviour in an application, especially if multiple levels of proxying are used.


"""
#make url encoding

value = urllib.parse.quote("please&", safe="")
print(value)


re = requests.get(f'http://*.put_url?key={value}')
print(re.text)


# curl 'http://*.put_url?key=please%26'