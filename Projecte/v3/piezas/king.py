from piezas.pieza import Pieza

class King(Pieza):
    
    def __init__(self, fila, col, equipo):
        Pieza.__init__(self, "K", equipo, fila, col)  
    
    def valid_move(self, mesa, pos):
        f = pos[2] - pos[0] #Fila final - Fila inicial
        c = pos[3] - pos[1] #Columna final - Columna inicial
        mpos = True
        if abs(f) > 1 or abs(c) > 1:
            mpos = False
        else:
            mpos = True
        
        return mpos
        #Fer que no puguis anar a casella amenaçada    
            
    # def getAmenazaAzul(self, mesa):
    #     amenaza = []
    #     if self.fila == 0:
    #         if self.col == 0:
    #             pos = [self.fila + 1, self.col]
    #             amenaza.append(pos)
    #             pos = [self.fila, self.col + 1]
    #             amenaza.append(pos)
    #             pos = [self.fila + 1, self.col + 1]
    #             amenaza.append(pos)
    #         elif self.col == 7:
    #             pos = [self.fila + 1, self.col]
    #             amenaza.append(pos)
    #             pos = [self.fila, self.col - 1]
    #             amenaza.append(pos)
    #             pos = [self.fila - 1, self.col - 1]
    #             amenaza.append(pos)
    #         else:
    #             pos = [self.fila + 1, self.col]
    #             amenaza.append(pos)
    #             pos = [self.fila, self.col - 1]
    #             amenaza.append(pos)
    #             pos = [self.fila, self.col + 1]
    #             amenaza.append(pos)
    #             pos = [self.fila + 1, self.col + 1]
    #             pos = [self.fila, self.col - 1]
    #             amenaza.append(pos)
    #             pos = [self.fila - 1, self.col - 1]
    #             amenaza.append(pos)
    #     elif self.fila == 7:
    #         if self.col == 0:
    #             pos = [self.fila - 1, self.col]
    #             amenaza.append(pos)
    #             pos = [self.fila, self.col + 1]
    #             amenaza.append(pos)
    #             pos = [self.fila - 1, self.col + 1]
    #             amenaza.append(pos)
    #         elif self.col == 7:
    #             pos = [self.fila - 1, self.col]
    #             amenaza.append(pos)
    #             pos = [self.fila, self.col - 1]
    #             amenaza.append(pos)
    #             pos = [self.fila - 1, self.col - 1]
    #             amenaza.append(pos)
    #         else:
    #             pos = [self.fila - 1, self.col]
    #             amenaza.append(pos)
    #             pos = [self.fila, self.col - 1]
    #             amenaza.append(pos)
    #             pos = [self.fila, self.col + 1]
    #             amenaza.append(pos)
    #             pos = [self.fila - 1, self.col + 1]
    #             amenaza.append(pos)
    #             pos = [self.fila - 1, self.col - 1]
    #             amenaza.append(pos)
    #     elif self.col == 0:
    #         pos = [self.fila + 1, self.col]
    #         amenaza.append(pos)
    #         pos = [self.fila, self.col - 1]
    #         amenaza.append(pos)
    #         pos = [self.fila, self.col + 1]
    #         amenaza.append(pos)
    #         pos = [self.fila + 1, self.col + 1]
    #         amenaza.append(pos)
    #         pos = [self.fila + 1, self.col - 1]
    #         amenaza.append(pos)
    #     elif self.col == 7:
    #         pos = [self.fila + 1, self.col]
    #         amenaza.append(pos)
    #         pos = [self.fila, self.col - 1]
    #         amenaza.append(pos)
    #         pos = [self.fila - 1, self.col]
    #         amenaza.append(pos)
    #         pos = [self.fila - 1, self.col - 1]
    #         amenaza.append(pos)
    #         pos = [self.fila + 1, self.col - 1]
    #         amenaza.append(pos)
    #     else:
    #         pos = [self.fila + 1, self.col]
    #         amenaza.append(pos)
    #         pos = [self.fila +1, self.col - 1]
    #         amenaza.append(pos)
    #         pos = [self.fila, self.col - 1]
    #         amenaza.append(pos)
    #         pos = [self.fila - 1, self.col - 1]
    #         amenaza.append(pos)
    #         pos = [self.fila - 1, self.col]
    #         amenaza.append(pos)
    #         pos = [self.fila - 1, self.col + 1]
    #         amenaza.append(pos)
    #         pos = [self.fila, self.col + 1]
    #         amenaza.append(pos)
    #         pos = [self.fila + 1, self.col + 1]
    #         amenaza.append(pos)
    #     return amenaza
    
    # def getAmenazaRoja(self, mesa):
    #     return self.getAmenazaAzul(mesa)
    
    def getPieza(self):
        if self.equipo == "R":
            return "\033[;31m"+ "K" + "\033[;37m"
        else:
            return "\033[;36m"+ "K" + "\033[;37m"
