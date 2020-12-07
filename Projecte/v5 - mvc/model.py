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
        self.turno = 1 #azul = 1, rojo = 0
        piezasRojas = [Torre(0),Caballo(0),Alfil(0),Queen(0),King(0),Alfil(0),Caballo(0),Torre(0)]
        piezasAzules = [Torre(1),Caballo(1),Alfil(1),Queen(1),King(1),Alfil(1),Caballo(1),Torre(1)]

        for i in range(len(self.M)):
            for j in range(5):
                self.M[j + 2][i] = Pieza(" ", "N")
            self.M[0][i] = piezasRojas[i]
            self.M[1][i] = Peon(0)
            self.M[6][i] = Peon(1)
            self.M[7][i] = piezasAzules[i]
    
    def comprobarPartida(self):
        numK = 0
        pos = []
        for i in range(len(self.M)):
            for j in range(len(self.M[i])):
                if self.M[i][j].tipo == "K":
                    numK += 1
                    pos.append(i)
                    pos.append(j)
        if numK < 2: return False
        else: return True
