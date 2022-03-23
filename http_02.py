import socket

#create first socket conneciton tcp socket
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect server with tcp
connection.connect(('ptl-57a96561-0b82c0dc.libcurl.so', 80))
#send http get request with this header and convert to bytes
connection.send(b'GET /pentesterlab?key=please HTTP/1.1\r\nHost: ptl-57a96561-0b82c0dc.libcurl.so\r\nConnection: close\r\n\r\n')
#get data from server
response = connection.recv(4096)
#write response output
print(response)


#with curl curl -X GET http://*.put_url?key=please