from piezas.pieza import Pieza
#POSSIBLES CANVIS
class Peon(Pieza):
        
    def __init__(self, equipo):
        Pieza.__init__(self, "P", equipo)        
        
    def valid_move(self, mesa, pos):
        f = pos[2] - pos[0] #Fila final - Fila inicial
        c = pos[3] - pos[1] #Columna final - Columna inicial
        mpos = True
        if self.equipo == 0 and f <= 0: #Las rojas solo se pueden mover hacia abajo (filas positivas)
            return False
        elif self.equipo == 1 and f >= 0: #Las azules solo se pueden mover hacia arriba (filas negativas)
            return False
        elif abs(f) > 1 or abs(c) > 1:
            if pos[0] == 1 or pos[0] == 6:
                if abs(f) == 2:
                    if self.equipo == 1 and mesa[pos[0] - 1][pos[1]].equipo == "N":#Mirar filera seguent
                        if pos[3] == pos[1]:
                            mpos = True      
                    elif self.equipo == 0 and mesa[pos[0] + 1][pos[1]].equipo == "N":#Mirar filera seguent
                        if pos[3] == pos[1]:
                            mpos = True          
                    else:
                        mpos = False      
            else:
                mpos = False
        else:
            if pos[3] == pos[1]:
                mpos = True
            elif mesa[pos[2]][pos[3]].equipo == "N":
                mpos = False
        return mpos   
