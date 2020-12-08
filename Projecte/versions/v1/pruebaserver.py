import socket, sys, threading
from tablero import Tablero
#control-z para salir
#ejecutar codigo: python3 server.py 1234

def client(s):
	sin=s.makefile('r')
	nick=sin.readline().rstrip()
	color = sin.readline().rstrip()
	global turno
	turno = 0
	with lock:
		users[nick] = s
		s.send(("Bienvenidos...normas...teclas...azul representa blancas, rojo representa negras. El color de tus piezas es: " + color + "\n").encode("UTF-8"))
		s.send(tablero.actualizartablero(turno, color).encode("UTF-8"))
	for line in sin:
		if tablero.myTurn(turno, color):
			with lock:
				for u in users.values():
					if u != s: 
						if tablero.comandocorrecto(turno, color, line):
							u.send(line.encode("UTF-8"))
							turno=turno+1
							u.send(tablero.actualizartablero(turno, color).encode("UTF-8"))
						else: s.send("Comanda erronea\n".encode("UTF-8"))
							
	s.close()
	with lock:
		del users[nick]

lock = threading.Lock()
users = {}
tablero = Tablero()

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('', int(sys.argv[1])))
serv.listen()

while True:
	s, _ = serv.accept()
	threading.Thread(target=client, args = (s,)).start()
