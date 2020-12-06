from piezas.peon import Peon
from piezas.torre import Torre
from piezas.alfil import Alfil
from piezas.caballo import Caballo
from piezas.king import King
from piezas.queen import Queen

class Tablero():
    def __init__(self):
        self.M= [[0 for x in range(8)] for _ in range(8)] #Mesa
        self.jugador = 1 #azul = 1, rojo = 0

        self.M[0][0] = Torre(0, 0, 0)
        self.M[0][1] = Caballo(0, 1, 0)
        self.M[0][2] = Alfil(0, 2, 0)
        self.M[0][3] = Queen(0, 3, 0)
        self.M[0][4] = King(0, 4, 0)
        self.M[0][5] = Alfil(0, 5, 0)
        self.M[0][6] = Caballo(0, 6, 0)
        self.M[0][7] = Torre(0, 7, 0)

        for i in range(len(self.M[1])):
            self.M[1][i] = Peon(1, i, 0) 
        
        for i in range(len(self.M[6])):
            self.M[6][i] = Peon(1, i, 1)
            
        self.M[7][0] = Torre(7, 0, 1)
        self.M[7][1] = Caballo(7, 1, 1)
        self.M[7][2] = Alfil(7, 2, 1)
        self.M[7][3] = Queen(7, 3, 1)
        self.M[7][4] = King(7, 4, 1)
        self.M[7][5] = Alfil(7, 5, 1)
        self.M[7][6] = Caballo(7, 6, 1)
        self.M[7][7] = Torre(7, 7, 1)
    
    def comprobarPartida(self):
        numK = 0
        pos = []
        for i in range(len(self.M)):
            for j in range(len(self.M[i])):
                if self.M[i][j] != 0:
                    if self.M[i][j].tipo == "K":
                        numK += 1
                        pos.append(i)
                        pos.append(j)
        if numK < 2:
            if self.M[pos[0]][pos[1]].equipo == 0:
                self.jugador = 0
                return False
            else:
                self.jugador = 1
                return False
        else:
            return True

