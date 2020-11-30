from pieza import Pieza

class Alfil(Pieza):
    
    def __init__(self, fila, col, equipo):
        Pieza.__init__(self, "A", equipo, fila, col)  
    
    def move(self):
        return
    
    def getPieza(self):
        if self.equipo == "R":
            return "\033[;31m"+ "A" + "\033[;37m"
        else:
            return "\033[;36m"+ "A" + "\033[;37m"


