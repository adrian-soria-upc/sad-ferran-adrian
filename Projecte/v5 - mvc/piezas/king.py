from piezas.pieza import Pieza

class King(Pieza):
    
    def __init__(self, fila, col, equipo):
        Pieza.__init__(self, "K", equipo, fila, col)  
    
    def valid_move(self, mesa, pos):
        f = pos[2] - pos[0] #Fila final - Fila inicial
        c = pos[3] - pos[1] #Columna final - Columna inicial
        mpos = True
        if abs(f) > 1 or abs(c) > 1:
            #Enroque
            if pos[0] == self.fila and pos[1] == self.col:#NO PASSAR FILA I COLUMNA 
                if f == 0:
                    if c == -2:
                        if mesa[pos[0]][pos[1] - 1].equipo == "N" and  mesa[pos[0]][pos[1] - 2].equipo == "N" and mesa[pos[0]][pos[1] - 3].equipo == "N":
                            if mesa[pos[0]][pos[1] - 4].tipo == "T" and mesa[pos[0]][pos[1] - 4].equipo == self.equipo:
                                mpos = True
                                self.enroque = True
                    elif c == 2:
                        if mesa[pos[0]][pos[1] + 1].equipo == "N" and  mesa[pos[0]][pos[1] + 2].equipo == "N":
                            if mesa[pos[0]][pos[1] + 3].tipo == "T" and mesa[pos[0]][pos[1] + 3].equipo == self.equipo:
                                mpos = True
                                self.enroque = True
                    else:
                        mpos = False
                        self.enroque = False
            else:
                mpos = False
                self.enroque = False
        else:
            mpos = True
            self.enroque = False        
        return mpos
