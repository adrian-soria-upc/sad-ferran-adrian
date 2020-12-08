import socket, sys, threading
import view, controller
from model import Tablero
#ejecutar codigo: python3 server.py 1234

def client(s):
	sin = s.makefile('r')
	nick = sin.readline().rstrip()
	inpS = open(s.fileno(), 'w', 1)
	if len(users) == 0: 
		p = 1 
		color = "azul"
	else:
		p = 0
		color = "rojo"
	with lock:
		users[p] = {}
		users[p][p] = s
		inpS.write(view.dibujarInicio(color,tablero, nick, p))
	for line in sin:
		if tablero.turno == p and tablero.comprobarPartida() and len(users) == 2:
			with lock:
				u = users[abs(p-1)][abs(p-1)] #Socket enemigo
				inpU = open(u.fileno(), 'w', 1)
				if controller.comandoCorrecto(p, line, tablero):
					inpU.write(view.dibujarComanda(p, nick, line))
					inpU.write(view.dibujarMesa(abs(p-1), tablero))
					inpS.write(view.dibujarMesa(p, tablero))
				else: 
					inpS.write("Comanda erronea\n")
	s.close()
	with lock:
		del users[p]

lock = threading.Lock()
users = {} #users = {azul:{nick1:socket1},rojo:{nick2:socket2}}
tablero = Tablero()

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('', int(sys.argv[1])))
serv.listen()

while True:
	s, _ = serv.accept()
	threading.Thread(target=client, args = (s,)).start()
