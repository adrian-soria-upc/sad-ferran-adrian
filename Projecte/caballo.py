from pieza import Pieza

class Caballo(Pieza):
    
    def __init__(self, fila, col, equipo):
        Pieza.__init__(self, "C", equipo, fila, col)  
    
    def move(self):
        return
    
    def getPieza(self):
        if self.equipo == "R":
            return "\033[;31m"+ "C" + "\033[;37m"
        else:
            return "\033[;36m"+ "C" + "\033[;37m"


