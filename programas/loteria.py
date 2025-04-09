
#Librerías
import random
from limpiar import *
from files import *


                                                   #Bloques de Try-Except para cargar la memoria:
#------------------------------------------------------------------------------------------------------------------------------------------------
try:
   with open(".\\MemoriaLoteria\\memoria_boleta.txt", "r") as archivo:
    boleta_total_loteria = int(archivo.read())
except FileNotFoundError:
    boleta_total_loteria = 0


try:
   with open(".\\MemoriaLoteria\\memoria_boleta_ganadora.txt", "r") as archivo:
      contador_ganador = int(archivo.read())
except FileNotFoundError:
      contador_ganador = 0

try:
   with open(".\\MemoriaLoteria\\memoria_revancha.txt", "r") as archivo:
      contador_de_revanchas = int(archivo.read())
except FileNotFoundError:
      contador_de_revanchas = 0

try:
   with open(".\\MemoriaLoteria\\memoria_jugadas.txt", "r") as archivo:
      contador_de_jugadas = int(archivo.read())
except FileNotFoundError:
      contador_de_jugadas = 0

try:
   with open(".\\MemoriaLoteria\\memoria.sorteos.txt", "r") as archivo:
      contar_sorteos = int(archivo.read())
except FileNotFoundError:
      contar_sorteos = 0

#------------------------------------------------------------------------------------------------------------------------------------------------
#Fin de los bloques de Try-Except para cargar la memoria

#----------------------------------------------------------------------------------------------------------------------------------------------------
#Funcion Principal de creación de boletas para lotería
def creacion_boletas_loteria():
   #Listas y Variables 
   revanchas_loteria = []
   jugadas = []



#Funcion Secundaria para Aleatorio
#---------------------------------------------------------------------------------------------------------
   def aleatorio_loteria():
       #Variables y Listas:
       precio_jugada_loteria = 0
       precio_revancha_loteria = 0
       
      
       contador_jugadas = int(input("¿Cuántas jugadas desea realizar?: "))
       
    
       for jugada in range(contador_jugadas):
         precio_jugada_loteria += 2
         jugada = random.sample(range(0, 66), 6)  # Genera una nueva boleta aleatoria

         jugadas.append(jugada)  # Agrega a la lista local
         print(f"Tu jugada aleatoria: {jugada}")

         contar_jugadas()

         #Función para guardar la cantidad de jugadas en un archivo:
         guardar_jugadas()

        #Ingresando la opción para incluir las jugadas como revancha:
         opcion = input("¿Deseas incluir esta jugada como revancha? (Si/No): ")
         opcion = opcion.capitalize()
         if opcion == "Si":
            precio_revancha_loteria += 1
            revanchas_loteria.append(jugadas)

            #Contador de revanchas
            contar_revanchas()

            #Guardar las cantidad de jugadas en el archivo:
            guardar_jugadas_revancha()

            print("\nLa jugada fue añadida para Revancha")
         else:
            print("\nLa jugada no fue añadida como revancha")      

          
        
        #Limpiar pantalla para mejor visualización
       limpiar_pantalla()
     
       #prints
       precio_total = precio_jugada_loteria + precio_revancha_loteria
       print(f"\nJugadas Aleatorias ingresadas: {jugadas}")
       print(f"\nJugadas con Revancha: {revanchas_loteria}")
       print(f"\nPrecio total: ${precio_total}")        

       #Función para conteo de boletas totales
       boleta_total()
       
       #Función para guardar el total de boletas en un archivo
       guardar_total_boletas()

       
       try:
          with open(file , "a") as archivo:
             archivo.write(f"{'=' *50}\n")
             archivo.write(f"{'-' * 7} Boleta aleatoria {'-' * 7}\n")
             archivo.write(f"{'=' *50}\n")
             archivo.write(f"Boleta {boleta_total_loteria}\n")
             archivo.write(f"Jugadas : {jugadas}\n" )
             archivo.write(f"Jugadas de revancha: {revanchas_loteria}\n")
             archivo.write(f"Precio total ${precio_total}: \n")
             
             
             
       except FileExistsError:
          print("Lo siento pero no encontramos su archivo")
          
       except Exception as error:
          print(f"Lo siento, el archivo tuvo un problema tipo: {error}")
   
          

               
    
 #------------------------------------------------------------------------------------------------------------
 # Fin de la función Aleatoria
 
        
        
                                              
                    	#Función Secundaria para Manual Loteria
