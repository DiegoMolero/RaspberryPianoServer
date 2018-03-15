 #!/usr/bin/env python
import time,sys
from socket import *
TCP_PORT = 8000
BUFFER_SIZE = 1024
TOKEN="lsnu3kwbf"
UDP_PORT = 8001

MESSAGE = "Hello, World!"

def clientUDP():
	s = socket(AF_INET, SOCK_DGRAM) #create UDP socket
	s.bind((gethostbyname(gethostname()), UDP_PORT))
	while 1:
		data, addr = s.recvfrom(1024) #wait for a packet
		data=data.decode()
		if data.startswith(TOKEN):
			print ("got service announcement from", str(data[len(TOKEN):]))
			return str(data[len(TOKEN):])

def clientTCP(tcp_ip):
	s = socket(AF_INET, SOCK_STREAM)
	s.connect((tcp_ip, TCP_PORT))
	s.send(MESSAGE.encode())
	while 1:
		data = s.recv(BUFFER_SIZE)
		if not data: break
		print (str(data.decode()))
	s.close()

def main(argv):
	ip = clientUDP()
	clientTCP(ip)

if __name__== "__main__":
    main(sys.argv)