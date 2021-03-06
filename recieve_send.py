#!/usr/bin/env python

import sys
from threading import Thread
from socket import *
from time import *

TCP_PORT = 8000
BUFFER_SIZE = 16  # Normally 1024, but we want fast response

# /-- Hololens Server Network ---
def sendData(data_piano):
	if 'conn' in globals():
		conn.send(data_piano.encode())  # echo
		print('Data sent: '+data_piano)
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
	client, addr = sock.accept()
	while 1:
		data_piano = client.recv(BUFFER_SIZE)
		data_send = data_piano.replace('\n','') # Removes the first line break
		print("Local data piano recieved:"+data_send)
		sendData(data_send+'\n') # The line break signal the final of the message
	

def main(argv):
	if(len(argv) != 2):
		print ('Sintex error, this program needs 1 arguments: recieve_send.py <port>')
		sys.exit(2)
	udp_server = Thread(target=startUDP,args=(argv[1],))
	udp_server.daemon = False
	udp_server.start()
	sleep(1)
	tcp_server = Thread(target=setupTCP)
	tcp_server.daemon = False
	tcp_server.start()

if __name__== "__main__":
    main(sys.argv)

