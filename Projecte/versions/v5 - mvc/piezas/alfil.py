from piezas.pieza import Pieza

class Alfil(Pieza):
    
    def __init__(self, equipo):
        Pieza.__init__(self, "A", equipo)  
    
    def valid_move(self, mesa, pos):
        f = pos[2] - pos[0] #Fila final - Fila inicial
        c = pos[3] - pos[1] #Columna final - Columna inicial
        mpos = True
        if abs(f) == abs(c):
            #Izquierda-Arriba
            if f < 0 and c < 0:
                for i in range(abs(f)):
                    if i != 0 and mesa[pos[0] - i][pos[1] - i].equipo != "N":
                        mpos = False
            #Derecha-Arriba
            elif f < 0 and c > 0:
                for i in range(abs(f)):
                    if i!=0 and mesa[pos[0] - i][pos[1] + i].equipo != "N":
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
        else:
            mpos = False 
        return mpos