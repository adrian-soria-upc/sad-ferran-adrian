def comandocorrecto(color, line, m):
    pos = [] 
    line = line.upper()
    if line[len(line) - 3] == "F" and line[len(line) - 2] == "F":
        tumbarRey(color)
        return True
    pos.append(ord(line[len(line) - 5]) - ord("1"))
    pos.append(ord(line[len(line) - 4]) - ord("A"))
    pos.append(ord(line[len(line) - 3]) - ord("1"))
    pos.append(ord(line[len(line) - 2]) - ord("A"))
    return controlMovimiento(pos, color, m)

def tumbarRey(color, m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] != 0:
                if m[i][j].tipo == "K" and m[i][j].equipo == color:
                    m[i][j] = 0

#Optimitzar al final
def controlMovimiento(pos, color, m):
        for i in pos:
            if i > 7 or i < 0: #Miramos si estamos dentro del rango de actuación
                return False
        if m[pos[0]][pos[1]] == 0:
            return False
        elif m[pos[0]][pos[1]].equipo != color:
            return False
        elif m[pos[2]][pos[3]] == 0: #Miramos si la casilla esta vacía
            return move(pos, m)
        elif m[pos[2]][pos[3]].equipo == m[pos[0]][pos[1]].equipo: #Miramos si la pieza de destino es de nuestro equipo
            return False
        else:
            return move(pos, m)

def enroque(pos, m):
    c = pos[3] - pos[1]
    if c > 0:
        m[pos[2]][pos[3]] = m[pos[0]][pos[1]]
        m[pos[0]][pos[1]] = 0
        m[pos[2]][pos[3] - 1] = m[pos[2]][pos[3] + 1]
        m[pos[2]][pos[3] + 1] = 0
    else:
        m[pos[2]][pos[3]] = m[pos[0]][pos[1]]
        m[pos[0]][pos[1]] = 0
        m[pos[2]][pos[3] + 1] = m[pos[2]][pos[3] - 2]
        m[pos[2]][pos[3] - 2] = 0

def move(pos, m):
    mcomp = m[pos[0]][pos[1]].valid_move(m, pos)
    if mcomp:
        if m[pos[0]][pos[1]].enroque:
            enroque(pos, m)
        else:
            m[pos[2]][pos[3]] = m[pos[0]][pos[1]]
            m[pos[0]][pos[1]] = 0
        #tablero.jugador = abs(tablero.jugador - 1)
        return True 
    else:
        return False