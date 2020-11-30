from pieza import Pieza

class Peon(Pieza):
        
    def __init__(self, fila, col, equipo):
        Pieza.__init__(self, "P", equipo, fila, col)        
        
    def move(self, mesa, pos):
        f = abs(pos[0] - pos[2])
        c = abs(pos[1] - pos[3])
        if f > 1 or c > 1:
            return -1
        else:
            if pos[3] == pos[1]:
                if pos[0] < pos[2]:
                    mesa[pos[2]][pos[3]] = mesa[pos[0]][pos[1]]
                    mesa[pos[0]][pos[1]] = 0
                else:
                    mesa[pos[2]][pos[3]] = mesa[pos[0]][pos[1]]
                    mesa[pos[0]][pos[1]] = 0 
            else:
                if mesa[pos[2]][pos[3]] != 0:
                    if pos[0] < pos[2]:
                        mesa[pos[2]][pos[3]] = mesa[pos[0]][pos[1]]
                        mesa[pos[0]][pos[1]] = 0
                    else:
                        mesa[pos[2]][pos[3]] = mesa[pos[0]][pos[1]]
                        mesa[pos[0]][pos[1]] = 0    
        return mesa
    
    def getPieza(self):
        if self.equipo == "R":
            return "\033[;31m"+ "P" + "\033[;37m"
        else:
            return "\033[;36m"+ "P" + "\033[;37m"