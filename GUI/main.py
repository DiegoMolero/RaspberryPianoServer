#!/usr/bin/env python

import sys,pyqrcode,png
from tkinter import *
from time import *

def drawQR(code):
    url = pyqrcode.create(code)
    url.png('qr.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    img = PhotoImage(file="qr.png")
    panel = Label(root, image=img)
    panel.grid(row=0,column=0, sticky=E)
    panel.mainloop()


def main(argv):
    init_GUI()
    drawQR("hi")
    root.mainloop()

def init_GUI():
    global root
    global info_label_server,info_label_piano,label_0
    root = Tk()
    sleep(1)
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

def update_label_serverTCP(msg):
    info_label_server.configure(text = msg)

def update_label_Piano(msg):
    info_label_piano.configure(text = msg)

def update_label_Info(msg):
    label_0.configure(text=msg)

if __name__== "__main__":
    main(sys.argv)





