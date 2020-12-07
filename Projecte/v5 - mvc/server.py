import socket, sys, threading
import view, controller
from model import Tablero
#ejecutar codigo: python3 server.py 1234

BLUE = '\033[34m'
RED = '\033[31m'
DEFAULT = '\033[0m'

def client(s):
	sin = s.makefile('r')
	nick = sin.readline().rstrip()
	if len(users) == 0: #Optimitzar
		p = 1 #Color del client
		color = "azul"
	else:
		p = 0
		color = "rojo"
	with lock:
		users[p] = {}
		users[p][p] = s
		s.send(view.dibujarInicio(color,tablero, nick, p).encode("UTF-8"))
	for line in sin:
		if tablero.turno == p and tablero.comprobarPartida() and len(users) == 2:
			with lock:
				u = users[abs(p-1)][abs(p-1)] #Socket enemigo
				if controller.comandoCorrecto(p, line, tablero):
					u.send(view.dibujarComanda(color, nick, line).encode("UTF-8"))
					u.send(view.dibujarMesa(abs(p-1), tablero).encode("UTF-8"))
					s.send(view.dibujarMesa(p, tablero).encode("UTF-8"))
					if tablero.comprobarPartida() == False: #Entra peró el client no imprimeix, no peta
						u.send(view.finPartida(tablero.turno).encode("UTF-8"))
						s.send(view.finPartida(tablero.turno).encode("UTF-8"))
				else: 
					s.send("Comanda erronea\n".encode("UTF-8"))		
	s.close()
	with lock:
		del users[p]

lock = threading.Lock()
users = {} #users = {azul:{nick1:socket1},rojo:{nick2:socket2}}
tablero = Tablero()

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('', int(sys.argv[1])))
serv.listen(2)

while True:
	s, _ = serv.accept()
	threading.Thread(target=client, args = (s,)).start()
