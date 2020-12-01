from pieza import Pieza

class King(Pieza):
    
    def __init__(self, fila, col, equipo):
        Pieza.__init__(self, "K", equipo, fila, col)  
    
    def valid_move(self, mesa, pos):
        f = pos[2] - pos[0] #Fila final - Fila inicial
        c = pos[3] - pos[1] #Columna final - Columna inicial
        if abs(f) > 1 or abs(c) > 1:
            return False
        else:
            return True
        #Fer que no puguis anar a casella amenaçada    
            
    def getPieza(self):
        if self.equipo == "R":
            return "\033[;31m"+ "K" + "\033[;37m"
        else:
            return "\033[;36m"+ "K" + "\033[;37m"
