from piezas.pieza import Pieza

class Torre(Pieza):
    def __init__(self, fila, col, equipo):
        Pieza.__init__(self, "T", equipo, fila, col)  
        
    def valid_move(self, mesa, pos):
        f = pos[2] - pos[0] #Fila final - Fila inicial
        c = pos[3] - pos[1] #Columna final - Columna inicial
        mpos = True
        #Arriba
        if c == 0 and f < 0:
            for i in range(abs(f)):
                if i < 0 and mesa[pos[0] - i][pos[1]] != 0:
                    mpos = False
        #Abajo
        elif c == 0 and f > 0:
            for i in range(abs(f)):
                if i < 0 and mesa[pos[0] + i][pos[1]] != 0:
                    mpos = False
        #Izquierda
        elif c < 0 and f == 0:
            for i in range(abs(c)):
                if  i < 0 and mesa[pos[0]][pos[1] - i] != 0:
                    mpos = False
        #Derecha
        elif c > 0 and f == 0:
            for i in range(abs(c)):
                if i < 0 and mesa[pos[0]][pos[1] + i] != 0:
                    mpos = False
        return mpos
    
    # def getAmenazaAzul(self, mesa):
    #     amenaza = []
    #     i = 1
    #     #Arriba
    #     while self.fila - i >= 0 and mesa[self.fila - i][self.col] == 0:
    #         pos = [self.fila - i, self.col]
    #         amenaza.append(pos)
    #         i+=1
    #     #Abajo
    #     i = 1
    #     while self.fila + i <= 7 and mesa[self.fila + i][self.col] == 0:
    #         pos = [self.fila + i, self.col]
    #         amenaza.append(pos)
    #         i+=1
    #     #Izquierda
    #     i = 1
    #     while self.col - i >= 0 and mesa[self.fila][self.col - i] == 0:
    #         pos = [self.fila, self.col - i]
    #         amenaza.append(pos)
    #         i+=1
    #     #Derecha
    #     i = 1
    #     while self.col + i <= 7 and mesa[self.fila][self.col + i] == 0:
    #         pos = [self.fila, self.col + i]
    #         amenaza.append(pos)
    #         i+=1
            
    #     return amenaza
    
    # def getAmenazaRoja(self, mesa):
    #     return self.getAmenazaAzul(mesa)
    
    def getPieza(self):
        if self.equipo == "R":
            return "\033[;31m"+ "T" + "\033[;37m"
        else:
            return "\033[;36m"+ "T" + "\033[;37m"