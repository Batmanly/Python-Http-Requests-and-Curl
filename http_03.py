import socket

#create first socket conneciton tcp socket
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect server with tcp
connection.connect(('ptl-588a2856-bda1f76a.libcurl.so', 80))
#send http get request with this header and convert to bytes
connection.send(b'GET /pentesterlab HTTP/1.1\r\nHost: ptl-588a2856-bda1f76a.libcurl.so\r\nCookie: key=please\r\nConnection: close\r\n\r\n')
#get data from server
response = connection.recv(4096)
#write response output
print(response)


#with curl curl -X GET http://*.put_url --header "Cookie: key=please"