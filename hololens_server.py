#!/usr/bin/env python
 
import socket
TCP_IP = ''
#TCP_IP = socket.gethostbyname(socket.gethostname())

TCP_PORT = 8000
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print("Listening from...")
print("IP:\t"+socket.gethostbyname(socket.gethostname())) #HOST
print("PORT:\t"+str(s.getsockname()[1])) #PORT

conn, addr = s.accept()
print ('Connection address:'+ str(addr))
conn.send('hello'.encode())
while 1:
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	print ("received data: "+ str(data.decode()))
	conn.send(data)  # echo
conn.close()