#Proyecto de loteria 
#Joel Maisonet
#Christian Matias 
#Jorge Maldonado

#librerias
import random #importamos la libreria random
from files import *
from menu import *
from limpiar_pantalla import *

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

#Funcion Principal de creación de boletas
boleta_total = []
def creacion_boletas_loteria():
    

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
       boleto = int(input("¿Cuántos boletos desea?: "))
       boletas_aleatoria = [] # Lista local para almacenar las boletas generadas
       coincidencias_totales = []
        
       numero = random.sample(range(0, 66), 6)  # Genera un número aleatorio de sorteo
       print(f"El número aleatorio es: {numero}")
       for i in range(boleto):
         boleta = random.sample(range(0, 66), 6)  # Genera una nueva boleta aleatoria
         boleta_total.append(boleta)  # Agrega cada boleta al total global
         boletas_aleatoria.append(boleta)  # Agrega a la lista local
         print(f"Esta es tu boleta aleatoria: {boletas_aleatoria}")
        
        # Comparar cada boleta existente con el número aleatorio generado
       for i, boleta in enumerate(boleta_total):
            coincidencias = set(boleta) & set(numero)  # Encuentra los números en común
            coincidencias_totales.append(coincidencias)
            if coincidencias:
                print(f"Boleta {i + 1}: Le pegaste a {len(coincidencias)} número(s), coincidencias: {sorted(coincidencias)}")
            else:
                print(f"Boleta {i + 1}: No ganó.")
                 
                 
      
           # Guardar los datos en un archivo
       with open(file, "a") as archivo:
          archivo.write(f"Su boleta es: {boletas_aleatoria}\n")
          archivo.write(f"El numero del sorteo es: {numero}\n")
          archivo.write(f"Coincidencias totales: {coincidencias_totales}\n")
          archivo.write("=" * 50 + "\n")
        
     
        
        # Generar los boletos aleatorios solicitados
       
            
            
       return boleta_aleatoria
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
                
    def manual_saca3():
         cantidad_jugadas = int(input("Ingrese la cantidad de jugadas a realizar: "))

         jugadas = []
         while True:
            try:
                for i in range(cantidad_jugadas):
                    valores_jugadas = []
                    valores_unicos = set()
        
                    for j in range(3):
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
            
            
            return manual_saca3
            
    #--------------------------------------------------------------------------------------------------------------------------------------------------
    #Fin de la función Manual
    
    #Returns de la función Creación_Boletas:
    return aleatorio_loteria, manual_loteria, boleta_total, premios_loteria, premios_saca3,manual_saca3
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Fin de la función creación de boletas de Lotería

    
#generar numero random en sorteos
def generar_sorteo():
    return random.sample(range(0,66),6)
    
    #Fin de generar sorteo random
#----------------------------------------------------------------------------------------------------
            



                            #Creación de la función para generar sorteos
#-----------------------------------------------------------------------------------------------------
def creacion_sorteos():
#---------------------------------------------------------------------------------------------------
    



    #Creando función para generar numeros randoms para los sorteos
    def generar_sorteo_loteria():
       
        #Listas para el Sorteo:
        total_sorteos_loteria = []

        #generar numero random en sorteos
        sorteo_loteria = random.sample(range(0,66),6)
        
        total_sorteos_loteria.append(sorteo_loteria)
        return sorteo_loteria
        
#------------------------------------------------------------------------------------------------------
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




                              #Función para la opción 2 de generar sorteo
