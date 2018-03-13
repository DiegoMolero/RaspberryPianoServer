#!/usr/bin/env python
 
import socket,pyqrcode,png

TCP_IP = ''
TCP_PORT = 8000
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
TCP_SERVER= socket.gethostbyname(socket.gethostname())

#SET UP SERVER
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

#CONSOLE INFO
print("Listening from...")
print("IP:\t"+TCP_SERVER) #HOST
print("PORT:\t"+str(s.getsockname()[1])) #PORT

#QR CODE
qr = pyqrcode.create(TCP_SERVER)
qr.png('qr.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
qr.show()

#CONNECTION
conn, addr = s.accept()
print ('Connection address:'+ str(addr))
conn.send('hello'.encode())
while 1:
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	print ("received data: "+ str(data.decode()))
	conn.send(data)  # echo
conn.close()