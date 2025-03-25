
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
    else:  # Para (Linux, macOS)
        os.system('clear')
# Fin de la función Limpiar_Pantalla

#-------------------------------------------------------------------------------------------------------
#Funcion Principal de creación de boletas

def creacion_boletas_loteria():
    boleta_total = []

#Funcion Secundaria para premios de lotería
#---------------------------------------------------------------------------------------------------------
    def premios_loteria():
    #Tabla para hacer print a los premios principales
    #Columnas:
        print("+--------------------------------------+")
        print("|                 Premios              |")
        print("+--------------------------------------+")
        print("| Sorteo Principal      |    Premio    |")
        print("+--------------------------------------+")
    
    # Filas:
        print("| Acierta los 6 números | 1,000,000.00 |")
        print("+--------------------------------------+")
        print("|  Acierta 5 números    | 300,000.00   |")
        print("+--------------------------------------+")
        print("|  Acierta 4 números    | 75,0000.00   |")
        print("+--------------------------------------+")
        print("|  Acierta 3 números    |  1  boleto   |")
        print("+--------------------------------------+")

    #Tabla para hacer print a los premios de revancha
    #Columnas:
        print("+--------------------------------------+")
        print("|         Premios  de  Revancha        |")
        print("+--------------------------------------+")
        print("|     Revancha      |      Premio      |")
        print("+--------------------------------------+")
    
    # Filas:
        print("| Acierta los 6 números | 500,000.00   |")
        print("+--------------------------------------+")
        print("|  Acierta 5 números    | 100,000.00   |")
        print("+--------------------------------------+")
        print("|  Acierta 4 números    | 25,0000.00   |")
        print("+--------------------------------------+")
 #------------------------------------------------------------------------------------------------------------
 # Fin de la función de premios para Loteria      

#Funcion Secundaria para premios de lotería
#---------------------------------------------------------------------------------------------------------
    def premios_saca3():
    #Tabla para hacer print a los premios principales
    #Columnas:
        print("+------------------------------------------------------------+")
        print("|                                Premios                     |")
        print("+------------------------------------------------------------+")
        print("|            Sorteo Principal         |        Premio        |")
        print("+------------------------------------------------------------+")
    
    # Filas: 
        print("| Exacta(3 números en orden correcto) |        100,000.00    |")
        print("+------------------------------------------------------------+")
        print("|             Combinada               |         25,000.00    |")
        print("| (3 números en cualquier orden)      |                      |")
        print("+------------------------------------------------------------+")
        

     #Tabla para hacer print a los premios revancha
    #Columnas:
        print("+------------------------------------------------------------+")
        print("|                                Premios                     |")
        print("+------------------------------------------------------------+")
        print("|              Revancha              |        Premio         |")
        print("+------------------------------------------------------------+")
    
    # Filas: 
        print("| Exacta(3 números en orden correcto) |        25,000.00     |")
        print("+------------------------------------------------------------+")
        print("|             Combinada               |        12,500.00     |")
        print("| (3 números en cualquier orden)      |                      |")
        print("+------------------------------------------------------------+")
        
 #------------------------------------------------------------------------------------------------------------
 # Fin de la función de premios para Loteria      

#Funcion Secundaria para Aleatorio
#---------------------------------------------------------------------------------------------------------
    def aleatorio_loteria():
         #Variables y Listas:
         jugadas_aleatoria = []
         cantidad_jugadas = int(input("Ingrese la cantidad de jugadas a realizar: "))
         
        #Ciclo for para las jugadas aleatorias
         for j in range(cantidad_jugadas):
             jugada = random.sample(range(0, 66),6)
             print (f"Jugada {j + 1} añadida.")
             jugadas_aleatoria.append(jugada)  # Se añaden las jugadas aleatorias en una sola lista 
         boleta_total.append(jugadas_aleatoria) # Se añade a la lista de boletas total
            
         print(f"{jugadas_aleatoria}")
         print(f"{boleta_total}")
         return jugadas_aleatoria
 #------------------------------------------------------------------------------------------------------------
 # Fin de la función Aleatoria
   
