from websocket import create_connection
#create websocket connection
ws = create_connection("ws://ptl-4543182b-59b890cd.libcurl.so/pentesterlab")

#send data to server
ws.send('key')

#get result from server
result = ws.recv()
print(result)
#close connection
ws.close()