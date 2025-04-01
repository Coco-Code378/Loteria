
                            #Funcion menu para loteria
#----------------------------------------------------------------------------------------------

def menu(): 
    
    #Funcion para menu principal
    def menu_principal():
        print(f"{"-" * 15} Bienvenidos al proyecto de lotería {"-" * 15}")
        print(f"{"-" * 6} ¿Qué selección de juego te gustaría jugar? {"-" * 6}")
        print(f"{"-" * 6} 1. Lotería")
        print(f"{"-" * 6} 2. Saca 3")
        print(f"{"-" * 6} 3. Salir")
    #Fin del menu principal
#------------------------------------------------------------------------------------------
    #Funcion para menu los juegos
    def menu_juegos():
        print(f"{"-" * 15} Bienvenido a la loteria {"-" * 15}")
        print(f"{"-" * 6} 1. Comprar boleta")
        print(f"{"-" * 6} 2. Comprar boleta con revancha")
        print(f"{"-" * 6} 3. Generar sorteo")
        print(f"{"-" * 6} 4. Reportes")
        print(f"{"-" * 6} 5. Salir")
    #Fin de la funcion de juegos
#-----------------------------------------------------------------------------------------
    #Funcion para menu de creacion de boletas
    def menu_boletas():
            print(f"\n {"-" * 15} Creación de Boletas {"-" * 15}\n")
            print(f"{"-" * 15} Selección de jugadas: {"-" * 15}")
            print(f"{"-" * 6} ¿Cómo deseas llenar tus jugadas? {"-" * 6}")
            print(f"{"-" * 6} 1. Aleatorio")
            print(f"{"-" * 6} 2. Manual")
    #fin de funcion para creacion de boletas
#------------------------------------------------------------------------------------------
    return menu_principal, menu_juegos, menu_boletas