#Función Secundaria para Manual
#-----------------------------------------------------------------------------------------------------------
    def manual_loteria():
        #Variables y listas
        cantidad_jugadas = int(input("Ingrese la cantidad de jugadas a realizar: "))

        jugadas = []
        while True:
            try:
                for i in range(cantidad_jugadas):
                    valores_jugadas = []
                    valores_unicos = set()
        
                    for j in range(6):
                        while True:
                            numeros = int(input(f"Ingrese un valor: {j + 1} del 0 al {66 - 1} en la jugada {i + 1}, (No se puede repetir): "))
                    
                            if 0 <=  numeros <= 65:
                                if numeros not in valores_unicos:
                                    print(f"\n El número: {numeros} fue agregado \n")
                                    valores_jugadas.append(numeros)
                                    valores_unicos.add(numeros)
                                    break  
                                else:
                                    print(f"\n No se puede repetir el valor {numeros}, por favor inténtelo de nuevo")
                            else:
                                print("\n Elegiste un número no correspondido a lo que se pide.")    
                    valores_unicos.clear()             
                    jugadas.append(valores_jugadas)
                    boleta_total.append(valores_jugadas)
                
                print(f"Boletas manuales ingresadas: {jugadas}")
                break
            except ValueError as value:
                print(f"\n Ingresaste un valor diferente a lo que se pide, por favor, inténtelo de nuevo. Error: {value} ")
    #--------------------------------------------------------------------------------------------------------------------------------------------------
    #Fin de la función Manual
    
    #Returns de la función Creación_Boletas:
    return aleatorio_loteria, manual_loteria, boleta_total, premios_loteria, premios_saca3
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Fin de la función creación de boletas de Lotería

#Creación de la función para generar sorteos
#-----------------------------------------------------------------------------------------------------
def creacion_sorteos():
    
 #Creación de la función secundaria para comparar boletas     
#------------------------------------------------------------------------------------------------------   
    #Creando funcion para comparar boletos
    def comparar_boletas(sorteo,total_boletas):

        #Búcle para la comparación de boleta
        for i, boleta in enumerate(total_boletas):
            coincidencias = set(boleta) & set(sorteo)  # Comparamos cada boleta con el sorteo
            if coincidencias:
                print(f"Boleta {i + 1}: Le pegaste a {len(coincidencias)} número(s), coincidencias: {sorted(coincidencias)}") #Compara las coindicencias
            else:
                print(f"Boleta {i + 1}: No ganó.")
#------------------------------------------------------------------------------------------------------
#fin de la función secundaria para generar sorteos para Loteria 

#Creación de la función secundaria para generar sorteos para Loteria      
#------------------------------------------------------------------------------------------------------
        
    #Creando función para generar numeros randoms para los sorteos
    def generar_sorteo_loteria():
       
        #Listas para el Sorteo:
        total_sorteos_loteria = []

        #generar numero random en sorteos
        sorteo_loteria = random.sample(range(0,66),6)
        
        total_sorteos_loteria.append(sorteo_loteria)
        return sorteo_loteria
        
        
        #Fin de generar sorteo random
#----------------------------------------------------------------------------------------------------
#Fin de la función secundaria para generar sorteos para Loteria   

#Creación de la función secundaria para generar sorteos para Saca3   
#----------------------------------------------------------------------------------------------------------------
    def generar_sorteo_saca3():

        #Listas para el Sorteo Saca 3
        total_sorteos_saca3 = []

        #generar numero random en sorteos utilizando Choises para que puedan repetirse:
        sorteo_saca3 = random.choices(range(0,9), k=3) #La k = 3 es para indicar cuantos números deberá de generar
        total_sorteos_saca3.append(sorteo_saca3)
        return sorteo_saca3

    return comparar_boletas, generar_sorteo_loteria, generar_sorteo_saca3, 
    
#----------------------------------------------------------------------------------------------------------------   
    #Manejando función para la creación de archivos
#------------------------------------------------------------------------------

file = "boletas.txt"
def crear_archivo(file):
    
    #Comenzamos el manejo de errores pero por existencia
    try: 
     with open(file, "x") :#Me ayuda crear el archivo y cerrarlo automaticamente
        print(f"Archivo {file} se creo bien")
        
    except FileExistsError:
        print("El archivo ya existe")
    
   
 #Fin de la creación        
#----------------------------------------------------------------------------

def escoger():
   try: 
    escoger = str(input("Desea continuar? De lo contrario perdería su boleta".lower())) #lo convierto en lower la contestación
                                     
    if escoger == "si":
     print("Excelente, su archivo tiene la boleta registrada")
     crear_archivo(file)
                                         
    elif escoger == "no":
     print("Muy bien, fue bueno entretenerse")
                                        
    else:
     print("Tiene un error en su contestación")
     
   except FileExistsError:
       print("Ocurrio un problema en la creación del archivo")
                                         
   except TypeError as typo:
       print(f"Parece que puso un {typo} y es (si o no)")
                                         
   except Exception as error:
       print(f"Tuviste un error {error}, arreglalo")
                                     
    
    
        
# Fin de la creación de boletas

#----------------------------------------------------------------------------------------------
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
            print(f"{"-" * 6} 1. Aleatorio")
            print(f"{"-" * 6} 2. Manual")
    #fin de funcion para creacion de boletas
#------------------------------------------------------------------------------------------
    return menu_principal, menu_juegos, menu_boletas

