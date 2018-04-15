#!/usr/bin/env python

import sys,pyqrcode,png
from tkinter import *
from threading import Thread
from socket import *
from time import *

TCP_PORT = 8000
BUFFER_SIZE = 16  # Normally 1024, but fast response is needed
def doSomething(event):
    print ("bye")
    sleep(0.5)
    root.destroy()


def drawQR(code):
    url = pyqrcode.create(code)
    url.png('qr.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    img = PhotoImage(file="qr.png")
    panel = Label(root, image=img)
    panel.grid(row=0,column=0, sticky=E)
    panel.mainloop()

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
    if (len(argv) != 3):
        print('Sintex error, this program needs 2 arguments: main.py <ip> <port>')
        sys.exit(2)
    init_Services(argv[2])
    init_GUI()
    drawQR(argv[1])
    #root.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window
    root.mainloop()

def init_GUI():
    global root
    global info_label_server,info_label_piano,label_0
    root = Tk()
    label_0 = Label(root, text="Run MagicPiano and Scan the QR showed")
    label_1 = Label(root, text="Info Piano: ")
    label_2 = Label(root, text="Info Hololens Server: ")

    info_label_piano = Label(root, text="Disconnected")
    info_label_server = Label(root, text="Disconnected")

    label_0.grid(row=0,column = 1)
    label_1.grid(row=1,column = 0,sticky =W)
    label_2.grid(row=2,column = 0,sticky =W)

    info_label_piano.grid(row=1,column=1)
    info_label_server.grid(row=2, column=1)

def init_Services(port):
    udp_server = Thread(target=startUDP, args=(port,))
    udp_server.daemon = False
    udp_server.start()
    sleep(1)
    tcp_server = Thread(target=setupTCP)
    tcp_server.daemon = False
    tcp_server.start()

def update_label_serverTCP(msg):
    info_label_server.configure(text = msg)

def update_label_Piano(msg):
    info_label_piano.configure(text = msg)

def update_label_Info(msg):
    label_0.configure(text=msg)


if __name__== "__main__":
    main(sys.argv)