#-----------------------------------------------------------------------------------------------------------------
def generar_sort():
      # Generar un solo sorteo
    sorteo1 = generar_sorteo()
    sorteo2 = generar_sorteo()

    print(f"Sorteo generado: {sorteo2}")
    print(f"Sorteo generado2: {sorteo1}")
    print("\nComparación de Boleta:")

    # Generar una única boleta aleatoria
    boleta = random.sample(range(0, 66), 6)

    coincidencias = set(boleta) & set(sorteo2)  # Comparamos la boleta con el sorteo

    if coincidencias:
        print(f"Le pegaste a {len(coincidencias)} numeros coincidencias: {sorted(coincidencias)}")
    else:
        print("No ganó.")

    # Guardar los resultados en un archivo
    with open(file3, "a") as archivo:
        archivo.write(f"Tu Boleta: {boleta}\n")
        archivo.write(f"Numero del sorteo: {sorteo2}\n")
        archivo.write(f"Coincidencias: {sorted(coincidencias)}\n")
        archivo.write("=" * 50 + "\n")
#-------------------------------------------------------------------------------------------------------------




                             #Manejando función para la comparación de boletas para aleatorio
#-----------------------------------------------------------------------------------------------------------------

def comparar_boletas():

     sorteo2 = generar_sorteo()
     print(f"Sorteo generado: {sorteo2}")
     print("\nComparación de Boletas:")
    #Búcle para la comparación de boleta
     for i, boleta in enumerate(boleta_total):
        coincidencias = set(boleta) & set(sorteo2)  # Comparamos cada boleta con el sorteo
        
       
        if coincidencias:
             print(f"Boleta {i + 1}: Le pegaste a {len(coincidencias)} número(s), coincidencias: {sorted(coincidencias)}") #Compara las coindicencias
           
        else:
             print(f"Boleta {i + 1}: No ganó.")
             
        with open(file , "a") as archivo:
            archivo.write(f"su boleta es: {boleta}\n la del sorteo es: {sorteo2} \n iguales: {coincidencias}\n")
            
            archivo.write("=" * 50)
#-----------------------------------------------------------------------------------------------------------------
                                
   
                                   #Función para el case 3 de Reportes
#---------------------------------------------------------------------------------------

def escoger():
   try: 
    escoger = str(input("Desea continuar? De lo contrario perdería su boleta ".lower())) #lo convierto en lower la contestación
                                     
    if escoger == "si":
     print("Excelente, su archivo tiene la boleta registrada")
     crear_archivo(file)
     comparar_boletas()
                                         
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
                                     
 #-----------------------------------------------------------------------------------------
                            # Fin de la creación de boletas


#Fin de la función menu    

#----------------------------------------------------------------------------------------
#Función para el programa Main
def main():
    #Referencias de funciones:
    principal, juego, boletas = menu()
    aleatorio, manual, total_boletas,premios_loteria, premios_saca3, manual_saca3= creacion_boletas_loteria()
    comparar, generarloteria, generarsaca3  = creacion_sorteos()
    
    while True:
        try:
            principal()
            opcion = str(input("\n Elige la opción a seleccionar: "))
           
            match opcion:

                #Primer Case para la sección de "Lotería"
#------------------------------------------------------------------------------------------------------------------------------------------
                case "1":
                    # Llamando la función Limpiar_pantalla
                    limpiar_pantalla()
                    premios_loteria()
                    
                    
#----------------------------------------------------------------------------------------------------------------------------------------

                    #Búcle por si ocurre un error al escoger repita