#Fin de la función menu    

#----------------------------------------------------------------------------------------
#Función para el programa Main
def main():
    #Referencias de funciones:
    principal, juego, boletas = menu()
    aleatorio, manual, total_boletas,premios_loteria, premios_saca3 = creacion_boletas_loteria()
    comparar, generarloteria, generarsaca3  = creacion_sorteos()
    
    while True:
        try:
            principal()
            opcion = str(input("\n Elige la opción a seleccionar: "))
           
            match opcion:

                #Lotería
                case "1":
                    # Llamando la función Limpiar_pantalla
                    limpiar_pantalla()
                    premios_loteria()
                    while True:
                        
                        # Llamando la función menu_loteria
                        juego()
                        opcion_loteria = str(input("\n Elige la opción a seleccionar: "))
                        
                        match opcion_loteria:
                            case "1":
                                '''
                                Jorge, esta parte te la dejaré a ti, lo que debes de hacer es implementar el menu donde indique si el usuario quiere jugar manual o automático.
                                Inténtalo realizarlo con un while true y con un try y except. Para implementar el menu para boletas, solo tienes que llamarla: boletas()
                                '''
                                # Llamando la función Limpiar_pantalla
                                limpiar_pantalla()
                                manual()
                                aleatorio()
                                    
                            case "2":
                                print(f"\n {"-" * 15} Sorteos {"-" * 15}\n")
                                
                                print(f"\n {"-" * 7}Comparación de Boletas: {"-" * 7}")   
                                #Llamando la función generar_boletas()
                                sorteo = generarloteria()

                                print(f"\n El sorteo es: {sorteo} \n")

                                #Llamando la función comparar_sorteos()
                                comparar(sorteo,total_boletas)
                                    
                                    
                                    
                            case "3":
                                print(f"\n {"-" * 15} Registro {"-" * 15}\n")
                                     
                                print("Le vamos a crear un archivo con las boletas\n")
                                     
                                escoger()#llamo a la función para que escoja lo que desea hacer
                                     
                            case "4":
                                print(f"{"-" * 15} Saliendo del programa... {"-" * 15}")
                                break
                            case _:
                                    print("Hubo un error al intentar seleccionar la opción deseada.")
                        
                    
                    

                #Saca 3
                case "2":
                    # Llamando la función Limpiar_pantalla
                    limpiar_pantalla()
                    print(f"\n {"-" * 15} Saca 3 {"-" * 15}\n")

                    # Llamando la función menu_saca3
                    juego()
                    opcion_saca3 = str(input("\n Elige la opción a seleccionar: "))

                    match opcion_saca3:
                        case "1":
                            # Llamando la función Limpiar_pantalla
                            limpiar_pantalla()

                            boletas()
                            opcion_boletas = str(input("\n Elige la opción a seleccionar: "))

                            match opcion_boletas:
                                case "1":
                                    
                                    # Llamando la función Limpiar_pantalla
                                    limpiar_pantalla()
                                    
                                    print(f"\n {"-" * 15} Creación de Boletas Automaticas: {"-" * 15}\n")

                                case "2":
                                    # Llamando la función Limpiar_pantalla
                                    limpiar_pantalla()

                                    print(f"\n {"-" * 15} Creación de Boletas Manuales: {"-" * 15}\n")
                                    
                                case _:
                                    print("Hubo un error al intentar seleccionar la opción deseada.")

                        case "2":

                            # Llamando la función Limpiar_pantalla
                            limpiar_pantalla()

                            print(f"\n {"-" * 15} Sorteos {"-" * 15}\n")
                                
                            print(f"\n {"-" * 7}Comparación de Boletas: {"-" * 7}")   
                            #Llamando la función generar_boletas()
                            sorteo = generarsaca3()

                            print(f"\n El sorteo es: {sorteo} \n")

                            
                            
                        case "3":
                            # Llamando la función Limpiar_pantalla
                            limpiar_pantalla()
                        case "4":
                            print(f"{"-" * 15} Saliendo del programa... {"-" * 15}")
                            break
                        case _:
                            print("Hubo un error al intentar seleccionar la opción deseada.")
                #Salir del programa
                case "3":
                    print(f"{"-" * 15} Saliendo del programa... {"-" * 15}")
                    break
                case _:
                    print("Hubo un error al intentar seleccionar la opción deseada.")
        except ValueError as value:
                print(f"\n Ingresaste un valor diferente a lo que se pide, por favor, inténtelo de nuevo. Error: {value} ")
        except Exception as error:
                            print(f"Tiene un error llamado {error}, inténtalo más tarde por favor.")
#Returns de la función main:
    
# Fin de la función Main
#--------------------------------------------------------------------------------------------
#Llamada a la función Main para que el programa empiece con dicha función
main()