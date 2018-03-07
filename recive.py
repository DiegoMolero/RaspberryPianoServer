#!/usr/bin/env python
# To test it with netcat, start the script and execute:
# 
#    echo "Hello, cat." | ncat.exe 127.0.0.1 12345
#
import sys,socket

# /-- network ---
def incoming(host, port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  sock.bind((host, port))
  sock.listen(0)   # do not queue connections
  request, addr = sock.accept()
  return request.makefile('r', 0)

def main(argv):
    if(len(argv) != 3):
        print ('Sintex error: test.py <host> <port>')
        sys.exit(2)
    host = str(argv[1])
    port = int(argv[2])
    for line in incoming(host, port):
        print (line)
        
if __name__== "__main__":
    main(sys.argv)