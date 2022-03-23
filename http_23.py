import socket

#create first socket conneciton tcp socket
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect server with tcp
connection.connect(('ptl-51036a04-1c1e2cf5.libcurl.so', 80))
#send http get request with this header and convert to bytes
#The X-Forwarded-For (XFF) request header is a de-facto standard header for identifying the originating IP address of a client connecting to a web server through a proxy server.

connection.send(b'GET /pentesterlab HTTP/1.1\r\nHost: ptl-51036a04-1c1e2cf5.libcurl.so\r\nX-Forwarded-For: 1.2.3.4\r\nConnection: close\r\n\r\n')
#get data from server
response = connection.recv(4096)
#write response output
print(response)

#with curl curl -X GET http://*.put_url --header 'X-Forwarded-For: 1.2.3.4'