import socket

#create first socket conneciton tcp socket
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect server with tcp
connection.connect(('ptl-7b1da6d3-ba1bb192.libcurl.so', 80))
#send http get request with this header and convert to bytes
#Accept-Language is used by browsers to tell web applications what language user prefers.

connection.send(b'GET /pentesterlab HTTP/1.1\r\nHost: ptl-7b1da6d3-ba1bb192.libcurl.so\r\nAccept-Language: key-please\r\nConnection: close\r\n\r\n')
#get data from server
response = connection.recv(4096)
#write response output
print(response)


#with curl curl -X GET http://*.put_url --header "Accept-Language: key-please"