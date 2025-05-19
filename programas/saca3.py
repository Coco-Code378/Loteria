import random
from limpiar import *
from files import*


   
                                                   #Bloques de Try-Except para cargar la memoria:
#------------------------------------------------------------------------------------------------------------------------------------------------
try:
   with open(".\\MemoriaSaca3\\memoria_boleta_saca3.txt", "r") as archivo:
    boleta_total_saca3 = int(archivo.read())
except FileNotFoundError:
    boleta_total_saca3 = 0


try:
   with open(".\\MemoriaSaca3\\memoria_boleta_ganadora_saca3.txt", "r") as archivo:
      contador_ganador_saca3 = int(archivo.read())
except FileNotFoundError:
      contador_ganador_saca3 = 0

try:
   with open(".\\MemoriaSaca3\\memoria_revancha_saca3.txt", "r") as archivo:
      contador_de_revanchas_saca3 = int(archivo.read())
except FileNotFoundError:
      contador_de_revanchas_saca3 = 0

try:
   with open(".\\MemoriaSaca3\\memoria_jugadas_saca3.txt", "r") as archivo:
      contador_de_jugadas_saca3 = int(archivo.read())
except FileNotFoundError:
      contador_de_jugadas_saca3 = 0

try:
   with open(".\\MemoriaSaca3\\memoria_sorteos_saca3.txt", "r") as archivo:
      contar_sorteos_saca3 = int(archivo.read())
except FileNotFoundError:
      contar_sorteos_saca3 = 0

#------------------------------------------------------------------------------------------------------------------------------------------------
#Fin de los bloques de Try-Except para cargar la memoria
   




#-------------------------------------------------------------------------------------------------------------
def creacion_boleta_saca3():

    
    jugadas = []
    revancha_saca3 = []
    
    
    
    #-----------------------------------------------------------------------------------------------------------------
    
  
    
        
    def aleatorio_saca3():
       
        #Variables y Listas:
       precio_saca3 = 0
       precio_revancha_saca3 = 0
      
       print(f"{'=' * 8} Costos: {'=' * 8}")
       print("Cada jugada cuesta $2.00")
       print("Cada revancha cuesta $1.00")
      
       cantidad_jugadas = int(input("¿Cuántas jugadas desea realizar?: "))
       
    
       for jugada in range(cantidad_jugadas):
         #Contar jugadas:
         contar_jugadas_saca3()
         
         precio_saca3 += 2
         jugada = random.randint(range(0, 9), 3)  # Genera una nueva boleta aleatoria
        
      
         jugadas.append(jugada)  # Agrega a la lista local

         #Guardar Jugada
         guardar_jugadas_saca3()

         print(f"Tu jugada aleatoria: {jugada}")

         #Opciones para implementar jugada como Revancha
         opcion = input("\n¿Deseas incluir esta jugada como revancha? (Si/No): ")
         opcion = opcion.capitalize()
         if opcion == "Si":
            precio_revancha_saca3 += 1
            revancha_saca3.append(jugada)
            print("\nLa jugada fue añadida para Revancha")

            #Contar Revanchas
            contar_revanchas_saca3()

            #Guardar Revanchas:
            guardar_jugadas_revancha_saca3()
         else:
            print("\nLa jugada no fue añadida como revancha")   
            
        
        #Limpiar pantalla para mejor visualización
       limpiar_pantalla()
       
       
       precio_total_saca3 = precio_saca3 + precio_revancha_saca3
       print(f"\nJugadas Aleatorias ingresadas: {jugadas}")
       print(f"\nJugadas con Revancha: {revancha_saca3}")
       print(f"\nPrecio total: ${precio_total_saca3}")        

       #Contar Boletas
       boleta_total()

       #Guardar Boletas
       guardar_total_boletas_saca3()
       
       try:
          with open(file2 , "a") as archivo:
             archivo.write(f"{'=' *50}\n")
             archivo.write(f"{'-' * 7} Saca 3 Boleta Aleatoria {'-' * 7}\n")
             archivo.write(f"{'=' *50}\n")
             archivo.write(f"Boleta {boleta_total_saca3}\n")
             archivo.write(f"Jugadas : {jugadas}\n" )
             archivo.write(f"Jugadas de revancha: {revancha_saca3}\n")
             archivo.write(f"Precio total ${precio_total_saca3}: \n")
             
             
             
       except FileExistsError:
          print("Lo siento pero no encontramos su archivo")
          
       except Exception as error:
          print(f"Lo siento, el archivo tuvo un problema tipo: {error}")
   
   
        
           #Función para hacer Manual saca 3               
