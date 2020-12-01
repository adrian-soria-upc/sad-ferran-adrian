from piezas.peon import Peon
from piezas.torre import Torre
from piezas.alfil import Alfil
from piezas.caballo import Caballo
from piezas.king import King
from piezas.queen import Queen

def crearMatriz(color):
        M= [[0 for x in range(8)] for _ in range(8)] #Mesa
        jugando = True

        M[0][0] = Torre(0, 0, "R")
        M[0][1] = Caballo(0, 1, "R")
        M[0][2] = Alfil(0, 2, "R")
        M[0][3] = Queen(0, 3, "R")
        M[0][4] = King(0, 4, "R")
        M[0][5] = Alfil(0, 5, "R")
        M[0][6] = Caballo(0, 6, "R")
        M[0][7] = Torre(0, 7, "R")

        M[1][0] = Peon(1, 0, "R")
        M[1][1] = Peon(1, 1, "R")
        M[1][2] = Peon(1, 2, "R")
        M[1][3] = Peon(1, 3, "R")
        M[1][4] = Peon(1, 4, "R")
        M[1][5] = Peon(1, 5, "R")
        M[1][6] = Peon(1, 6, "R")
        M[1][7] = Peon(1, 7, "R")
        
        M[6][0] = Peon(6, 0, "A")
        M[6][1] = Peon(6, 1, "A")
        M[6][2] = Peon(6, 2, "A")
        M[6][3] = Peon(6, 3, "A")
        M[6][4] = Peon(6, 4, "A")
        M[6][5] = Peon(6, 5, "A")
        M[6][6] = Peon(6, 6, "A")
        M[6][7] = Peon(6, 7, "A")

        M[7][0] = Torre(7, 0, "A")
        M[7][1] = Caballo(7, 1, "A")
        M[7][2] = Alfil(7, 2, "A")
        M[7][3] = Queen(7, 3, "A")
        M[7][4] = King(7, 4, "A")
        M[7][5] = Alfil(7, 5, "A")
        M[7][6] = Caballo(7, 6, "A")
        M[7][7] = Torre(7, 7, "A")
        
        return dibujarMesaString(M, color)

def dibujarMesaString(matriz, jugador):
        mesa = ""
        if jugador == "azul":
            mesa += "\033[;36m"+"                 TURNO JUGADOR AZUL" + "\n"
        else:
            mesa += "\033[;31m"+"                 TURNO JUGADOR ROJO" + "\n"
        mesa += "\033[;37m" + "       A     B     C     D     E     F     G     H" + "\n" + "   -------------------------------------------------" + "\n"
        for i in range(len(matriz)):
            mesa += str(i + 1) + "| " + '[| '
            for j in range(len(matriz[i])):
                if matriz[i][j] == 0:
                    mesa += "    " + "| "
                else:
                    mesa += " " + matriz[i][j].getPieza() + "  | " 
            mesa += ']' + "\n" + "   -------------------------------------------------" + "\n"
        mesa += "       A     B     C     D     E     F     G     H" + "\n"
        return mesa
        
def actualizartablero(turno, color):
	if turno==0:
		return crearMatriz(color)
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
