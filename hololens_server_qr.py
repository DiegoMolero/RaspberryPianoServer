#!/usr/bin/env python
 
import socket,pyqrcode,png
import sys,time
from threading import Thread
from socket import *

TCP_PORT = 8000
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
TCP_SERVER= gethostbyname(gethostname())

def setupTCP():
	print("Starting TCP Server")
	s = socket(AF_INET, SOCK_STREAM)
	s.bind((TCP_SERVER, TCP_PORT))
	s.listen(1)
	print("Listening from...")
	print("IP:\t"+gethostbyname(gethostname())) #HOST
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

def QRCode():
	#QR CODE
	qr = pyqrcode.create(TCP_SERVER)
	qr.png('qr.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
	qr.show()


def main(argv):
	tcp_server = Thread(target=setupTCP)
	tcp_server.daemon = False
	tcp_server.start()
	time.sleep(2)
	qr_thread = Thread(target=QRCode)
	qr_thread.daemon = True
	qr_thread.start()

if __name__== "__main__":
    main(sys.argv)