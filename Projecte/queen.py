from pieza import Pieza

class Queen(Pieza):
    
    def __init__(self, fila, col, equipo):
        Pieza.__init__(self, "Q", equipo, fila, col)  
        
    def valid_move(self, mesa, pos):
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
                    if i != 0 and mesa[pos[0] + i][pos[1] - i] != 0:
                        mpos = False
            #Abajo-Derecha
            elif f > 0 and c > 0:
                for i in range(abs(f)):
                    if i!=0 and mesa[pos[0] + i][pos[1] + i] != 0:
                        mpos = False
        #Arriba
        if c == 0 and f < 0:
            for i in range(abs(f)):
                if i < 0 and mesa[pos[0] - i][pos[1]] != 0:
                    mpos = False
        #Abajo
        elif c == 0 and f > 0:
            for i in range(abs(f)):
                if i < 0 and mesa[pos[0] + i][pos[1]] != 0:
                    mpos = False
        #Izquierda
        elif c < 0 and f == 0:
            for i in range(abs(c)):
                if  i < 0 and mesa[pos[0]][pos[1] - i] != 0:
                    mpos = False
        #Derecha
        elif c > 0 and f == 0:
            for i in range(abs(c)):
                if i < 0 and mesa[pos[0]][pos[1] + i] != 0:
                    mpos = False
        return mpos
    
    def getPieza(self):
        if self.equipo == "R":
            return "\033[;31m"+ "Q" + "\033[;37m"
        else:
            return "\033[;36m"+ "Q" + "\033[;37m"
