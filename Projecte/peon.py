from pieza import Pieza

class Peon(Pieza):
        
    def __init__(self, fila, col, equipo):
        Pieza.__init__(self, "P", equipo, fila, col)        
        
    def valid_move(self, mesa, pos):
        f = pos[2] - pos[0] #Fila final - Fila inicial
        c = pos[3] - pos[1] #Columna final - Columna inicial
        if abs(f) > 1 or abs(c) > 1:
            if pos[0] == 1 or pos[0] == 6:
                if abs(f) == 2:
                    if self.equipo == "A" and mesa[pos[0] - 1][pos[1]] == 0:
                        if pos[3] == pos[1]:
                            return True
                    elif self.equipo == "R" and mesa[pos[0] + 1][pos[1]] == 0:
                        if pos[3] == pos[1]:
                            return True
                    else:
                        return False
            else:
                return False
        elif self.equipo == "R" and f <= 0: #Las rojas solo se pueden mover hacia abajo (filas positivas)
            return False
        elif self.equipo == "A" and f >= 0: #Las azules solo se pueden mover hacia arriba (filas negativas)
            return False
        else:
            if pos[3] == pos[1]:
                return True
            elif mesa[pos[2]][pos[3]] != 0:
                return True  
          
    def getPieza(self):
        if self.equipo == "R":
            return "\033[;31m"+ "P" + "\033[;37m"
        else:
            return "\033[;36m"+ "P" + "\033[;37m"