#-----------------------------------------------------------------------------------------------------------
   def manual_loteria(): 
        #Variables y listas
        precio_jugada_loteria = 0
        precio_revancha_loteria = 0
        
        #Prints 
        print(f"{"=" * 8} Costos: {"=" * 8}")
        print(f"Cada jugada cuesta $2.00")
        print(f"Cada revancha cuesta $1.00")

        #Variable para la cantidad_jugadas de jugadas
        contador_jugadas = int(input("Ingrese la cantidad_jugadas de jugadas a realizar: "))
        
        
        while True:
            try:
               
                for i in range(contador_jugadas):
                    contar_jugadas()
                    #Listas inicializadas en el For
                    precio_jugada_loteria += 2
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

                    #Ingresando y limpiando las listas
                    valores_unicos.clear()             
                    jugadas.append(valores_jugadas)

                    #Función para guardar la cantidad de jugadas en un archivo:
                    guardar_jugadas()
                    
                    #Ingresando la opción para incluir las jugadas como revancha:
                    opcion = input("¿Deseas incluir esta jugada como revancha? (Si/No): ")
                    opcion = opcion.capitalize()
                    if opcion == "Si":
                        precio_revancha_loteria += 1
                        revanchas_loteria.append(valores_jugadas[:])

                        #Contador de revanchas:
                        contar_revanchas()

                        #Guardar las cantidad de jugadas en el archivo:
                        guardar_jugadas_revancha()

                        print("\nLa jugada fue añadida para Revancha")
                    else:
                        print("\nLa jugada no fue añadida como revancha")   


                #Limpiar pantalla para mejor visualización
                limpiar_pantalla()
                
                #Prints
                precio_total = precio_jugada_loteria + precio_revancha_loteria
                print(f"\nJugadas manuales ingresadas: {jugadas}")
                print(f"\nJugadas con Revancha: {revanchas_loteria}")
                print(f"\nPrecio total: ${precio_total}")

                #Función para el conteo de boletas
                boleta_total()

                #Función para guardar en un archivo el total de boletas
                guardar_total_boletas()

                

                try:
                 with open(file , "a") as archivo:
                  archivo.write(f"{'=' *50}\n")
                  archivo.write(f"{'-' * 7} Boleta Manual {'-' * 7}\n")
                  archivo.write(f"{'=' *50}\n")
                  archivo.write(f"Boleta {boleta_total_loteria}\n")
                  archivo.write(f"Jugadas : {jugadas}\n" )
                  archivo.write(f"Jugadas de revancha: {revanchas_loteria}\n")
                  archivo.write(f"Precio total ${precio_total}: \n")
             
             
             
                except FileExistsError:
                 print("Lo siento pero no encontramos su archivo")
          
                except Exception as error:
                 print(f"Lo siento, el archivo tuvo un problema tipo: {error}")
                
                
                
            except ValueError as value:
                print(f"\n Ingresaste un valor diferente a lo que se pide, por favor, inténtelo de nuevo. Error: {value} ")
         #Cerrando el ciclo While True
           

   
#-----------------------------------------------------------------------------------------------------------------------------------------
    #Returns de la función Creación_Boletas:
   return aleatorio_loteria, manual_loteria, jugadas, revanchas_loteria
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Fin de la función creación de boletas de Lotería

                                       #Funciones para conteos
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Funcion para almacenar, sumar y obtener el valor de las boletas.
#---------------------------------------------------------------------------------------------------------

def boleta_total():
   global boleta_total_loteria
   boleta_total_loteria += 1 #  Suma 1 cada vez que se ejecuta
      
      
   return boleta_total_loteria

def get_boleta_total():
   global boleta_total_loteria
   return boleta_total_loteria

def guardar_total_boletas():
   try:
      global boleta_total_loteria
      memoria_boleta = ".\\MemoriaLoteria\\memoria_boleta.txt" 
      with open(memoria_boleta, "w") as mb:
         mb.write(f"{boleta_total_loteria}")
   except Exception as error:
         print(f"Error al intentar guardar en memoria: {error}")
   
   return guardar_total_boletas
#---------------------------------------------------------------------------------------------------------
#Final de la funcion para almacenar, sumar y obtener el valor de las boletas.

#Funcion para para almacenar, sumar y obtener el valor  de las boletas ganadoras:
#---------------------------------------------------------------------------------------------------------
def contador_de_ganadores():
   global contador_ganador 
   contador_ganador += 1     

   return contador_ganador

def get_contador_de_ganadores():
   global contador_ganador
   return contador_ganador

