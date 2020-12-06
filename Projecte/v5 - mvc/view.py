#POSAR RED;BLUE;DEFAULT
#Posar Strings Server
def dibujarMesa(color, tablero):
    mesa = ""
    if tablero.turno == 1:
        mesa += "\n" + "\033[;36m"+"                   TURNO JUGADOR AZUL" + "\n"
    else:
        mesa += "\n" + "\033[;31m"+"                   TURNO JUGADOR ROJO" + "\n"
    if color == 1:
        return mesa + dibujarMesaStringAzul(tablero.M)
    else:
        return mesa + dibujarMesaStringRojo(tablero.M)

def dibujarMesaStringAzul(matriz):
    mesa = ""
    mesa += "\033[;37m" + "        " + "A     B     C     D     E     F     G     H" + "\n"
    mesa += "   " + "---------------------------------------------------" + "\n"
    for i in range(len(matriz)):
        mesa += str(i + 1) + "| " + '[ | '
        for j in range(len(matriz[i])):
            mesa += " " + matriz[i][j].getPieza() + "  | " 
        mesa += ']' + "\n" + "   " + "---------------------------------------------------" + "\n"
    mesa += "        " + "A     B     C     D     E     F     G     H" + "\n" + "\n" + "\n"
    return mesa

def dibujarMesaStringRojo(matriz):
    mesa = ""
    mesa += "\033[;37m" + "        " + "H     G     F     E     D     C     B     A" + "\n"
    mesa += "   " + "---------------------------------------------------" + "\n" 
    for i in range(len(matriz)):
        mesa += str(8 - i) + "| " + '[ | '
        for j in range(len(matriz[7 - i])):
            mesa += " " + matriz[7 - i][7 - j].getPieza() + "  | " 
        mesa += ']' + "\n" + "   " + "---------------------------------------------------" + "\n"
    mesa += "        " + "H     G     F     E     D     C     B     A" + "\n" + "\n" + "\n"
    return mesa
