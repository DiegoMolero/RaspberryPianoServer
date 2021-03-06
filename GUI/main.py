#!/usr/bin/env python

import sys,pyqrcode,png
try:
    from Tkinter import *
except ImportError:
	from tkinter import *
from threading import Thread
from socket import *
from time import *

TCP_PORT = 8000
BUFFER_SIZE = 16  # Normally 1024, but fast response is needed

def serverTCP_Connected():
    info_label_server.configure(text="Connected",fg = "green")

def serverTCP_Disconnected():
    info_label_server.configure(text="Disconnected", fg="red")


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
    serverTCP_Connected()
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
    #INITIALIZE UDP SERVER - PIANO
	udp_server = Thread(target=startUDP, args=(argv[2],))
	udp_server.daemon = False
	udp_server.start()
	sleep(0.5)
    #INITIALIZE TCP SERVER - HOLOLENS
	tcp_server = Thread(target=setupTCP)
	tcp_server.daemon = False
	tcp_server.start()
	sleep(0.5)
    #INITIALIZE RASPBERRY GUI
	gui = Thread(target=init_GUI, args=(argv[1],))
	gui.daemon = False
	gui.start()
    #INITIALIZE DRAW QR CODE

def init_GUI(code):
	global root
	global info_label_server,label_0,label_2
	root = Tk()
	root.title("Server")
	label_0 = Label(root, text="Run the application \n and Scan the QR code")
	label_2 = Label(root, text="Connection status:")
	
	info_label_server = Label(root, text="")
	label_0.grid(row=0,column = 1)
	label_2.grid(row=2,column = 0,sticky =W)
	
	info_label_server.grid(row=2, column=1)
	serverTCP_Disconnected()
	drawQR(code)

if __name__== "__main__":
    main(sys.argv)





