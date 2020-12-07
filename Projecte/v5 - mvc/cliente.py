import socket, sys, threading
#ejecutar codigo: python3 client.py localhost 1234 usuario

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2])))	
nick = sys.argv[3]

def input():
	out = open(s.fileno(), 'w', 1)
	out.write(f'{nick}\n')
	for line in sys.stdin:
		out.write(line)
	s.shutdown(socket.SHUT_WR)
threading.Thread(target = input).start()

def output():
	inp = open(s.fileno(), 'r')
	for line in inp:
		sys.stdout.write(line)
threading.Thread(target = output).start()