#----------------------------------------------------------------------------------------------------------------------------------------
                    while True:
                        
                                                # Llamando la función menu_loteria   
                        #-----------------------------------------------------------------------------------------------------
                        
                        juego()
                        opcion_loteria = str(input("\n Elige la opción a seleccionar: "))
                        
                        
                                                        #segundo case por si marca la opción "1"
                        #------------------------------------------------------------------------------------------------------------------
                        match opcion_loteria:
                            case "1":
                                 try:
                                      boletas()
                                      choose = int(input("Escoja entre (1) o (2): "))
                                     
                                     
                                    
                                                                    
                                      """Te dejare los comentarios para el case nuevo que vayas hacer Christian (Dile a chatgpt que arrele la sintaxis)
                                      Digo que lo arregle porque al colocar el match case tendras que darle un salto a gran parte del
                                      código.
                                      """
                                                                   
                                                             #Tercer Match Case para que el usuario escoga entre aleatorio o manual
                                     #-------------------------------------------------------------------------------------------------------
                                     
                                     
                                                    #Este case se encarga de limpiar y brincar a la función de aleatorio
                                     #----------------------------------------------------------------------------------------------------------------
                                      if choose == 1:
                                         limpiar_pantalla()
                                         
                                         #Lo lleva a la función aleatorio para llevar al file los datos de la boleta aleatoria
                                         aleatorio()
                            
                                        
                                        
                                                    #Este segundo case es por si el usuario escoge la opción manual
                                    #------------------------------------------------------------------------------------------------------------------------
                                      elif choose == 2 :
                                        limpiar_pantalla()
                                        
                                        #Lo lleva a escoger los numeros que desea para subirlo a la boleta
                                        manual()
                                        
                                        #Este lo lleva a una función para generar sorteo aleatoriamente
                                        sorteo = generar_sorteo() 
                                        print(f"El sorteo es: {sorteo}")
                                        
                                        #Lo lleva a la función de comparación de boletas
                                        comparar_boletas()
                                          
                                      else:
                                         print("Opción no valida, Escoja entre (1) o (2)")
                                         
                                 except TypeError as typo:
                                       print(f"Tiene un error {typo}")
                                 break
                             #-------------------------------------------------------------------------------------------------------------------------------
                             
                             
                           
                           
                           
                                    #Este es el case para comprar boleta con revancha
                           #----------------------------------------------------------------------------------------------------------------------------------
                            case "2":
                                pass 
                            
                            
                             #Este es el tercer case del segundo match case para generar sorteo aleatoriamente
                             #--------------------------------------------------------------------------------------------------------------------------------       
                            case "3":
                                print(f"\n {"-" * 15} Generar Sorteo {"-" * 15}\n")
                                
                                
                                print(f"\n {"-" * 7}Comparación de Boletas: {"-" * 7}")   
                                #Llamando la función generar_boletas()
                                
                                
                               #Voy a la función de generar sorteo para que comparé, crea y los lleva al file
                                generar_sort()                                
                                    
                                    
                                    
                                    #Este es el cuarto case del segundo Match Case para los reportes
                            #------------------------------------------------------------------------------------------------------------------------------------
                            case "4":
                                print(f"\n {"-" * 15} Reportes {"-" * 15}\n")
                                     
                                print("Le vamos a crear un archivo con las boletas\n")
                                     
                                escoger()#llamo a la función para que escoja lo que desea hacer
                                
                                
                                
                                     #Función para salir del programa
                            #------------------------------------------------------------------------------------------------------------------------------------         
                            case "5":
                                print(f"{"-" * 15} Saliendo del programa... {"-" * 15}")
                                break
                            
                            
                            
                                    #Función por si ocurre un error, vuelva indique y vuelva a intentarlo
                            #-------------------------------------------------------------------------------------------------------------------------------------
                            case _:
                                    print("Hubo un error al intentar seleccionar la opción deseada.")
                        
                    
                    #Este es el segundo case del primer Match Case para escoger el saca 3
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
                #Saca 3
                case "2":
                    # Llamando la función Limpiar_pantalla
                    limpiar_pantalla()
                    print(f"\n {"-" * 15} Saca 3 {"-" * 15}\n")
                    
