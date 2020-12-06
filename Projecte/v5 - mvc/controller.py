from piezas.pieza import Pieza
#intToString() falta per fer

def comandoCorrecto(color, line, tablero):
    pos = [] 
    line = line.upper()
    if line[len(line) - 3] == "F" and line[len(line) - 2] == "F":
        tumbarRey(color, tablero.M)
        return True
    pos.append(ord(line[len(line) - 5]) - ord("1"))
    pos.append(ord(line[len(line) - 4]) - ord("A"))
    pos.append(ord(line[len(line) - 3]) - ord("1"))
    pos.append(ord(line[len(line) - 2]) - ord("A"))
    return controlMovimiento(pos, color, tablero)

def tumbarRey(color,m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j].tipo == "K" and m[i][j].equipo == color:
                m[i][j] = Pieza(" ", "N")

def controlMovimiento(pos, color, tablero):
        for i in pos:
            if i > 7 or i < 0: #Miramos si estamos dentro del rango de actuación
                return False
        if tablero.M[pos[0]][pos[1]].equipo != color or tablero.M[pos[2]][pos[3]].equipo == tablero.M[pos[0]][pos[1]].equipo:
            return False
        elif tablero.M[pos[0]][pos[1]].valid_move(tablero.M, pos):
            return move(pos, tablero)
        else:
            return False

def enroque(pos,m):
    c = pos[3] - pos[1]
    if c > 0:
        m[pos[2]][pos[3]] = m[pos[0]][pos[1]]
        m[pos[0]][pos[1]] = Pieza(" ", "N")
        m[pos[2]][pos[3] - 1] = m[pos[2]][pos[3] + 1]
        m[pos[2]][pos[3] + 1] = Pieza(" ", "N")
    else:
        m[pos[2]][pos[3]] = m[pos[0]][pos[1]]
        m[pos[0]][pos[1]] = Pieza(" ", "N")
        m[pos[2]][pos[3] + 1] = m[pos[2]][pos[3] - 2]
        m[pos[2]][pos[3] - 2] = Pieza(" ", "N")

def move(pos,tablero):
    if tablero.M[pos[0]][pos[1]].enroque:
        enroque(pos, tablero.M)
    else:
        tablero.M[pos[2]][pos[3]] = tablero.M[pos[0]][pos[1]]
        tablero.M[pos[0]][pos[1]] = Pieza(" ", "N")
    tablero.turno = abs(tablero.turno - 1)
    return True 

