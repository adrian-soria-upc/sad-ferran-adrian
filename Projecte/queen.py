from pieza import Pieza

class Queen(Pieza):
    
    def __init__(self, fila, col, equipo):
        Pieza.__init__(self, "Q", equipo, fila, col)  
        
    def move(self):
        return

    def getPieza(self):
        if self.equipo == "R":
            return "\033[;31m"+ "Q" + "\033[;37m"
        else:
            return "\033[;36m"+ "Q" + "\033[;37m"
