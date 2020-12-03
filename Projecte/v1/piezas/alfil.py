from piezas.pieza import Pieza

class Alfil(Pieza):
    
    def __init__(self, fila, col, equipo):
        Pieza.__init__(self, "A", equipo, fila, col)  
    
    def valid_move(self, mesa, pos):
        f = pos[2] - pos[0] #Fila final - Fila inicial
        c = pos[3] - pos[1] #Columna final - Columna inicial
        mpos = True
        if abs(f) == abs(c):
            #Izquierda-Arriba
            if f < 0 and c <0:
                for i in range(abs(f)):
                    if i != 0 and mesa[pos[0] - i][pos[1] - i] != 0:
                        mpos = False
            #Derecha-Arriba
            elif f < 0 and c > 0:
                for i in range(abs(f)):
                    if i!=0 and mesa[pos[0] - i][pos[1] + i] != 0:
                        mpos = False
            #Abajo-Izquierda
            elif f > 0 and c < 0:   
                for i in range(abs(f)):
                    if i != 0 and mesa[pos[0] + i][pos[1] - i] != 0:
                        mpos = False
            #Abajo-Derecha
            elif f > 0 and c > 0:
                for i in range(abs(f)):
                    if i!=0 and mesa[pos[0] + i][pos[1] + i] != 0:
                        mpos = False
        else:
            print("DIAGONALES NO IGUALES")
            mpos = False
        
        return mpos
    
    # def getAmenazaAzul(self, mesa):
    #     amenaza = []
    #     i = 1
    #     #Arriba- Izquierda
    #     while self.fila - i >= 0 and self.col - i >= 0 and mesa[self.fila - i][self.col - i] == 0:
    #         pos = [self.fila - i, self.col - i]
    #         amenaza.append(pos)
    #         i+=1
    #     #Abajo - Izquierda
    #     i = 1
    #     while self.fila + i <= 7 and self.col - i >= 0 and mesa[self.fila + i][self.col - i] == 0:
    #         pos = [self.fila + i, self.col]
    #         amenaza.append(pos)
    #         i+=1
    #     #Arriba - Derecha
    #     i = 1
    #     while self.col + i <= 7 and self.fila - i >= 0 and mesa[self.fila - i][self.col + i] == 0:
    #         pos = [self.fila - i, self.col + i]
    #         amenaza.append(pos)
    #         i+=1
    #     #Abajo - Derecha
    #     i = 1
    #     while self.col + i <= 7 and self.fila + i <= 7 and mesa[self.fila + i][self.col + i] == 0:
    #         pos = [self.fila + i, self.col + i]
    #         amenaza.append(pos)
    #         i+=1
            
    #     return amenaza
    
    def getAmenazaRoja(self, mesa):
        return self.getAmenazaAzul(mesa)
    
    def getPieza(self):
        if self.equipo == "R":
            return "\033[;31m"+ "A" + "\033[;37m"
        else:
            return "\033[;36m"+ "A" + "\033[;37m"


