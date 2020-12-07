BLUE = '\033[34m'
RED = '\033[31m'
DEFAULT = '\033[0m'
class Pieza:
    def __init__(self, tipo, equipo):
        self.tipo = tipo
        self.equipo = equipo
        self.enroque = False
    
    def getPieza(self):
        if self.equipo == 0:
            return RED+ self.tipo + DEFAULT
        else:
            return BLUE+ self.tipo + DEFAULT