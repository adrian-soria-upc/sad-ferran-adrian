from piezas.pieza import Pieza
from piezas.alfil import Alfil
from piezas.torre import Torre

class Queen(Pieza):
    
    def __init__(self, fila, col, equipo):
        Pieza.__init__(self, "Q", equipo, fila, col)  

    def valid_move(self, mesa, pos):
        alfil = Alfil(self.fila, self.col, self.equipo)
        torre = Torre(self.fila, self.col, self.equipo)
        if alfil.valid_move(mesa, pos) or torre.valid_move(mesa, pos):
            return True
        else:
            return False