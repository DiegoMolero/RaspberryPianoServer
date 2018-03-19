import sys,pyqrcode,png

def main(argv):
	if(len(argv) != 2):
		print ('Sintex error, the programs needs 1 argument: qr_show.py <ip>')
		sys.exit(2)
	print("Starting QR Show")
	url = pyqrcode.create(str(argv[1]))
	url.png('qr.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
	url.show()

if __name__== "__main__":
	main(sys.argv)