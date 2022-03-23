import socket

#create first socket conneciton tcp socket
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect server with tcp
connection.connect(('ptl-79a1417b-e5a718b3.libcurl.so', 80))
#send http get request with this header and convert to bytes
"""
This type of request is extremely useful when testing application with multiple layers of reverse proxies.
"""
connection.send(b'GET /pentesterlab#pentesterlab HTTP/1.1\r\nHost: ptl-79a1417b-e5a718b3.libcurl.so\r\nX-Forwarded-Host: pentesterlab.com\r\nConnection: close\r\n\r\n')
#get data from server
response = connection.recv(4096)
#write response output
print(response)

#--path-as-is mean don't touch path that i write...
# # this mean in http fragment we can use in html website to direct some path.
# we can specify path with --request-target  
#with curl curl 'http://*.put_url#pentesterlab' -v