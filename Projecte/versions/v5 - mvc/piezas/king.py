from piezas.pieza import Pieza

class King(Pieza):
    
    def __init__(self, equipo):
        Pieza.__init__(self, "K", equipo)  
    
    def valid_move(self, mesa, pos):
        f = pos[2] - pos[0] #Fila final - Fila inicial #0
        c = pos[3] - pos[1] #Columna final - Columna inicial #2
        if abs(f) > 1 or abs(c) > 1:
            #Enroque
            if (pos[0] == 0 or pos[0] == 7) and pos[1] == 4:
                if f == 0:
                    if c == -2:
                        if mesa[pos[0]][pos[1] - 1].equipo == "N" and  mesa[pos[0]][pos[1] - 2].equipo == "N" and mesa[pos[0]][pos[1] - 3].equipo == "N":
                            if mesa[pos[0]][pos[1] - 4].tipo == "T" and mesa[pos[0]][pos[1] - 4].equipo == self.equipo:
                                self.enroque = True
                                return True
                    elif c == 2:
                        if mesa[pos[0]][pos[1] + 1].equipo == "N" and  mesa[pos[0]][pos[1] + 2].equipo == "N":
                            if mesa[pos[0]][pos[1] + 3].tipo == "T" and mesa[pos[0]][pos[1] + 3].equipo == self.equipo:
                                self.enroque = True
                                return True
                    else:
                        self.enroque = False
                        return False
            else:
                self.enroque = False
                return False
        else:
            self.enroque = False
            return True        
