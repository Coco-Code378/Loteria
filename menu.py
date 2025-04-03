
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
        print(f"{"-" * 6} 2. Generar sorteo")
        print(f"{"-" * 6} 3. Reportes")
        print(f"{"-" * 6} 4. Salir")
    #Fin de la funcion de juegos
#-----------------------------------------------------------------------------------------
    #Funcion para menu de creacion de boletas
    def menu_boletas():
            print(f"\n {"-" * 15} Creación de Boletas {"-" * 15}\n")
            print(f"{"-" * 15} Selección de jugadas: {"-" * 15}")
            print(f"{"-" * 6} ¿Cómo deseas llenar tus jugadas? {"-" * 6}")
            print(f"{"-" * 6} 1. Manual")
            print(f"{"-" * 6} 2. Aleatorio")
    #fin de funcion para creacion de boletas
#------------------------------------------------------------------------------------------
    #Funcion Secundaria para premios de lotería
#---------------------------------------------------------------------------------------------------------
    def premios_loteria():
    #Tabla para hacer print a los premios principales      #Tabla para hacer print a los premios de revancha
                                                        #Columnas:
        print("+--------------------------------------+          +--------------------------------------+") 
        print("|                 Premios              |          |         Premios  de  Revancha        |")
        print("+--------------------------------------+          +--------------------------------------+")    
        print("| Sorteo Principal      |    Premio    |          |     Revancha      |      Premio      |")
        print("+--------------------------------------+          +--------------------------------------+")
    
                                                        #Filas:
        print("| Acierta los 6 números | 1,000,000.00 |          | Acierta los 6 números | 500,000.00   |")
        print("+--------------------------------------+          +--------------------------------------+")
        print("|  Acierta 5 números    | 300,000.00   |          |  Acierta 5 números    | 100,000.00   |")
        print("+--------------------------------------+          +--------------------------------------+")
        print("|  Acierta 4 números    | 75,0000.00   |          |  Acierta 4 números    | 25,0000.00   |")
        print("+--------------------------------------+          +--------------------------------------+")
        print("|  Acierta 3 números    |  1  boleto   |")
        print("+--------------------------------------+")


 #------------------------------------------------------------------------------------------------------------
 # Fin de la función de premios para Loteria      

#Funcion Secundaria para premios de lotería
#---------------------------------------------------------------------------------------------------------
    def premios_saca3():
    #Tabla para hacer print a los premios principales                                            #Tabla para hacer print a los premios revancha
                                                                                #Columnas:
        print("+------------------------------------------------------------+                     +------------------------------------------------------------+")
        print("|                                Premios                     |                     |                                Premios                     |")
        print("+------------------------------------------------------------+                     +------------------------------------------------------------+")
        print("|            Sorteo Principal         |        Premio        |                     |              Revancha              |        Premio         |")
        print("+------------------------------------------------------------+                     +------------------------------------------------------------+")
    
                                                                                  # Filas: 
        print("| Exacta(3 números en orden correcto) |        100,000.00    |                     | Exacta(3 números en orden correcto) |        25,000.00     |")
        print("+------------------------------------------------------------+                     +------------------------------------------------------------+")
        print("|             Combinada               |         25,000.00    |                     |             Combinada               |        12,500.00     |")
        print("| (3 números en cualquier orden)      |                      |                     | (3 números en cualquier orden)      |                      |")
        print("+------------------------------------------------------------+                     +------------------------------------------------------------+")
        
        
 #------------------------------------------------------------------------------------------------------------
 # Fin de la función de premios para Loteria      
    return menu_principal, menu_juegos, menu_boletas, premios_loteria, premios_saca3
