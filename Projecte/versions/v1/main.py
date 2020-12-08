from tablero import Tablero

if __name__ == "__main__":
    mesa = Tablero()
    ferran = mesa.dibujarMesaString(mesa.M)
    print(ferran)
    print(len(ferran))
    
    # while mesa.jugando == True:
    #     mesa.turno()