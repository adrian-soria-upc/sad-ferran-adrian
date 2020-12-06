from piezas.pieza import Pieza
from piezas.alfil import Alfil
from piezas.torre import Torre

class Queen(Pieza):
    
    def __init__(self, fila, col, equipo):
        Pieza.__init__(self, "Q", equipo, fila, col)  

    def valid_move(self, mesa, pos):
        alfil = Alfil(self.fila, self.col, self.equipo)
        torre = Torre(self.fila, self.col, self.equipo)
        if alfil.valid_move(mesa, pos) or torre.valid_move(mesa, pos):
            return True
        else:
            return False

    def valid_move2(self, mesa, pos):
        f = pos[2] - pos[0] #Fila final - Fila inicial
        c = pos[3] - pos[1] #Columna final - Columna inicial
        mpos = True
        #Diagonales
        if abs(f) == abs(c):
            #Izquierda-Arriba
            if f < 0 and c <0:
                for i in range(abs(f)):
                    if i != 0 and mesa[pos[0] - i][pos[1] - i] != 0:
                        mpos = False
            #Derecha-Arriba
            elif f < 0 and c > 0:
                for i in range(abs(f)):
                    if i!=0 and mesa[pos[0] - i][pos[1] + i] != 0:
                        mpos = False
            #Abajo-Izquierda
            elif f > 0 and c < 0:   
                for i in range(abs(f)):
                    if i != 0 and mesa[pos[0] + i][pos[1] - i].equipo != "N":
                        mpos = False
            #Abajo-Derecha
            elif f > 0 and c > 0:
                for i in range(abs(f)):
                    if i!=0 and mesa[pos[0] + i][pos[1] + i].equipo != "N":
                        mpos = False
        #Arriba
        elif c == 0 and f < 0:
            for i in range(abs(f)):
                if i != 0 and mesa[pos[0] - i][pos[1]].equipo != "N":
                    mpos = False
        #Abajo
        elif c == 0 and f > 0:
            for i in range(abs(f)):
                if i != 0 and mesa[pos[0] + i][pos[1]].equipo != "N":
                    mpos = False
        #Izquierda
        elif c < 0 and f == 0:
            for i in range(abs(c)):
                if  i != 0 and mesa[pos[0]][pos[1] - i].equipo != "N":
                    mpos = False
        #Derecha
        elif c > 0 and f == 0:
            for i in range(abs(c)):
                if i != 0 and mesa[pos[0]][pos[1] + i].equipo != "N":
                    mpos = False
        else: 
            mpos = False
        return mpos