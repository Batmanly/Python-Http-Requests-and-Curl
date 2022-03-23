import socket

#create first socket conneciton tcp socket
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect server with tcp
connection.connect(('ptl-1a9a14d6-337c7c24.libcurl.so', 80))
#send http get request with this header and convert to bytes

connection.send(b'POST /pentesterlab HTTP/1.1\r\nHost: ptl-1a9a14d6-337c7c24.libcurl.so\r\nConnection: close\r\n\r\n')

#connection.send(b'key=please')
#get data from server
response = connection.recv(4096)
#write response output
print(response)


#with curl curl -X POST http://*.put_url 