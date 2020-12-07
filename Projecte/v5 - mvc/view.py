BLUE = '\033[34m'
RED = '\033[31m'
DEFAULT = '\033[0m'
def dibujarMesa(color, tablero):
    mesa = ""
    if tablero.turno == 1:
        mesa += "\n" + BLUE +"                   TURNO JUGADOR AZUL" + "\n"
    else:
        mesa += "\n" + RED +"                   TURNO JUGADOR ROJO" + "\n"
    if color == 1:
        mesa += dibujarMesaStringAzul(tablero.M)
    else:
        mesa += dibujarMesaStringRojo(tablero.M)
    if tablero.comprobarPartida() == False:
        if tablero.turno == 1:
            mesa += "EL GANADOR ES EL JUGADOR ROJO\n"
        else:
            mesa += "EL GANADOR ES EL JUGADOR AZUL\n"
    return mesa		

def dibujarMesaStringAzul(matriz):
    mesa = ""
    mesa += DEFAULT + "        " + "A     B     C     D     E     F     G     H" + "\n"
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
    mesa += DEFAULT + "        " + "H     G     F     E     D     C     B     A" + "\n"
    mesa += "   " + "---------------------------------------------------" + "\n" 
    for i in range(len(matriz)):
        mesa += str(8 - i) + "| " + '[ | '
        for j in range(len(matriz[7 - i])):
            mesa += " " + matriz[7 - i][7 - j].getPieza() + "  | " 
        mesa += ']' + "\n" + "   " + "---------------------------------------------------" + "\n"
    mesa += "        " + "H     G     F     E     D     C     B     A" + "\n" + "\n" + "\n"
    return mesa

def dibujarInicio(jugador, tablero, nick, color):
    mesa = "Bienvenido " + nick + ".\nEn este juego de ajedrez, las piezas azules coresponden a las blancas y las rojas a las negras.\nPara hacer un movimiento debes introducir por ejemplo: 7d6d. Donde '7d' corresponde a las coordenadas de origen de la pieza, y 6d las coordenadas de destino. Si introduces ff te rendiras. El color de tus piezas es: "
    mesa += jugador + " ¡SUERTE!\n" 
    return mesa + dibujarMesa(color, tablero)

def dibujarComanda(color, nick, line):
    if color == 1:
        return f"{BLUE}{nick}>{DEFAULT} {line}"
    else:
        return f"{RED}{nick}>{DEFAULT} {line}"
