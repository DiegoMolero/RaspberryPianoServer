#!/usr/bin/env python
 
import socket,pyqrcode,png
import sys,time
from threading import Thread
from socket import *

UDP_PORT_SENDER = 8001
UDP_PORT_LISTENER = 8000
UDP_IP= ""
HOLOLENS_IP= "192.168.1.89"

BUFFER_SIZE = 1024  # Normally 1024, but we want fast response


def UDPListener():
	print("Starting UDP Listener in "+gethostbyname("")+":"+str(UDP_PORT_LISTENER))
	sock = socket(AF_INET,SOCK_DGRAM) # Internet,UDP
	sock.bind((UDP_IP, UDP_PORT_LISTENER))
	while True:
		data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
		print (str(data.decode()))
		
def UDPSender():
	print("Starting UDP Sender to port:"+str(UDP_PORT_SENDER))
	sock = socket(AF_INET,SOCK_DGRAM) # Internet,UDP
	while True:
		sock.sendto(("hello").encode(), (HOLOLENS_IP, UDP_PORT_SENDER))
		time.sleep(3)
		
def QRCode():
	#QR CODE
	qr = pyqrcode.create(UDP_IP)
	qr.png('qr.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
	qr.show()


def main(argv):
	listener = Thread(target=UDPListener)
	listener.daemon = False
	listener.start()
	sender = Thread(target=UDPSender)
	sender.daemon = False
	sender.start()
	time.sleep(2)
	qr_thread = Thread(target=QRCode)
	qr_thread.daemon = True
	qr_thread.start()

if __name__== "__main__":
    main(sys.argv)