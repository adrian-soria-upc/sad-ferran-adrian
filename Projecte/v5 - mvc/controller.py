from piezas.pieza import Pieza
import server
#intToString() falta per fer
def comandoCorrecto(color, line):
    pos = [] 
    line = line.upper()
    if line[len(line) - 3] == "F" and line[len(line) - 2] == "F":
        tumbarRey(color)
        return True
    pos.append(ord(line[len(line) - 5]) - ord("1"))
    pos.append(ord(line[len(line) - 4]) - ord("A"))
    pos.append(ord(line[len(line) - 3]) - ord("1"))
    pos.append(ord(line[len(line) - 2]) - ord("A"))
    return controlMovimiento(pos, color)

def tumbarRey(color):
    for i in range(len(server.tablero.M)):
        for j in range(len(server.tablero.M[i])):
            if server.tablero.M[i][j].tipo == "K" and server.tablero.M[i][j].equipo == color:
                server.tablero.M[i][j] = Pieza(" ", "N", i, j)

def controlMovimiento(pos, color):
        for i in pos:
            if i > 7 or i < 0: #Miramos si estamos dentro del rango de actuación
                return False
        if server.tablero.M[pos[0]][pos[1]].equipo != color or server.tablero.M[pos[2]][pos[3]].equipo == server.tablero.M[pos[0]][pos[1]].equipo:
            return False
        elif server.tablero.M[pos[0]][pos[1]].valid_move(server.tablero.M, pos):
            return move(pos)
        else:
            return False

def enroque(pos):
    c = pos[3] - pos[1]
    if c > 0:
        server.tablero.M[pos[2]][pos[3]] = server.tablero.M[pos[0]][pos[1]]
        server.tablero.M[pos[0]][pos[1]] = Pieza(" ", "N", pos[0], pos[1])
        server.tablero.M[pos[2]][pos[3] - 1] = server.tablero.M[pos[2]][pos[3] + 1]
        server.tablero.M[pos[2]][pos[3] + 1] = Pieza(" ", "N", pos[2], pos[3] + 1)
    else:
        server.tablero.M[pos[2]][pos[3]] = server.tablero.M[pos[0]][pos[1]]
        server.tablero.M[pos[0]][pos[1]] = Pieza(" ", "N", pos[0], pos[1])
        server.tablero.M[pos[2]][pos[3] + 1] = server.tablero.M[pos[2]][pos[3] - 2]
        server.tablero.M[pos[2]][pos[3] - 2] = Pieza(" ", "N", pos[2], pos[3] - 2)

def move(pos):
    if server.tablero.M[pos[0]][pos[1]].enroque:
        enroque(pos)
    else:
        server.tablero.M[pos[2]][pos[3]] = server.tablero.M[pos[0]][pos[1]]
        server.tablero.M[pos[0]][pos[1]] = Pieza(" ", "N", pos[0], pos[1])
    server.tablero.jugador = abs(server.tablero.jugador - 1)
    return True 
