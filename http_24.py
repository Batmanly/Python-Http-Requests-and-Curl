import socket

#create first socket conneciton tcp socket
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect server with tcp
connection.connect(('ptl-80a884bc-841409fe.libcurl.so', 80))
#send http get request with this header and convert to bytes
"""
The X-Forwarded-Host (XFH) header is a de-facto standard header for identifying the original host requested by the client in the Host HTTP request header.

Host names and ports of reverse proxies (load balancers, CDNs) may differ from the origin server handling the request, in that case the X-Forwarded-Host header is useful to determine which Host was originally used.

"""
connection.send(b'GET /pentesterlab HTTP/1.1\r\nHost: ptl-80a884bc-841409fe.libcurl.so\r\nX-Forwarded-Host: pentesterlab.com\r\nConnection: close\r\n\r\n')
#get data from server
response = connection.recv(4096)
#write response output
print(response)

#with curl curl -X GET http://*.put_url --header 'X-Forwarded-Host: pentesterlab.com'