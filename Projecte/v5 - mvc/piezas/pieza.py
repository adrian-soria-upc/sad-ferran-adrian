class Pieza:
    def __init__(self, tipo, equipo):
        self.tipo = tipo
        self.equipo = equipo
        self.enroque = False
    
    def getPieza(self):
        if self.equipo == 0:
            return "\033[;31m"+ self.tipo + "\033[;37m"
        else:
            return "\033[;36m"+ self.tipo + "\033[;37m"  