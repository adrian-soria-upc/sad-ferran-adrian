def actualizartablero(turno, color):
	if turno==0:
		return "tableroInicio\n"
	elif turno<4:
		return "jugada\n"
	else:#esta mal
		if color=="rojo":
			return "\nganador rojo\n"
		else:
			return "\nganador azul\n"
def myTurn(turno, color):
	if ((turno % 2 != 0) & (color == 'azul')): #truno negras (IMPAR)
		return True
	elif ((turno % 2 == 0) & (color == 'rojo')): #turno blancas (PAR)
		return True
	else:	
		return False	

	
def comandocorrecto(turno, color, line):
	return True	