#-----------------------------------------------------------------------------------------------------------------------------------------

    def manual_saca3():
        
        # Variables y listas
        precio_jugada_loteria = 0
        precio_revancha_saca3 = 0
        jugadas = []
        revancha_saca3 = []

        # Información sobre los costos
        print(f"{'=' * 8} Costos: {'=' * 8}")
        print("Cada jugada cuesta $2.00")
        print("Cada revancha cuesta $1.00")

        try:
            # Cantidad de jugadas a realizar
            cantidad_jugadas = int(input("Ingrese la cantidad de jugadas a realizar: "))

            for i in range(cantidad_jugadas):
                #Contar las jugadas:
                contar_jugadas_saca3()
                # Inicializar listas para la jugada actual
                precio_jugada_loteria += 2
                valores_jugadas = []
                valores_unicos = set()

                # Introducción de valores de la jugada
                print(f"\n--- Jugada {i + 1} ---")
                for j in range(3):
                    while True:
                        numeros = int(input(f"Ingrese el número {j + 1} (0-9, no se puede repetir): "))
                        if 0 <= numeros <= 9:
                            if numeros not in valores_unicos:
                                valores_jugadas.append(numeros)
                                valores_unicos.add(numeros)
                                print(f"Número {numeros} agregado correctamente.")
                                break
                            else:
                                print(f"El número {numeros} ya fue ingresado, elija otro.")
                        else:
                            print("El número debe estar entre 0 y 9.")

                jugadas.append(valores_jugadas)

                #Guardar la cantidad de jugadas:
                guardar_jugadas_saca3()

                #Opciones para implementar jugada como Revancha
                opcion = input("¿Deseas incluir esta jugada como revancha? (Si/No): ").capitalize()
                if opcion == "Si":
                    precio_revancha_saca3 += 1
                    revancha_saca3.append(valores_jugadas[:])
                    print("\nLa jugada fue añadida para Revancha")
                    
                    #Contar Revanchas
                    contar_revanchas_saca3()

                    #Guardar Revanchas:
                    guardar_jugadas_revancha_saca3()
                else:
                    print("\nLa jugada no fue añadida como revancha")   
                
            # Mostrar resultados finales
            precio_total = precio_jugada_loteria + precio_revancha_saca3
            print(f"\nJugadas manuales ingresadas: {jugadas}")
            print(f"Jugadas con revancha: {revancha_saca3}")
            print(f"Precio total: ${precio_total}")
            
            #Función para contar boletas:
            boleta_total()

            #Función para guardar boletas:
            guardar_total_boletas_saca3()



            try:
                with open(file2, "a") as archivo:
                    archivo.write(f"{'=' * 50}\n")
                    archivo.write(f"{'-' * 7} Saca 3 Boleta Manual {'-' * 7}\n")
                    archivo.write(f"{'=' * 50}\n")
                    archivo.write(f"Jugadas: {jugadas}\n")
                    archivo.write(f"Jugadas con revancha: {revancha_saca3}\n")
                    archivo.write(f"Precio total: ${precio_total}\n")
            except FileNotFoundError:
                print("Error: El archivo no fue encontrado.")
            except Exception as error:
                print(f"Error inesperado: {error}")

        except ValueError as value_error:
            print(f"Error: Valor inválido ingresado. Por favor, inténtelo de nuevo. {value_error}")
            

            
            
            
    #--------------------------------------------------------------------------------------------------------------------------------------------------
    #Fin de la función Manual
    
    return  aleatorio_saca3, manual_saca3, jugadas , revancha_saca3

#-------------------------------------------------------------------------------------------------------------


                                            #Creación de Sorteos saca 3
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#generar numero random en sorteos
def generar_sorteo_saca3():
    return random.sample(range(0, 9),3)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

                                            #Creación de Sorteos saca 3 revancha
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#generar numero random en sorteos
def generar_sorteo_saca3_revancha():
    return random.sample(range(0, 9),3)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