#-------------------------------------------------------------------------------------------------------------------------------------



                    # Llamando la función menu_saca3
                    juego()
                    opcion_saca3 = str(input("\n Elige la opción a seleccionar: "))
                    
                    
                    
                    
                                            #Match Case para las opciones del menu del saca 3
                    #--------------------------------------------------------------------------------------------------------------------------
                    match opcion_saca3:
                        case "1":
                            # Llamando la función Limpiar_pantalla
                            limpiar_pantalla()

                            boletas()
                            opcion_boletas = str(input("\n Elige la opción a seleccionar: "))
                            
                            
                            
                                            #Este 2 Match Case es para el manejo de opciónes para hacer la boleta manual o aleatoriamente
                        #------------------------------------------------------------------------------------------------------------------------------
                            match opcion_boletas:
                                
                                
                                            #El case 1 es para la creación de boletas automáticas
                            #-------------------------------------------------------------------------------------------------------------------------
                                case "1":
                                    
                                    # Llamando la función Limpiar_pantalla
                                    limpiar_pantalla()
                                    
                                    print(f"\n {"-" * 15} Creación de Boletas Automaticas: {"-" * 15}\n")


                                                        #Este match case es para el manejo de la boleta manual
                            #-----------------------------------------------------------------------------------------------------------------------
                                case "2":
                                    # Llamando la función Limpiar_pantalla
                                    limpiar_pantalla()

                                    print(f"\n {"-" * 15} Creación de Boletas Manuales: {"-" * 15}\n")
                                    manual_saca3()
                                    
                                    
                                    
                                                    #Este match case es si ocurre un error en la opción
                            #-------------------------------------------------------------------------------------------------------------------------
                                case _:
                                    print("Hubo un error al intentar seleccionar la opción deseada.")


                                                
                                                #Este es el segundo case para generar sorteos
                    #----------------------------------------------------------------------------------------------------------------------------------
                        
                        
                        
                               #Este es el segundo case para la boleta con revancha
                    #----------------------------------------------------------------------------------------------------------------------------------
                        case "2":
                            pass
                        
                        
                               #Este es el tercero case para generar sorteos
                    #----------------------------------------------------------------------------------------------------------------------------------
                        
                        case "3":

                            # Llamando la función Limpiar_pantalla
                            limpiar_pantalla()

                            print(f"\n {"-" * 15} Sorteos {"-" * 15}\n")
                                
                            print(f"\n {"-" * 7}Comparación de Boletas: {"-" * 7}")   
                            
                            
                            #Llamando la función generar_boletas()
                        #---------------------------------------------------------------------------------------------------------------------------------
                            sorteo = generarsaca3()

                            print(f"\n El sorteo es: {sorteo} \n")

                            
                            
                                    #Este es el cuarto match case del segundo match case para poder hacer una limpieza de pantalla
                        #-----------------------------------------------------------------------------------------------------------------------------
                        case "4":
                            # Llamando la función Limpiar_pantalla
                            limpiar_pantalla()
                            
                            
                            
                            
                            
                                        #Este es el quinto match case para el segundo match case para poder salir del programa
                    #------------------------------------------------------------------------------------------------------------------------------------
                        case "5":
                            print(f"{"-" * 15} Saliendo del programa... {"-" * 15}")
                            break
                        
                        
                        
                        
                                    #Este es por si ocurre algun problema al escoger alguna función
                    #-------------------------------------------------------------------------------------------------------------------------------------
                        case _:
                            print("Hubo un error al intentar seleccionar la opción deseada.")
                            
                            
                
                                        #Este es el tercer match case del primer match case para cerrar el programa
#--------------------------------------------------------------------------------------------------------------------------------------------------------
                case "3":
                    print(f"{"-" * 15} Saliendo del programa... {"-" * 15}")
                    break
                
                #Este es el último case para capturar algún error en la opción
#---------------------------------------------------------------------------------------------------------------------------------------------------------
                case _:
                    print("Hubo un error al intentar seleccionar la opción deseada.")
                    
                    
                    
                    #Aquí capturo los errores que salgan con tipo (ValueError) y (Exception)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
        except ValueError as value:
                print(f"\n Ingresaste un valor diferente a lo que se pide, por favor, inténtelo de nuevo. Error: {value} ")
        except Exception as error:
                            print(f"Tiene un error llamado {error}, inténtalo más tarde por favor.")
 #----------------------------------------------------------------------------------------------------------------------------------------------------------
                            
                            
#Returns de la función main:
    
# Fin de la función Main
#--------------------------------------------------------------------------------------------
#Llamada a la función Main para que el programa empiece con dicha función
main()