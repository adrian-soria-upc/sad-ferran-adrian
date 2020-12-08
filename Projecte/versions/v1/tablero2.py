from peon import Peon
from torre import Torre
from alfil import Alfil
from caballo import Caballo
from king import King
from queen import Queen

class Tablero:
    def __init__(self):
        self.M= [[0 for x in range(8)] for _ in range(8)] #Mesa
        self.jugando = True
        self.jugador = 1 #Jugador 1 azules, jugador 0 rojas

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

    #Cliente
    def dibujarMesa(self, matriz):
        print("")
        if self.jugador == 1:
            print("\033[;36m"+"                 TURNO JUGADOR AZUL", end = "")
        else:
            print("\033[;31m"+"                 TURNO JUGADOR ROJO", end = "")
        print("\033[;37m")
        print("       A     B     C     D     E     F     G     H")
        print("   -------------------------------------------------")
        for i in range(len(matriz)):
            print(i + 1, end = "| ")
            print('[|', end = " ")
            for j in range(len(matriz[i])):
                if self.M[i][j] == 0:
                    print(" ", end = "")
                    print(" ", end = "  ")
                    print("|", end = " ")
                else:
                    print(" ", end = "")
                    print(matriz[i][j].getPieza(), end = "  ")
                    print("|", end = " ")
            print (']')
            print("   -------------------------------------------------")
        print("       A     B     C     D     E     F     G     H")
        print()
        
    def dibujarMesaString(self, matriz):
        mesa = ""
        if self.jugador == 1:
            mesa += "\033[;36m"+"                 TURNO JUGADOR AZUL" + "\n"
        else:
            mesa += "\033[;31m"+"                 TURNO JUGADOR ROJO" + "\n"
        mesa += "\033[;37m" + "       A     B     C     D     E     F     G     H" + "\n" + "   -------------------------------------------------" + "\n"
        for i in range(len(matriz)):
            mesa += str(i + 1) + "| " + '[| '
            for j in range(len(matriz[i])):
                if matriz[i][j] == 0:
                    mesa += "    " + "| "
                else:
                    mesa += " " + matriz[i][j].getPieza() + "  | " 
            mesa += ']' + "\n" + "   -------------------------------------------------" + "\n"
        mesa += "       A     B     C     D     E     F     G     H" + "\n"
        return mesa
        
    # def get_danger_moves(self):
    #     danger_moves_azul = []
    #     danger_moves_rojo = []
    #     for i in range(len(self.M)):
    #         for j in range(len(self.M[i])):
    #             if self.M[i][j] != 0:
    #                 if self.M[i][j].equipo == "A":
    #                     danger_moves_azul.append(self.M[i][j].getAmenazaAzul(self.M))
    #                 if self.M[i][j].equipo == "R":
    #                     danger_moves_rojo.append(self.M[i][j].getAmenazaRoja(self.M))
    #     return danger_moves_azul
    
        
    def turno(self):
        #Aixó representa el torn d'un jugador
        #Cliente envia jugada
        pos = []
        print("¿Que pieza quieres mover? (Ejemplo 8A)")
        inp = str(input())
        print("¿A dónde la quieres mover? (Ejemplo 2A)")
        inp = inp + str(input())
        inp = inp.upper()
        #Servidor procesa jugada
        pos.append(int(inp[0]) - 1)
        pos.append(ord(inp[1]) - ord("A"))
        pos.append(int(inp[2]) - 1)
        pos.append(ord(inp[3]) - ord("A"))
        self.controlMovimiento(pos)
        
    def move(self,pos):
        mcomp = self.M[pos[0]][pos[1]].valid_move(self.M, pos)
        if mcomp:
             self.M[pos[2]][pos[3]] = self.M[pos[0]][pos[1]]
             # self.M[pos[2]][pos[3]].fila = pos[2]
             # self.M[pos[2]][pos[3]].col = pos[3]
             self.M[pos[0]][pos[1]] = 0
             self.comprobarPartida()
             #Cambio de jugador
             self.jugador = abs(self.jugador - 1)
             #Enviar resposta al client
             self.dibujarMesa(self.M)
             
        else:
            print("Movimiento de pieza incorrecto")
            self.dibujarMesa(self.M)
            self.turno()
        
    def comprobarPartida(self):
        chain = self.tableroToString(self.M)
        if chain.count("K") < 2:
            k = chain.find("K") + 64
            if k == "A":
                print("GANA EL JUGADOR ROJO")
            else:
                print("GANA EL JUGADOR AZUL")
            self.jugando = False
        
    #Controla si se puede mover en primera instancia la pieza
    def controlMovimiento(self, pos):
        for i in pos:
            if i > 7 or i < 0: #Miramos si estamos dentro del rango de actuación
                print("Movimiento no válido, fuera de rango")
                self.turno()
                return
        if self.M[pos[0]][pos[1]].equipo == "R" and self.jugador == 1:
            print("No es tu pieza")
            self.turno()
            return
        elif self.M[pos[0]][pos[1]].equipo == "A" and self.jugador == 0:
            print("No es tu pieza")
            self.turno()
            return
        elif self.M[pos[2]][pos[3]] == 0: #Miramos si la casilla esta vacía
            self.move(pos)
            return
        elif self.M[pos[2]][pos[3]].equipo == self.M[pos[0]][pos[1]].equipo: #Miramos si la pieza de destino no es de nuestro equipo
                print("Movimiento no válido, es tu pieza")
                self.turno()
                return
        else:
            self.move(pos)
            return    

    #Función que pasa de una matriz, a una string para enviar
    def tableroToString(self, mesa):
        piezas = ""
        equipo = ""
        for i in range(len(mesa)):
            for j in range(len(mesa[i])):
                if mesa[i][j] != 0:
                    piezas = piezas + mesa[i][j].tipo
                    equipo = equipo + mesa[i][j].equipo
                else:
                    piezas = piezas + "0"
                    equipo = equipo + "N"
        chain = piezas + equipo
        return chain
       
    #Funcion que pasa dos strings, a una matriz
    def stringToTablero(self, chain):
        mesa= [[0 for x in range(8)] for _ in range(8)] #Mesa
        piezas = ""
        equipo = ""
        tipo = 0
        for i in range(len(chain)):
            if i < 64:
                piezas = piezas + chain[i]
            else:
                equipo = equipo + chain[i]
        for i in range(len(mesa)):
            for j in range(len(mesa[i])):
                if piezas[tipo] == "P":
                    mesa[i][j] = Peon(i, j, equipo[tipo])
                elif piezas[tipo] == "A":
                    mesa[i][j] = Alfil(i, j, equipo[tipo])
                elif piezas[tipo] == "C":
                    mesa[i][j] = Caballo(i, j, equipo[tipo])
                elif piezas[tipo] == "T":
                    mesa[i][j] = Torre(i, j, equipo[tipo])
                elif piezas[tipo] == "K":
                    mesa[i][j] = King(i, j, equipo[tipo])
                elif piezas[tipo] == "Q":
                    mesa[i][j] = Queen(i, j, equipo[tipo])
                else:
                    mesa[i][j] = 0
                tipo = tipo + 1
        return mesa
    
    