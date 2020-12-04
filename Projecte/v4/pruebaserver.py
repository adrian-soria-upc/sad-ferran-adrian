import socket, sys, threading
from tablero import Tablero
#control-z para salir
#ejecutar codigo: python3 server.py 1234
#FALTA: victoria-derrota, model-view-controler(separarcontrol tablero , interfaztablero,) clase serverclient?

def client(s):
	sin = s.makefile('r')
	nick = sin.readline().rstrip()
	color = sin.readline().rstrip()
	with lock:
		#while (color!="azul") & (color!="rojo"):
		#	s.send("Color erroneo, escrive azul o rojo: ".encode("UTF-8"))
		#	color = sin.readline().rstrip()
		if color=="azul": p=1
		else: p=0
		#while users.get(p, {}).get(p)!=None:
		#	while (color!="azul") & (color!="rojo"):
		#		s.send("Color erroneo, escrive azul o rojo: ".encode("UTF-8"))
		#		color = sin.readline().rstrip()
		#	if color=="azul": p=1
		#	else: p=0
		users[p]={}
		users[p][p] = s
		s.send(("Bienvenido " + nick + ".\nEn este juego de ajedrez, las piezas azules coresponden a las blancas y las rojas a las negras. Para hacer un movimiento debes introducir por ejemplo: 7d6d Donde '7d' corresponde a las coordenadas de origen de la pieza, y 6d las coordenadas de destino. Si introduces ff te rendiras. El color de tus piezas es: " + color + "\n¡SUERTE!\n").encode("UTF-8"))
		s.send(tablero.dibujarMesa(tablero.M, p).encode("UTF-8"))
	for line in sin:
		if ((tablero.jugador == p) & (tablero.comprobarPartida())):
			with lock:
				u=users[abs(p-1)][abs(p-1)]
				if tablero.comandocorrecto(p, line):
					u.send(line.encode("UTF-8"))
					u.send(tablero.dibujarMesa(tablero.M, abs(p-1)).encode("UTF-8"))
					s.send(tablero.dibujarMesa(tablero.M, p).encode("UTF-8"))
					if tablero.comprobarPartida() == False:
						u.send(("EL GANADOR ES EL JUGADOR " + color.upper() + "\n").encode("UTF-8"))
						s.send(("EL GANADOR ES EL JUGADOR " + color.upper() + "\n").encode("UTF-8"))
				else: s.send("Comanda erronea\n".encode("UTF-8"))		
	s.close()
	with lock:
		del users[p]

lock = threading.Lock()
users = {}
#user = {azul:{nick1:socket1}
#        rojo:{nick2:socket2}}
tablero = Tablero()

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('', int(sys.argv[1])))
serv.listen()

while len(users)<1: 
	s, _ = serv.accept()
	threading.Thread(target=client, args = (s,)).start()