#Funcion para para almacenar, sumar y obtener el valor  de las boletas ganadoras:
#---------------------------------------------------------------------------------------------------------
def contador_de_ganadores_saca3():
   global contador_ganador_saca3 
   contador_ganador_saca3 += 1     

   return contador_ganador_saca3

def get_contador_de_ganadores_saca3():
   global contador_ganador_saca3
   return contador_ganador_saca3

def guardar_contador_de_ganadores_saca3():
    try:
      global contador_ganador_saca3
      memoria_boleta_ganadora = ".\\MemoriaSaca3\\memoria_boleta_ganadora_saca3.txt" 
      with open(memoria_boleta_ganadora, "w") as mb:
         mb.write(f"{contador_ganador_saca3}")
    except Exception as error:
         print(f"Error al intentar guardar en memoria: {error}")
   
    

#Fin de la funcion para para almacenar, sumar y obtener el valor  de las boletas ganadoras:
#---------------------------------------------------------------------------------------------------------

#Funciones para contar la cantidad de sorteos:
#---------------------------------------------------------------------------------------------------------

def contador_de_sorteos_saca3():
   global contar_sorteos_saca3 
   contar_sorteos_saca3 += 1

   return contar_sorteos_saca3 

def get_contador_de_sorteos_saca3():
   global contar_sorteos_saca3
   return contar_sorteos_saca3

def guardar_contador_de_sorteos_saca3():
   try:
      global contar_sorteos_saca3
      memoria_sorteos = ".\\MemoriaSaca3\\memoria_sorteos_saca3.txt"
      with open(memoria_sorteos, "w") as mb:
         mb.write(f"{contar_sorteos_saca3}")
   except Exception as error:
      print(f"Error al intentar guardar en memoria: {error}")


#---------------------------------------------------------------------------------------------------------
#Final de contadores de sorteos

#Creación de funciones para guardar en un archivo la cantidad de valores de los arreglos de jugada y revancha
#---------------------------------------------------------------------------------------------------------
def contar_jugadas_saca3():
   global contador_de_jugadas_saca3
   contador_de_jugadas_saca3 += 1

   return contador_de_jugadas_saca3

def contar_revanchas_saca3():
   global contador_de_revanchas_saca3
   contador_de_revanchas_saca3 += 1

   return contador_de_revanchas_saca3

def get_jugadas_saca3():
   global contador_de_jugadas_saca3
   return contador_de_jugadas_saca3

def get_revanchas_saca3():
   global contador_de_revanchas_saca3
   return contador_de_revanchas_saca3

def guardar_jugadas_saca3():
   
   try:
      global contador_de_jugadas_saca3
      memoria_jugada = ".\\MemoriaSaca3\\memoria_jugadas_saca3.txt"
      with open(memoria_jugada, "w") as mb:
         mb.write(f"{contador_de_jugadas_saca3}")
   except Exception as error:
      print(f"Error al intentar guardar en memoria: {error}")

def guardar_jugadas_revancha_saca3():
   
   try:
      global contador_de_revanchas_saca3
      memoria_revancha = ".\\MemoriaSaca3\\memoria_revancha_saca3.txt"
      with open(memoria_revancha, "w") as mb:
         mb.write(f"{contador_de_revanchas_saca3}")
   except Exception as error:
      print(f"Error al intentar guardar en memoria: {error}")

#---------------------------------------------------------------------------------------------------------
#Fin de la función para guardar en un archivo la cantidad de valores de los arreglos de jugada y revancha
                  #Funciones para conteos
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Funcion para almacenar, sumar y obtener el valor de las boletas.
#---------------------------------------------------------------------------------------------------------

def boleta_total():
   global boleta_total_saca3
   boleta_total_saca3 += 1 #  Suma 1 cada vez que se ejecuta
      
      
   return boleta_total_saca3

def get_boleta_total_saca3():
   global boleta_total_saca3
   return boleta_total_saca3

