from pieza import Pieza

class King(Pieza):
    
    def __init__(self, fila, col, equipo):
        Pieza.__init__(self, "K", equipo, fila, col)  
    
    def move(self):
        return
    
    def getPieza(self):
        if self.equipo == "R":
            return "\033[;31m"+ "K" + "\033[;37m"
        else:
            return "\033[;36m"+ "K" + "\033[;37m"
