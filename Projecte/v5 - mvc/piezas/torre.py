from piezas.pieza import Pieza

class Torre(Pieza):
    def __init__(self, fila, col, equipo):
        Pieza.__init__(self, "T", equipo, fila, col)  
        
    def valid_move(self, mesa, pos):
        f = pos[2] - pos[0] #Fila final - Fila inicial
        c = pos[3] - pos[1] #Columna final - Columna inicial
        mpos = True
        #Arriba
        if c == 0 and f < 0:
            for i in range(abs(f)):
                if i != 0 and mesa[pos[0] - i][pos[1]] != 0:
                    mpos = False
        #Abajo
        elif c == 0 and f > 0:
            for i in range(abs(f)):
                if i != 0 and mesa[pos[0] + i][pos[1]] != 0:
                    mpos = False
        #Izquierda
        elif c < 0 and f == 0:
            for i in range(abs(c)):
                if  i != 0 and mesa[pos[0]][pos[1] - i] != 0:
                    mpos = False
        #Derecha
        elif c > 0 and f == 0:
            for i in range(abs(c)):
                if i != 0 and mesa[pos[0]][pos[1] + i] != 0:
                    mpos = False
        return mpos