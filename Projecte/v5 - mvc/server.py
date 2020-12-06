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
		s.send(("Bienvenido " + nick + ".\nEn este juego de ajedrez, las piezas azules coresponden a las blancas y las rojas a las negras.\nPara hacer un movimiento debes introducir por ejemplo: 7d6d. Donde '7d' corresponde a las coordenadas de origen de la pieza, y 6d las coordenadas de destino. Si introduces ff te rendiras. El color de tus piezas es: ").encode("UTF-8"))
		s.send(color.encode("UTF-8")) #Juntar!!!!!!!!!
		s.send(view.dibujarMesa(p, tablero).encode("UTF-8"))
	for line in sin:
		if tablero.turno == p and tablero.comprobarPartida() and len(users) == 2:
			with lock:
				u = users[abs(p-1)][abs(p-1)] #Socket enemigo
				if controller.comandoCorrecto(p, line, tablero):
					if color == "azul":
						u.send(f"{BLUE}{nick}>{DEFAULT} {line}".encode("UTF-8"))
					else:
						u.send(f"{RED}{nick}>{DEFAULT} {line}".encode("UTF-8"))
					u.send(view.dibujarMesa(abs(p-1), tablero).encode("UTF-8"))
					s.send(view.dibujarMesa(p, tablero).encode("UTF-8"))
					if tablero.comprobarPartida() == False:
						if tablero.turno == 0:
							u.send(("EL GANADOR ES EL JUGADOR ROJO\n").encode("UTF-8"))
							s.send(("EL GANADOR ES EL JUGADOR ROJO\n").encode("UTF-8"))
						else:
							u.send(("EL GANADOR ES EL JUGADOR AZUL\n").encode("UTF-8"))
							s.send(("EL GANADOR ES EL JUGADOR AZUL\n").encode("UTF-8"))
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
