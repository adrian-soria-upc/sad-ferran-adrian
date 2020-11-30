from pieza import Pieza

class Torre(Pieza):
    def __init__(self, fila, col, equipo):
        Pieza.__init__(self, "T", equipo, fila, col)  
        
    def move(self):
        return
    
    def getPieza(self):
        if self.equipo == "R":
            return "\033[;31m"+ "T" + "\033[;37m"
        else:
            return "\033[;36m"+ "T" + "\033[;37m"