def guardar_total_boletas_saca3():
   try:
      global boleta_total_saca3
      memoria_boleta = ".\\MemoriaSaca3\\memoria_boleta_saca3.txt" 
      with open(memoria_boleta, "w") as mb:
         mb.write(f"{boleta_total_saca3}")
   except Exception as error:
         print(f"Error al intentar guardar en memoria: {error}")
   
   return guardar_total_boletas_saca3
#---------------------------------------------------------------------------------------------------------
#Final de la funcion para almacenar, sumar y obtener el valor de las boletas.


                                                #Esta función es la encargada de generar los premios y los sorteos
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def aleatorio_saca3_reporte(jugadas):
    #Contador de Sorteos:
    contador_de_sorteos_saca3()

    # Aquí se registran los premios (o se guardan mejor dicho)
    premio = " "
    sorteo_jugadas = generar_sorteo_saca3()  # Genera el sorteo de Saca 3
    
    print(f"Sorteo generado: {sorteo_jugadas}")
    
    # Preguntar al jugador si desea jugar exacta o combinada
    modo = input("¿Desea jugar Exacta o Combinada? (Escriba 'Exacta' o 'Combinada'): ").lower()
    
    # Validar elección
    while modo not in ["exacta", "combinada"]:
        print("Por favor, elija entre 'Exacta' o 'Combinada'.")
        modo = input("¿Desea jugar Exacta o Combinada? (Escriba 'Exacta' o 'Combinada'): ").lower()
    
    print("\nComparación de Boletas:")
    
    # Bucle para la comparación de boletas
    for i, boleta in enumerate(jugadas):
        coincidencias = set(boleta) & set(sorteo_jugadas)  # Coincidencias sin importar el orden
        es_exacta = boleta == sorteo_jugadas  # Coincidencia exacta
        
        if modo == "exacta":
            # Procesar como jugada exacta
            if es_exacta:
                print(f"Su jugada es: {jugadas} y la del sorteos es: {sorteo_jugadas}")
                print(f"Jugada {i + 1}: Felicidades, acertaste el orden que era.")
                premio = "Felicidades, ganaste los $100,000 dólares"

                #Contador de ganadores:
                contador_de_ganadores_saca3()

                #Guardar contador de ganador
                guardar_contador_de_ganadores_saca3()
            else:
                print(f"Su jugada es: {jugadas} y la del sorteo es: {sorteo_jugadas}")
                print(f"Jugada {i + 1}: No fue una jugada exacta.")
                premio = "Sin premio."
        
        elif modo == "combinada":
            # Procesar como jugada combinada
           if coincidencias:
             print(f"Jugada {i + 1}: Le pegaste a {len(coincidencias)} numero(s), coincidencias: {sorted(coincidencias)}")
        
        # Evaluar el número de coincidencias y asignar premio
             if len(coincidencias) == 3:
               premio = "Felicidades, acertaste los 3 numeros, ganaste 25,000.00"

               #Contador de ganadores:
               contador_de_ganadores_saca3()

               #Guardar contador de ganador
               guardar_contador_de_ganadores_saca3()
             elif len(coincidencias) == 2:
              premio = "Acertaste 2 numeros. Buen intento, sigue participando."

             elif len(coincidencias) == 1:
              premio = "Acertaste 1 numero. Mas suerte la proxima vez."
             else:
              premio = "No alcanzaste el premio, pero sigue intentándolo."
              
        else:
         print(f"Jugada {i + 1}: No hubo coincidencias.")
         premio = "Sin premio esta vez."



        
        # Guardar los datos de la jugada en el archivo
        try:
          with open(file2, "a") as archivo:
            archivo.write(f'{"=" * 50}\n')
            archivo.write(f"{'-' * 7}Su boleta es: {boleta} {'-' * 7}\n")
            archivo.write(f" {'=' * 50}\n" )
            archivo.write(f"La del sorteo es: {sorteo_jugadas}\n")
            archivo.write(f"Iguales: {sorted(coincidencias) if coincidencias else 'Ninguna'}\n")
            archivo.write(f"Su premio es: {premio}\n")
            archivo.write("=" * 50 + "\n")

        except FileNotFoundError:
            print("Error: El archivo no fue encontrado.")
        except Exception as e:
            print(f"Error: {e}")

    #Guardar sorteos en archivo
    guardar_contador_de_sorteos_saca3()
              
