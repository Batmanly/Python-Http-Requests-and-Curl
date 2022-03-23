import requests

"""
Having the same parameter twice in a request can trigger weird behaviour in an application, especially if multiple levels of proxying are used.



"""
re = requests.post('http://*.put_url?key=please', data={'key': 'please'})
print(re.text)

#with curl curl -X POST 'http://*.put_url?key=please' --data 'key=please'