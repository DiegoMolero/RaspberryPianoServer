 #!/usr/bin/env python
import socket


TCP_IP = '172.31.254.97'
TCP_PORT = 8000
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode())
while 1:
	data = s.recv(BUFFER_SIZE)
	if not data: break
	print (str(data.decode()))
s.close()
