from tablero import Tablero

if __name__ == "__main__":
    mesa = Tablero()
    mesa.dibujarMesa(mesa.M)
    chain = mesa.tableroToString(mesa.M)
    print(chain)
    prueba = mesa.stringToTablero(chain)
    mesa.dibujarMesa(prueba)
    
    
    # while mesa.jugando == True:
    #     mesa.turno()