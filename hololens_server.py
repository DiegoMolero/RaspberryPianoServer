#!/usr/bin/env python
 
import socket


TCP_IP = '172.19.248.171'

TCP_PORT = 8000
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print(s.getsockname()[0]) #HOST
print(s.getsockname()[1]) #PORT

conn, addr = s.accept()
print ('Connection address:'+ str(addr))
conn.send(b'hello')
while 1:
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	print ("received data:"+ str(data))
	conn.send(data)  # echo
conn.close()