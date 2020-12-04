import socket, sys, threading
#ejecutar codigo: python3 client.py localhost 1234 usuario color

BLUE = '\033[34m'
RED = '\033[31m'
DEFAULT = '\033[0m'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
nick = sys.argv[3]
color = sys.argv[4]

#while (color!="azul") & (color!="rojo"):
#	print("Color erroneo, escrive azul o rojo: ")
#	color=sys.stdin.readline().rstrip()
s.connect((sys.argv[1], int(sys.argv[2])))	

def input():
	out = open(s.fileno(), 'w', 1)
	out.write(f'{nick}\n')
	out.write(f'{color}\n')
	for line in sys.stdin:
		if color == 'rojo':
			out.write(f"{RED}{nick}>{DEFAULT} {line}") 
		elif color == 'azul':
			out.write(f"{BLUE}{nick}>{DEFAULT} {line}")
	s.shutdown(socket.SHUT_WR)
threading.Thread(target = input).start()

def output():
	inp = open(s.fileno(), 'r')
	for line in inp:
		sys.stdout.write(line)
threading.Thread(target = output).start()

