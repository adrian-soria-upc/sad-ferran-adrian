from tablero import Tablero

if __name__ == "__main__":
    mesa = Tablero()
    mesa.dibujarMesa(mesa.M)
    
    while mesa.jugando == True:
        mesa.turno()