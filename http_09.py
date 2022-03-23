import socket

#create first socket conneciton tcp socket
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect server with tcp
connection.connect(('ptl-ad7f4244-fffa456d.libcurl.so', 80))
#send http get request with this header and convert to bytes
#Content-Type is used by browsers to tell web applications in what format is used in the body of request.
req = b'GET /pentesterlab?key=please&key=please HTTP/1.1\r\nHost: ptl-ad7f4244-fffa456d.libcurl.so\r\n'
req += b'Connection: close\r\n\r\n'
connection.send(req)
#get data from server
response = connection.recv(4096)
#write response output
print(response)


#with curl curl -X GET 'http://*.put_url?key=please&key=please'