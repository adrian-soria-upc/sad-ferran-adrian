import socket, sys, threading
from tablero import Tablero
#control-z para salir
#ejecutar codigo: python3 server.py 1234
#FALTA: victoria-derrota, model-view-controler(separarcontrol tablero , interfaztablero,) clase serverclient?

def client(s):
	sin=s.makefile('r')
	nick=sin.readline().rstrip()
	color = sin.readline().rstrip()
	with lock:
		users[nick] = s
		s.send(("Bienvenido " + nick + ".\nEn este juego de ajedrez, las piezas azules coresponden a las blancas y las rojas a las negras. Para hacer un movimiento debes introducir por ejemplo: 7d6d Donde '7d' corresponde a las coordenadas de origen de la pieza, y 6d las coordenadas de destino. El color de tus piezas es: " + color + "\n¡SUERTE!\n").encode("UTF-8"))
		s.send(tablero.dibujarMesaString(tablero.M).encode("UTF-8"))
	for line in sin:
		if ((tablero.jugador == color) & (tablero.comprobarPartida())):
			with lock:
				for u in users.values():
					if u != s: 
						if tablero.comandocorrecto(color, line):
							u.send(line.encode("UTF-8"))
							u.send(tablero.dibujarMesaString(tablero.M).encode("UTF-8"))
							s.send(tablero.dibujarMesaString(tablero.M).encode("UTF-8"))
						else: s.send("Comanda erronea\n".encode("UTF-8"))
		elif tablero.comprobarPartida() == False:
			s.send(("EL GANADOR ES EL JUGADOR " + tablero.jugador.upper() + "\n").encode("UTF-8"))			
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