def guardar_contador_de_ganadores():
    try:
      global contador_ganador
      memoria_boleta_ganadora = ".\\MemoriaLoteria\\memoria_boleta_ganadora.txt" 
      with open(memoria_boleta_ganadora, "w") as mb:
         mb.write(f"{contador_ganador}")
    except Exception as error:
         print(f"Error al intentar guardar en memoria: {error}")
   
    

#Fin de la funcion para para almacenar, sumar y obtener el valor  de las boletas ganadoras:
#---------------------------------------------------------------------------------------------------------

#Funciones para contar la cantidad de sorteos:
#---------------------------------------------------------------------------------------------------------

def contador_de_sorteos():
   global contar_sorteos 
   contar_sorteos += 1

   return contar_sorteos 

def get_contador_de_sorteos():
   global contar_sorteos
   return contar_sorteos

def guardar_contador_de_sorteos():
   try:
      global contar_sorteos
      memoria_sorteos = ".\\MemoriaLoteria\\memoria_sorteos.txt"
      with open(memoria_sorteos, "w") as mb:
         mb.write(f"{contar_sorteos}")
   except Exception as error:
      print(f"Error al intentar guardar en memoria: {error}")


#---------------------------------------------------------------------------------------------------------
#Final de contadores de sorteos

#Creación de funciones para guardar en un archivo la cantidad de valores de los arreglos de jugada y revancha
#---------------------------------------------------------------------------------------------------------
def contar_jugadas():
   global contador_de_jugadas
   contador_de_jugadas += 1

   return contador_de_jugadas

def contar_revanchas():
   global contador_de_revanchas
   contador_de_revanchas += 1

   return contador_de_revanchas

def get_jugadas():
   global contador_de_jugadas
   return contador_de_jugadas

def get_revanchas():
   global contador_de_revanchas
   return contador_de_revanchas

def guardar_jugadas():
   
   try:
      global contador_de_jugadas
      memoria_jugada = ".\\MemoriaLoteria\\memoria_jugadas.txt"
      with open(memoria_jugada, "w") as mb:
         mb.write(f"{contador_de_jugadas}")
   except Exception as error:
      print(f"Error al intentar guardar en memoria: {error}")

def guardar_jugadas_revancha():
   
   try:
      global contador_de_revanchas
      memoria_revancha = ".\\MemoriaLoteria\\memoria_revancha.txt"
      with open(memoria_revancha, "w") as mb:
         mb.write(f"{contador_de_revanchas}")
   except Exception as error:
      print(f"Error al intentar guardar en memoria: {error}")

#---------------------------------------------------------------------------------------------------------
#Fin de la función para guardar en un archivo la cantidad de valores de los arreglos de jugada y revancha

                                            #Creación de Sorteos Loteria
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#generar numero random en sorteos
def generar_sorteo():
    return random.sample(range(0,66),6)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

#Comienzo de la función sorteo_loteria_revancha
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def sorteo_loteria_revanchas(revanchas):
    #Función para contar los sorteos 
    contador_de_sorteos()

    premio = " "
    sorteo_revanchas = generar_sorteo()
    print(f"Sorteo generado: {sorteo_revanchas}")
    

     
    with open(file , "a") as archivo:
       archivo.write(f"{'=' * 50}\n")
       archivo.write(f"{'-' * 7 } Generar sorteo {'-' * 7}\n ")
       archivo.write(f"El sorteo generado es: {sorteo_revanchas}\n")
       archivo.write(f"{'=' * 50}\n")
       
    print("\nComparación de Boletas:")
    #Búcle para la comparación de boleta
    for i, boleta in enumerate(revanchas):
       coincidencias = set(boleta) & set(sorteo_revanchas)  # Comparamos cada boleta con el sorteo
        
       
       if coincidencias:
           print(f"Jugada {i + 1}: Le pegaste a {len(coincidencias)} número(s), coincidencias: {sorted(coincidencias)}")

           if len(coincidencias) == 3:
              premio = "Felicidades, acertaste 3 números y ganaste un boleto gratis"

              #Función para contar los ganadores
              contador_de_ganadores()

              #Función para guardar los valores del conteo:
              guardar_contador_de_ganadores()
              
           elif len(coincidencias) == 4:
              premio = "Felicidades, acertaste 4 números y ganaste 75,000 dólares"

              #Función para contar los ganadores
              contador_de_ganadores()

              #Función para guardar los valores del conteo:
              guardar_contador_de_ganadores()

           elif len(coincidencias) == 5:
              premio = "Felicidades, acertaste 5 números y ganaste 300,000 dólares"

              #Función para contar los ganadores
              contador_de_ganadores()

              #Función para guardar los valores del conteo:
              guardar_contador_de_ganadores()
           elif len(coincidencias) == 6:
              premio = "Felicidades, acertaste todos los números y ganaste EL MILLÓN"

              #Función para contar los ganadores
              contador_de_ganadores()

              #Función para guardar los valores del conteo:
              guardar_contador_de_ganadores()
           elif len(coincidencias) <= 2:
              print(f"La jugada {i + 1} no ganó.")
              
              premio = "No pudo ganar ningun premio"
       else:
           print(f"La jugada {i + 1} no ganó.")
           premio = "No pudo ganar ningun premio"

           with open(file , "a") as archivo:
            archivo.write(f"su boleta es: {boleta}\n la del sorteo es: {sorteo_revanchas} \n iguales: {coincidencias}\n")
            archivo.write(f"Su premio es {premio}")
            archivo.write("=" * 50)

       #Función para guardar en archivo los conteos de sorteos
       guardar_contador_de_sorteos()
    return contador_ganador
    
