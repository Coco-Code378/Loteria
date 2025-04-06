
#Librerías
import random
from limpiar_pantalla import *
from files import *


   
#-------------------------------------------------------------------------------------------------------
#Funcion Principal de creación de boletas para lotería
def creacion_boletas_loteria():
   #Listas 
   global boleta_total_loteria 
   boleta_total_loteria = 0
   revanchas_loteria = []
   jugadas = []

#Funcion para incrementar el valor de boletas:
#---------------------------------------------------------------------------------------------------------

   def boleta_total():
      global boleta_total_loteria  # Permite modificar la variable externa
      boleta_total_loteria += 1 #  Suma 1 cada vez que se ejecuta
      
      total = boleta_total_loteria
      
      return total

#---------------------------------------------------------------------------------------------------------
#Final de la función para incrementar el valor de las boletas

#Funcion Secundaria para Aleatorio
#---------------------------------------------------------------------------------------------------------
   def aleatorio_loteria():
       #Variables y Listas:
       precio_jugada_loteria = 0
       precio_revancha_loteria = 0
       
      
       cantidad_jugadas = int(input("¿Cuántas jugadas desea realizar?: "))
       
    
       for jugada in range(cantidad_jugadas):
         precio_jugada_loteria += 2
         jugada = random.sample(range(0, 66), 6)  # Genera una nueva boleta aleatoria
      
         jugadas.append(jugada)  # Agrega a la lista local
         print(f"Tu jugada aleatoria: {jugada}")
         opcion = input("\n¿Deseas incluir esta jugada como revancha? (Si/No): ")
         opcion = opcion.capitalize()
         if opcion == "Si":
            precio_revancha_loteria += 1
            revanchas_loteria.append(jugada)
            print("\nLa jugada fue añadida para Revancha")
         else:
            print("\nLa jugada no fue añadida como revancha")   
        
        #Limpiar pantalla para mejor visualización
       limpiar_pantalla()
      
       precio_total = precio_jugada_loteria + precio_revancha_loteria
       print(f"\nJugadas Aleatorias ingresadas: {jugadas}")
       print(f"\nJugadas con Revancha: {revanchas_loteria}")
       print(f"\nPrecio total: ${precio_total}")        
       boleta_total()
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

        #Variable para la cantidad de jugadas
        cantidad_jugadas = int(input("Ingrese la cantidad de jugadas a realizar: "))
        
        
        while True:
            try:
               
                for i in range(cantidad_jugadas):
                    
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

                    opcion = input("¿Deseas incluir esta jugada como revancha? (Si/No): ")
                    opcion = opcion.capitalize()
                    if opcion == "Si":
                        precio_revancha_loteria += 1
                        revanchas_loteria.append(jugadas)
                        print("\nLa jugada fue añadida para Revancha")
                    else:
                        print("\nLa jugada no fue añadida como revancha")   

                    
                
                #Limpiar pantalla para mejor visualización
                limpiar_pantalla()
                
                precio_total = precio_jugada_loteria + precio_revancha_loteria
                print(f"\nJugadas manuales ingresadas: {jugadas}")
                print(f"\nJugadas con Revancha: {revanchas_loteria}")
                print(f"\nPrecio total: ${precio_total}")
                boleta_total()
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
            return boleta_total_loteria
              

#-----------------------------------------------------------------------------------------------------------------------------------------
    #Returns de la función Creación_Boletas:
   return aleatorio_loteria, manual_loteria, jugadas, revanchas_loteria, boleta_total
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Fin de la función creación de boletas de Lotería

                                            #Creación de Sorteos Loteria
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#generar numero random en sorteos
def generar_sorteo():
    return random.sample(range(0,66),6)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

                                            #Creación de Sorteos saca 3
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#generar numero random en sorteos
def generar_sorteo_saca3():
    return random.sample(range(0, 3),9)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------



#Comienzo de la función sorteo_loteria_revancha
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def sorteo_loteria_revanchas(revanchas):
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
           elif len(coincidencias) == 4:
              premio = "Felicidades, acertaste 4 números y ganaste 75,000 dólares"
           elif len(coincidencias) == 5:
              premio = "Felicidades, acertaste 5 números y ganaste 300,000 dólares"
           elif len(coincidencias) == 6:
              premio = "Felicidades, acertaste todos los números y ganaste EL MILLÓN"
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
#----------------------------------------------------------------------------------------------------------------- 
#Final de sorteo_loteria_revancha

#Comiezno de la funcion sorteo_loteria_jugadas
#----------------------------------------------------------------------------------------------------------------- 
def sorteo_loteria_jugadas(jugadas):
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
            elif len(coincidencias) == 4:
               premio = "Felicidades, acertaste 4 números y ganaste 75,000 dólares"
            elif len(coincidencias) == 5:
               premio = "Felicidades, acertaste 5 números y ganaste 300,000 dólares"
            elif len(coincidencias) == 6:
               premio = "Felicidades, acertaste todos los números y ganaste EL MILLÓN"
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

#-----------------------------------------------------------------------------------------------------------------    
#Final de la función sorteo_loteria_jugadas