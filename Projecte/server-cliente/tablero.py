def actualizartablero(turno, color):
	if turno==0:
		return "tableroInicio\n"
	elif turno<4:
		return "jugada\n"
	else:#esta mal
		if color=="azul":
			return "\nganador rojo\n"
		else:
			return "\nganador azul\n"
def myTurn(turno, color):
	if ((turno % 2 != 0) & (color == 'rojo')): #truno blancas (IMPAR)
		return True
	elif ((turno % 2 == 0) & (color == 'azul')): #turno negras (PAR)
		return True
	else:	
		return False	

	
def comandocorrecto(turno, color, line):
	return True	
