
class Pieza:
    def __init__(self, tipo, equipo, fila, col):
        self.tipo = tipo
        self.equipo = equipo
        self.fila = fila
        self.col = col
        self.move_list = []
        	
    def move(self, pos):
        self.fila = pos[0]
        self.col = pos[1]
        
    def getPieza(self):
        if self.equipo == "R":
            return "\033[;31m"+ self.tipo + "\033[;37m"
        else:
            return "\033[;36m"+ self.tipo + "\033[;37m"


        