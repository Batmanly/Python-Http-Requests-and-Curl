import requests

#send http multipart request


r = requests.post('http://*.put_url', files={'filename':b'test'})
print(r.text)


#with curl
# we can upload file with multipart http request
#curl -X POST http://*.put_url -F "filename=@flag.txt"