#----------------------------------------------------------------------------------------------------------------- 
#Final de sorteo_loteria_revancha

#Comiezno de la funcion sorteo_loteria_jugadas
#----------------------------------------------------------------------------------------------------------------- 
def sorteo_loteria_jugadas(jugadas):
     #Función para contar los sorteos 
     contador_de_sorteos()

     premio = " "
     sorteo_jugadas = generar_sorteo()
     print(f"Sorteo generado: {sorteo_jugadas}")
       
    
     
     with open(file , "a") as archivo:
       archivo.write(f"{'=' * 50}\n")
       archivo.write(f"{'-' * 7 } Generar sorteo {'-' * 7}\n ")
       archivo.write(f"El sorteo generado es: {sorteo_jugadas}\n")
       archivo.write(f"{'=' * 50}\n")
       

     

     print("\nComparación de Boletas:")
    #Búcle para la comparación de boleta
     for i, boleta in enumerate(jugadas):
        coincidencias = set(boleta) & set(sorteo_jugadas)  # Comparamos cada boleta con el sorteo
        
       
        if coincidencias:
            print(f"Jugada {i + 1}: Le pegaste a {len(coincidencias)} número(s), coincidencias: {sorted(coincidencias)}")

            if len(coincidencias) == 3:
               premio = "Felicidades, acertaste 3 números y ganaste un boleto gratis"


               #Función para contar los ganadores
               contador_de_ganadores()

              #Función para guardar los valores del conteo:
               guardar_contador_de_ganadores()
            elif len(coincidencias) == 4:
               premio = "Felicidades, acertaste 4 números y ganaste 75,000 dólares"

               #Función para contar los ganadores
               contador_de_ganadores()

               #Función para guardar los valores del conteo:
               guardar_contador_de_ganadores()

            elif len(coincidencias) == 5:
               premio = "Felicidades, acertaste 5 números y ganaste 300,000 dólares"

               #Función para contar los ganadores
               contador_de_ganadores()

               #Función para guardar los valores del conteo:
               guardar_contador_de_ganadores()

            elif len(coincidencias) == 6:
               premio = "Felicidades, acertaste todos los números y ganaste EL MILLÓN"

               #Función para contar los ganadores
               contador_de_ganadores()

               #Función para guardar los valores del conteo:
               guardar_contador_de_ganadores()

            elif len(coincidencias) <= 2:
                print(f"La jugada {i + 1} no ganó.")
                premio = "No pudo ganar ningun premio"

            else:
                print(f"La jugada {i + 1} no ganó.")
                premio = "No pudo ganar ningun premio"
        else:
           print(f"La jugada {i + 1} no ganó.")
           premio = "No pudo ganar ningun premio"
           

        try:
            with open(file, "a") as archivo:
                archivo.write(f"Boleta {i + 1}: {boleta}\n")
                archivo.write(f"Sorteo generado: {sorteo_jugadas}\n")
                archivo.write(f"Coincidencias: {sorted(coincidencias)}\n")
                archivo.write(f"Premio: {premio}\n")
                archivo.write("=" * 50 + "\n")
        except FileNotFoundError:
            print("Error: El archivo no fue encontrado.")
        except Exception as e:
            print(f"Error: {e}")

     #Función para guardar en archivo los conteos de sorteos
        guardar_contador_de_sorteos()
      

#-----------------------------------------------------------------------------------------------------------------    
#Final de la función sorteo_loteria_jugadas