#--------------------------------------------------------------------------------------------------------------------------------------------------------

                             #Esta función es la encargada de generar los premios y los sorteos de la revancha
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def sorteo_saca3_revanchas(revanchas):
    #Contador de Sorteos:
    contador_de_sorteos_saca3()

    # Aquí se registran los premios
    premio = " "
    sorteo_revanchas = generar_sorteo_saca3()  # Genera el sorteo de revanchas
    
    print(f"Saca 3 Sorteo Revanchas")
    
    # Guardar los datos del sorteo en el archivo
    with open(file2, "a") as archivo:
        archivo.write(f"{'=' * 50}\n")
        archivo.write(f"{'-' * 7} Saca 3 Sorteo {'-' * 7}\n")
        archivo.write(f"El sorteo generado es: {sorteo_revanchas}\n")
        archivo.write(f"{'=' * 50}\n")
    
    print("\nComparación de Boletas Revancha:")
    
    # Preguntar al usuario si desea jugar Exacta o Combinada
    modo = input("¿Desea jugar Exacta o Combinada? (Escriba 'Exacta' o 'Combinada'): ").lower()
    
    # Validar la elección del jugador
    while modo not in ["exacta", "combinada"]:
        print("Por favor, elija entre 'Exacta' o 'Combinada'.")
        modo = input("¿Desea jugar Exacta o Combinada? (Escriba 'Exacta' o 'Combinada'): ").lower()
    
    print("\nComparación de Boletas:")
    
    # Bucle para la comparación de boletas
    for i, boleta in enumerate(revanchas):
        coincidencias = set(boleta) & set(sorteo_revanchas)  # Coincidencias sin importar el orden
        es_exacta = boleta == sorteo_revanchas  # Coincidencia exacta
        
        if modo == "exacta":
            # Procesar como jugada exacta
            if es_exacta:
                print(f"Su jugada es: {boleta} y la del sorteo es: {sorteo_revanchas}")
                print(f"Jugada {i + 1}: Felicidades, acertaste el orden que era.")
                premio = "Felicidades, ganaste los $25,000.00 dólares"

                #Contador de ganadores:
                contador_de_ganadores_saca3()

                #Guardar contador de ganador
                guardar_contador_de_ganadores_saca3()
            else:
                print(f"Su jugada es: {boleta} y la del sorteo es: {sorteo_revanchas}")
                print(f"Jugada {i + 1}: No fue una jugada exacta.")
                premio = "Sin premio."
        elif modo == "combinada":
            # Procesar como jugada combinada
            if coincidencias:
                print(f"Jugada {i + 1}: Le pegaste a {len(coincidencias)} número(s), coincidencias: {sorted(coincidencias)}")
                
                # Evaluar el número de coincidencias y asignar premio
                if len(coincidencias) == 3:
                    premio = "Felicidades, acertaste los 3 números, ganaste $12,500.00"
                    #Contador de ganadores:
                    contador_de_ganadores_saca3()

                    #Guardar contador de ganador
                    guardar_contador_de_ganadores_saca3()
                elif len(coincidencias) == 2:
                    premio = "Acertaste 2 números. Buen intento, sigue participando."
                elif len(coincidencias) == 1:
                    premio = "Acertaste 1 número. Más suerte la próxima vez."
                else:
                    premio = "No alcanzaste el premio, pero sigue intentándolo."
            else:
                print(f"Jugada {i + 1}: No hubo coincidencias.")
                premio = "Sin premio esta vez."
        
        # Escribir los resultados en el archivo
        with open(file2, "a") as archivo:
            archivo.write(f"Su boleta es: {boleta}\n")
            archivo.write(f"La del sorteo es: {sorteo_revanchas}\n")
            archivo.write(f"Iguales: {sorted(coincidencias) if coincidencias else 'Ninguna'}\n")
            archivo.write(f"Su premio es: {premio}\n")
            archivo.write("=" * 50 + "\n")

    #Guardar sorteos en archivo
    guardar_contador_de_sorteos_saca3()

#----------------------------------------------------------------------------------------------------------------- 
                                #Final de sorteo_saca 3 Revancha
                                
                                
