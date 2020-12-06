from piezas.pieza import Pieza

class Caballo(Pieza):
    
    def __init__(self, equipo):
        Pieza.__init__(self, "C", equipo)  
    
    def valid_move(self, mesa, pos):
        f = pos[2] - pos[0] #Fila final - Fila inicial
        c = pos[3] - pos[1] #Columna final - Columna inicial
        if abs(f) == 2 and abs(c) == 1:
            return True
        elif abs(f) == 1 and abs(c) == 2:
            return True
        else:
            return False