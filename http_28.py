import socket

#create first socket conneciton tcp socket
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect server with tcp
connection.connect(('ptl-c5499747-83354980.libcurl.so', 80))
#send http get request with this header and convert to bytes
"""
An HTTP multipart request is an HTTP request that HTTP clients construct to send files and data over to an HTTP Server. It is commonly used by browsers and HTTP clients to upload files to the server.
"""
connection.send(b'GET /pentesterlab HTTP/1.1\r\nHost: ptl-c5499747-83354980.libcurl.so\r\nContent-Type: multipart/form-data\r\nConnection: close\r\n\r\n')
#get data from server
response = connection.recv(4096)
#write response output
print(response)

#--path-as-is mean don't touch path that i write...
# # this mean in http fragment we can use in html website to direct some path.
# we can specify path with --request-target  
#with curl curl 'http://*.put_url' --header 'Content-Type: multipart/form-data' -v