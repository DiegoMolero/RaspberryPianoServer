#!/usr/bin/env python

import sys,time
from threading import Thread
from socket import *
#TCP_IP = ''
TCP_IP = gethostbyname(gethostname())
TOKEN="lsnu3kwbf"
UDP_PORT = 8001
TCP_PORT = 8000
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

def setupUDP():
	print("Starting UDP Clint to port: "+str(UDP_PORT)+" ...")
	us = socket(AF_INET, SOCK_DGRAM) #create UDP socket
	us.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) #this is a broadcast socket
	my_ip= gethostbyname(gethostname()) #get our IP. Be careful if you have multiple network interfaces or IPs
	while 1:
		data = TOKEN+my_ip
		us.sendto(data.encode(), ('<broadcast>', UDP_PORT))
		print ("sent service announcement")
		time.sleep(5)

def setupTCP():
	print("Starting TCP Server")
	s = socket(AF_INET, SOCK_STREAM)
	s.bind((TCP_IP, TCP_PORT))
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

def main(argv):
	udp_server = Thread(target=setupUDP)
	udp_server.daemon = False
	udp_server.start()
	time.sleep(2)
	tcp_server = Thread(target=setupTCP)
	tcp_server.daemon = False
	tcp_server.start()

if __name__== "__main__":
    main(sys.argv)