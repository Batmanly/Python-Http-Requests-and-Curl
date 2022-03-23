import socket

#create first socket conneciton tcp socket
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect server with tcp
connection.connect(('ptl-c9b3f570-6d74f0a0.libcurl.so', 80))
#send http get request with this header and convert to bytes
#Content-Type is used by browsers to tell web applications in what format is used in the body of request.


connection.send(b'GET /pentesterlab HTTP/1.1\r\nHost: ptl-c9b3f570-6d74f0a0.libcurl.so\r\nContent-Type: key/please\r\nConnection: close\r\n\r\n')
#get data from server
response = connection.recv(4096)
#write response output
print(response)


#with curl curl -X GET http://*.put_url --header "Content-Type: key/please"