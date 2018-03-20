#!/usr/bin/env python

import sys
from threading import Thread
from socket import *
from time import *

UDP_PORT_SENDER = 8001
UDP_PORT_LISTENER = 8000
BUFFER_SIZE = 16  # Normally 1024, but we want fast response

# /-- Hololens Server Network ---
def sendData(data_piano):
	if 'conn' in globals():
		conn.send(data_piano.encode())  # echo
		print('Data sent: '+data_piano)
		
def UDPListener():
	print("Starting UDP Listener in "+gethostbyname("")+":"+str(UDP_PORT_LISTENER))
	sock = socket(AF_INET,SOCK_DGRAM) # Internet,UDP
	sock.bind(('', UDP_PORT_LISTENER))
	while True:
		data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
		print (str(data.decode())+"From:"+addr)
		
def UDPSender():
	print("Starting UDP Sender to port:"+str(UDP_PORT_SENDER))
	sock_sender = socket(AF_INET,SOCK_DGRAM) # Internet,UDP
	while True:
		sock_sender.sendto(("hello").encode(), (HOLOLENS_IP, UDP_PORT_SENDER))
		time.sleep(3)

# /-- Local Network ---
def startUDP(port):
	print("Starting UDP Local Server, port:"+port)
	sock = socket(AF_INET, SOCK_STREAM)
	sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	sock.bind(('localhost', int(port)))
	sock.listen(0)   # do not queue connections
	client, addr = sock.accept()
	while 1:
		data_piano = client.recv(BUFFER_SIZE)
		print("Local data piano recieved:"+data_piano)
		sendData(data_piano)
	

def main(argv):
	if(len(argv) != 2):
		print ('Sintex error, this program needs 1 arguments: recieve_send.py <port>')
		sys.exit(2)
	TCPconnection = False
	udp_server = Thread(target=startUDP,args=(argv[1],))
	udp_server.daemon = False
	udp_server.start()
	sleep(1)
	udp_listener = Thread(target=UDPListener)
	udp_listener.daemon = False
	udp_listener.start()

if __name__== "__main__":
    main(sys.argv)

