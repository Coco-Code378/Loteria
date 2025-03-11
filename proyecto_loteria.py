#Proyecto de loteria 
#Joel Maisonet
#Christian Matias 
#Jorge Maldonado

#librerias
import random #importamos la libreria random
import os #importamos os


#Variables
data_dir = "data" 


#boletas_dir = os.path.join(data_dir, "boletos")  
#sorteos_dir = os.path.join(data_dir, "sorteos")
#reportes_dir = os.path.join(data_dir, "reportes")



#creamos los directorios o carpetas de archivos 

#boletas_dir = os.path.join(data_dir, "boletos")  
#sorteos_dir = os.path.join(data_dir, "sorteos")
#reportes_dir = os.path.join(data_dir, "reportes")

                                        #Creación del programa
#-----------------------------------------------------------------------------------------------------

#Función para detectar y limpiar terminal dependiendo del sistema operativo
def limpiar_pantalla():
    # Detecta el sistema operativo y usa el comando correspondiente
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix (Linux, macOS)
        os.system('clear')
# Fin de la función Limpiar_Pantalla

#Funcion para la creación de boletas
def creacion_boletas_loteria():
   
    def aleatorio():
         boletas_aleatoria = []
         revancha_aleatoria = []
    def manual():
        cantidad_jugadas = int(input("Ingrese la cantidad de jugadas a realizar: "))

        jugadas = []
        boletas_manual = []
        for i in range(cantidad_jugadas):
            valores_jugadas = []
            valores_unicos = set()
    
            for j in range(6):
                while True:  
                    numeros = int(input(f"Ingrese un valor: {j + 1} del 0 al {66 - 1} en la jugada {i + 1}, (No se puede repetir): "))
                
                    if not numeros < 0 and not numeros > 65:
                        if numeros not in valores_unicos:
                            print(f"El número: {numeros} fue agregado")
                            valores_jugadas.append(numeros)
                            valores_unicos.add(numeros)
                            break  
                        else:
                            print(f"No se puede repetir el valor {numeros}, por favor inténtelo de nuevo")
                    else:
                        print("Elegiste un número no correspondido a lo que se pide.")    
            valores_unicos.clear()             
            jugadas.append(valores_jugadas)
        
        boletas_manual.append(jugadas)
        print(f"{jugadas}")
        print(f"{boletas_manual}")
    return aleatorio, manual
        
# Fin de la creación de boletas

#Funcion menu para loteria
def menu(): 
    
    #Funcion para menu principal
    def menu_principal():
        print(f"{"-" * 15} Bienvenidos al proyecto de lotería {"-" * 15}")
        print(f"{"-" * 6} ¿Qué selección de juego te gustaría jugar? {"-" * 6}")
        print(f"{"-" * 6} 1. Lotería")
        print(f"{"-" * 6} 2. Saca 3")
        print(f"{"-" * 6} 3. Salir")
    #Fin del menu principal

    #Funcion para menu los juegos
    def menu_juegos():
        print(f"{"-" * 15} Bienvenido a la loteria {"-" * 15}")
        print(f"{"-" * 6} 1. Comprar boleta")
        print(f"{"-" * 6} 2. Generar sorteo")
        print(f"{"-" * 6} 3. Reportes")
        print(f"{"-" * 6} 4. Salir")
    #Fin de la funcion de juegos

    #Funcion para menu de creacion de boletas
    def menu_boletas():
            print(f"\n {"-" * 15} Creación de Boletas {"-" * 15}\n")
            print(f"{"-" * 15} Selección de jugadas: {"-" * 15}")
            print(f"{"-" * 6} ¿Cómo deseas llenar tus jugadas? {"-" * 6}")
            print(f"{"-" * 6} 1. Aleatorio")
            print(f"{"-" * 6} 1. Manual")
    #fin de funcion para creacion de boletas
    
    return menu_principal, menu_juegos, menu_boletas

#Fin de la función menu    


#Función para el programa Main
def main():
    #Referencias de funciones:
    principal, juego, boletas = menu()
    aleatorio, manual = creacion_boletas_loteria()
    while True:
        try:
            principal()
            opcion = str(input("\n Elige la opción a seleccionar: "))
            

            match opcion:

                #Lotería
                case "1":
                    # Llamando la función Limpiar_pantalla
                    limpiar_pantalla()
                    while True:
                        try:
                            # Llamando la función menu_loteria
                            juego()
                            opcion_uno = str(input("\n Elige la opción a seleccionar: "))

                            match opcion_uno:
                                case "1":
                                    '''
                                    Jorge, esta parte te la dejaré a ti, lo que debes de hacer es implementar el menu donde indique si el usuario quiere jugar manual o automático.
                                    Inténtalo realizarlo con un while true y con un try y except. Para implementar el menu para boletas, solo tienes que llamarla: boletas()
                                    '''
                                    # Llamando la función Limpiar_pantalla
                                    limpiar_pantalla()
                                    manual()
                                    
                                case "2":
                                    print(f"\n {"-" * 15} Sorteos {"-" * 15}\n")
                                case "3":
                                    print(f"{"-" * 15} Saliendo del programa... {"-" * 15}")
                                    break
                                case _:
                                    print("Hubo un error al intentar seleccionar la opción deseada.")
                        except Exception as error:
                            print(f"Tiene un error llamado {error}, inténtalo más tarde por favor.")
                    
                    

                #Saca 3
                case "2":
                    # Llamando la función Limpiar_pantalla
                    limpiar_pantalla()
                    print(f"\n {"-" * 15} Saca 3 {"-" * 15}\n")
                    # Llamando la función menu_saca3
                    juego()

                #Salir del programa
                case "3":
                    print(f"{"-" * 15} Saliendo del programa... {"-" * 15}")
                    break
                case _:
                    print("Hubo un error al intentar seleccionar la opción deseada.")
        except:
            print("Hubo error en el programa por lo que no pudo ser compilado.")
# Fin de la función Main

#Llamada a la función Main para que el programa empiece con dicha función
main()