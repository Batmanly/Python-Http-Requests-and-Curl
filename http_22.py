import socket

#create first socket conneciton tcp socket
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect server with tcp
connection.connect(('ptl-1b887537-95d2b08e.libcurl.so', 80))
#send http get request with this header and convert to bytes
#Accept-Language is used by browsers to tell web applications what language user prefers.

connection.send(b'HACK /pentesterlab HTTP/1.1\r\nHost: ptl-1b887537-95d2b08e.libcurl.so\r\nX-HTTP-Method-Override: HACK\r\nConnection: close\r\n\r\n')
#get data from server
response = connection.recv(4096)
#write response output
print(response)

#with curl curl -X HACK http://*.put_url --header 'X-HTTP-Method-Override: HACK'