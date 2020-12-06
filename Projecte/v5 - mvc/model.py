from piezas.peon import Peon
from piezas.torre import Torre
from piezas.alfil import Alfil
from piezas.caballo import Caballo
from piezas.king import King
from piezas.queen import Queen
from piezas.pieza import Pieza

class Tablero():
    def __init__(self):
        self.M= [[0 for x in range(8)] for _ in range(8)] #Mesa
        self.jugador = 1 #azul = 1, rojo = 0
        piezasRojas = [Torre(0,0,0),Caballo(0,1,0),Alfil(0,2,0),Queen(0,3,0),King(0,4,0),Alfil(0,5,0),Caballo(0,6,0),Torre(0,7,0)]
        piezasAzules = [Torre(0,0,1),Caballo(0,1,1),Alfil(0,2,1),Queen(0,3,1),King(0,4,1),Alfil(0,5,1),Caballo(0,6,1),Torre(0,7,1)]

        for i in range(len(self.M)):
            self.M[0][i] = piezasRojas[i]

        for i in range(len(self.M[1])):
            self.M[1][i] = Peon(1, i, 0) 
        
        for i in range(5):
            for j in range(8):
                self.M[i + 2][j] = Pieza(" ", "N", i, j)
 
        for i in range(len(self.M[6])):
            self.M[6][i] = Peon(6, i, 1) 
        
        for i in range(len(self.M[7])):
            self.M[7][i] = piezasAzules[i]
    
    def comprobarPartida(self):
        numK = 0
        pos = []
        for i in range(len(self.M)):
            for j in range(len(self.M[i])):
                if self.M[i][j].equipo != "N":
                    if self.M[i][j].tipo == "K":
                        numK += 1
                        pos.append(i)
                        pos.append(j)
        if numK < 2:
            if self.M[pos[0]][pos[1]].equipo == "N":
                self.jugador = 0
                return False
            else:
                self.jugador = 1
                return False
        else:
            return True