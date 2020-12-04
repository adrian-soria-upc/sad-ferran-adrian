from piezas.peon import Peon
from piezas.torre import Torre
from piezas.alfil import Alfil
from piezas.caballo import Caballo
from piezas.king import King
from piezas.queen import Queen

class Tablero():
    def __init__(self):
        self.M= [[0 for x in range(8)] for _ in range(8)] #Mesa
        self.jugador = 1 #azul = 1, rojo = 0

        self.M[0][0] = Torre(0, 0, 0)
        self.M[0][1] = Caballo(0, 1, 0)
        self.M[0][2] = Alfil(0, 2, 0)
        self.M[0][3] = Queen(0, 3, 0)
        self.M[0][4] = King(0, 4, 0)
        self.M[0][5] = Alfil(0, 5, 0)
        self.M[0][6] = Caballo(0, 6, 0)
        self.M[0][7] = Torre(0, 7, 0)

        for i in range(len(self.M[1])):
            self.M[1][i] = Peon(1, i, 0) 
        
        for i in range(len(self.M[6])):
            self.M[6][i] = Peon(1, i, 1)
            
        self.M[7][0] = Torre(7, 0, 1)
        self.M[7][1] = Caballo(7, 1, 1)
        self.M[7][2] = Alfil(7, 2, 1)
        self.M[7][3] = Queen(7, 3, 1)
        self.M[7][4] = King(7, 4, 1)
        self.M[7][5] = Alfil(7, 5, 1)
        self.M[7][6] = Caballo(7, 6, 1)
        self.M[7][7] = Torre(7, 7, 1)
    
    #Mirar de juntar
    def dibujarMesaStringAzul(self, matriz):
        mesa = ""
        mesa += "\033[;37m" + "        A     B     C     D     E     F     G     H" + "\n"
        mesa += "   ---------------------------------------------------" + "\n"
        for i in range(len(matriz)):
            mesa += str(i + 1) + "| " + '[ | '
            for j in range(len(matriz[i])):
                if matriz[i][j] == 0:
                    mesa += "    " + "| "
                else:
                    mesa += " " + matriz[i][j].getPieza() + "  | " 
            mesa += ']' + "\n" + "   ---------------------------------------------------" + "\n"
        mesa += "        A     B     C     D     E     F     G     H" + "\n" + "\n"
        return mesa

    #Mirar de juntar
    def dibujarMesaStringRojo(self, matriz):
        mesa = ""
        mesa += "\033[;37m" + "        H     G     F     E     D     C     B     A" + "\n"
        mesa += "   ---------------------------------------------------" + "\n" 
        for i in range(len(matriz)):
            mesa += str(8 - i) + "| " + '[ | '
            for j in range(len(matriz[7 - i])):
                if matriz[7 - i][7 - j] == 0:
                    mesa += "    " + "| "
                else:
                    mesa += " " + matriz[7 - i][7 - j].getPieza() + "  | " 
            mesa += ']' + "\n" + "   ---------------------------------------------------" + "\n"
        mesa += "        H     G     F     E     D     C     B     A" + "\n" + "\n"
        return mesa

    def dibujarMesa(self, m, color):
        mesa = ""
        if self.jugador == 1:
            mesa += "\n" + "\033[;36m"+"                   TURNO JUGADOR AZUL" + "\n"
        else:
            mesa += "\n" + "\033[;31m"+"                   TURNO JUGADOR ROJO" + "\n"
        if color == 1:
            return mesa + self.dibujarMesaStringAzul(m)
        else:
            return mesa + self.dibujarMesaStringRojo(m)
  
    def comandocorrecto(self,color, line):
        pos = [] 
        line = line.upper()
        if line[len(line) - 3] == "F" and line[len(line) - 2] == "F":
            self.tumbarRey(color)
            return True
        pos.append(ord(line[len(line) - 5]) - ord("1"))
        pos.append(ord(line[len(line) - 4]) - ord("A"))
        pos.append(ord(line[len(line) - 3]) - ord("1"))
        pos.append(ord(line[len(line) - 2]) - ord("A"))
        return self.controlMovimiento(pos, color)
    
    def tumbarRey(self, color):
        for i in range(len(self.M)):
            for j in range(len(self.M[i])):
                if self.M[i][j] != 0:
                    if self.M[i][j].tipo == "K" and self.M[i][j].equipo == color:
                        self.M[i][j] = 0

    #Optimitzar al final
    def controlMovimiento(self, pos, color):
            for i in pos:
                if i > 7 or i < 0: #Miramos si estamos dentro del rango de actuación
                    return False
            if self.M[pos[0]][pos[1]] == 0:
                return False
            elif self.M[pos[0]][pos[1]].equipo != color:
                return False
            elif self.M[pos[2]][pos[3]] == 0: #Miramos si la casilla esta vacía
                return self.move(pos)
            elif self.M[pos[2]][pos[3]].equipo == self.M[pos[0]][pos[1]].equipo: #Miramos si la pieza de destino es de nuestro equipo
                return False
            else:
                return self.move(pos)
    
    def enroque(self, pos):
        c = pos[3] - pos[1]
        if c > 0:
            self.M[pos[2]][pos[3]] = self.M[pos[0]][pos[1]]
            self.M[pos[0]][pos[1]] = 0
            self.M[pos[2]][pos[3] - 1] = self.M[pos[2]][pos[3] + 1]
            self.M[pos[2]][pos[3] + 1] = 0
        else:
            self.M[pos[2]][pos[3]] = self.M[pos[0]][pos[1]]
            self.M[pos[0]][pos[1]] = 0
            self.M[pos[2]][pos[3] + 1] = self.M[pos[2]][pos[3] - 2]
            self.M[pos[2]][pos[3] - 2] = 0

    def move(self,pos):
        mcomp = self.M[pos[0]][pos[1]].valid_move(self.M, pos)
        if mcomp:
            if self.M[pos[0]][pos[1]].enroque:
                self.enroque(pos)
            else:
                self.M[pos[2]][pos[3]] = self.M[pos[0]][pos[1]]
                self.M[pos[0]][pos[1]] = 0
            self.jugador = abs(self.jugador - 1)
            return True 
        else:
            return False
    
    def comprobarPartida(self):
        numK = 0
        pos = []
        for i in range(len(self.M)):
            for j in range(len(self.M[i])):
                if self.M[i][j] != 0:
                    if self.M[i][j].tipo == "K":
                        numK += 1
                        pos.append(i)
                        pos.append(j)
        if numK < 2:
            if self.M[pos[0]][pos[1]].equipo == 0:
                self.jugador = 0
                return False
            else:
                self.jugador = 1
                return False
        else:
            return True