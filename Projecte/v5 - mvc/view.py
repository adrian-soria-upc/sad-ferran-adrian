from model import Tablero
#Mirar de juntar

def dibujarMesaStringAzul(matriz):
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
def dibujarMesaStringRojo(matriz):
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

def dibujarMesa(m, color, jugador):
    mesa = "\n"
    if jugador == 1:
        mesa += "\n" + "\033[;36m"+"                   TURNO JUGADOR AZUL" + "\n"
    else:
        mesa += "\n" + "\033[;31m"+"                   TURNO JUGADOR ROJO" + "\n"
    if color == 1:
        return mesa + dibujarMesaStringAzul(m)
    else:
        return mesa + dibujarMesaStringRojo(m)