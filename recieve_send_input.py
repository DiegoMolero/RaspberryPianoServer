#!/usr/bin/env python

import sys
from threading import Thread
from socket import *
from time import *

TCP_PORT = 8000
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

# /-- Hololens Server Network ---
def sendData(data):
	if 'conn' in globals():
		conn.send(base+data.encode())  # echo
		print('Data send: '+data)
def setupTCP():
	print("Starting TCP Server")
	s = socket(AF_INET, SOCK_STREAM)
	s.bind(("", TCP_PORT))
	s.listen(1)
	print("Listening from...")
	print("PORT:\t"+str(s.getsockname()[1])) #PORT
	global conn,base
	conn, addr = s.accept()
	print ('Connection address:'+ str(addr))
	conn.send('hello'.encode())
	while 1:
		base = conn.recv(BUFFER_SIZE)
		if not base: break
		print ("received data: "+ str(base.decode()))


# /-- Local Network ---
def startUDP(port):
	print("Starting UDP Local Server, port:"+port)
	sock = socket(AF_INET, SOCK_STREAM)
	sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	sock.bind(('localhost', int(port)))
	sock.listen(0)   # do not queue connections
	while 1:
		data = input("Give me input:")
		sys.stdin.readline()
		sendData(data)
	

def main(argv):
	if(len(argv) != 2):
		print ('Sintex error, this program needs 1 arguments: recieve_send.py <port>')
		sys.exit(2)
	TCPconnection = False
	udp_server = Thread(target=startUDP,args=(argv[1],))
	udp_server.daemon = False
	udp_server.start()
	sleep(1)
	tcp_server = Thread(target=setupTCP)
	tcp_server.daemon = False
	tcp_server.start()

if __name__== "__main__":
    main(sys.argv)

