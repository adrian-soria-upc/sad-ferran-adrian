from piezas.peon import Peon
from piezas.torre import Torre
from piezas.alfil import Alfil
from piezas.caballo import Caballo
from piezas.king import King
from piezas.queen import Queen

class Tablero():
    def __init__(self):
        self.M= [[0 for x in range(8)] for _ in range(8)] #Mesa
        self.jugador = "azul"
    
        self.M[0][0] = Torre(0, 0, "R")
        self.M[0][1] = Caballo(0, 1, "R")
        self.M[0][2] = Alfil(0, 2, "R")
        self.M[0][3] = Queen(0, 3, "R")
        self.M[0][4] = King(0, 4, "R")
        self.M[0][5] = Alfil(0, 5, "R")
        self.M[0][6] = Caballo(0, 6, "R")
        self.M[0][7] = Torre(0, 7, "R")
    
        self.M[1][0] = Peon(1, 0, "R")
        self.M[1][1] = Peon(1, 1, "R")
        self.M[1][2] = Peon(1, 2, "R")
        self.M[1][3] = Peon(1, 3, "R")
        self.M[1][4] = Peon(1, 4, "R")
        self.M[1][5] = Peon(1, 5, "R")
        self.M[1][6] = Peon(1, 6, "R")
        self.M[1][7] = Peon(1, 7, "R")
        
        self.M[6][0] = Peon(6, 0, "A")
        self.M[6][1] = Peon(6, 1, "A")
        self.M[6][2] = Peon(6, 2, "A")
        self.M[6][3] = Peon(6, 3, "A")
        self.M[6][4] = Peon(6, 4, "A")
        self.M[6][5] = Peon(6, 5, "A")
        self.M[6][6] = Peon(6, 6, "A")
        self.M[6][7] = Peon(6, 7, "A")
    
        self.M[7][0] = Torre(7, 0, "A")
        self.M[7][1] = Caballo(7, 1, "A")
        self.M[7][2] = Alfil(7, 2, "A")
        self.M[7][3] = Queen(7, 3, "A")
        self.M[7][4] = King(7, 4, "A")
        self.M[7][5] = Alfil(7, 5, "A")
        self.M[7][6] = Caballo(7, 6, "A")
        self.M[7][7] = Torre(7, 7, "A")
    
    def dibujarMesaStringAzul(self, matriz):
        mesa = ""
        if self.jugador == "azul":
            mesa += "\n" + "\033[;36m"+"                   TURNO JUGADOR AZUL" + "\n"
        else:
            mesa += "\n" + "\033[;31m"+"                   TURNO JUGADOR ROJO" + "\n"
        mesa += "\033[;37m" + "        A     B     C     D     E     F     G     H" + "\n" + "   ---------------------------------------------------" + "\n"
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

    def dibujarMesaStringRojo(self, matriz):
        mesa = ""
        if self.jugador == "azul":
            mesa += "\n" + "\033[;36m"+"                   TURNO JUGADOR AZUL" + "\n"
        else:
            mesa += "\n" + "\033[;31m"+"                   TURNO JUGADOR ROJO" + "\n"
        mesa += "\033[;37m" + "        H     G     F     E     D     C     B     A" + "\n" + "   ---------------------------------------------------" + "\n"
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
               
    def comandocorrecto(self,color, line):
        pos = [] 
        inp = line
        inp = inp.upper()
        if inp[len(inp) - 3] == "F" and inp[len(inp) - 2] == "F":
            self.tumbarRey(color)
            return True
        pos.append(ord(inp[len(inp)-5]) - ord("1"))
        pos.append(ord(inp[len(inp)-4]) - ord("A"))
        pos.append(ord(inp[len(inp)-3]) - ord("1"))
        pos.append(ord(inp[len(inp)-2]) - ord("A"))
        return self.controlMovimiento(pos, color)
    
    def tumbarRey(self, color):
        if color == "azul":
            color = "A"
        else:
            color = "R"
        for i in range(len(self.M)):
            for j in range(len(self.M[i])):
                if self.M[i][j] != 0:
                    if self.M[i][j].tipo == "K" and self.M[i][j].equipo == color:
                        self.M[i][j] = 0

    def controlMovimiento(self, pos, color):
            for i in pos:
                if i > 7 or i < 0: #Miramos si estamos dentro del rango de actuación
                    return False
            if self.M[pos[0]][pos[1]] == 0:
                return False
            elif self.M[pos[0]][pos[1]].equipo == "A" and color == "rojo":
                return False
            elif self.M[pos[0]][pos[1]].equipo == "R" and color == "azul":
                return False
            elif self.M[pos[2]][pos[3]] == 0: #Miramos si la casilla esta vacía
                return self.move(pos)
            elif self.M[pos[2]][pos[3]].equipo == self.M[pos[0]][pos[1]].equipo: #Miramos si la pieza de destino no es de nuestro equipo
                return False
            else:
                return self.move(pos)
    
    def move(self,pos):
        mcomp = self.M[pos[0]][pos[1]].valid_move(self.M, pos)
        if mcomp:
             self.M[pos[2]][pos[3]] = self.M[pos[0]][pos[1]]
             self.M[pos[0]][pos[1]] = 0
             if self.jugador == "azul":
             	self.jugador = "rojo"
             else: 
                self.jugador = "azul"
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
            if self.M[pos[0]][pos[1]].equipo == "R":
                self.jugador = "rojo"
                return False
            else:
                self.jugador = "azul"
                return False
        else:
            return True