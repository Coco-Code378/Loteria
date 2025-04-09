import random
from limpiar import *
from files import*


   
   




#-------------------------------------------------------------------------------------------------------------
def creacion_boleta_saca3():

    #Creación de boletas para Saca3
    global boleta_total_saca3
    boleta_total_saca3 = 0
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
         precio_saca3 += 2
         jugada = random.sample(range(0, 9), 3)  # Genera una nueva boleta aleatoria
         jugada_revancha = random.sample(range(0,9) , 3)
      
         jugadas.append(jugada)  # Agrega a la lista local
         print(f"Tu jugada aleatoria: {jugada}")
         opcion = input("\n¿Deseas incluir esta jugada como revancha? (Si/No): ")
         opcion = opcion.capitalize()
         if opcion == "Si":
            precio_revancha_saca3 += 1
            revancha_saca3.append(jugada_revancha)
            print("\nLa jugada fue añadida para Revancha")
         else:
            print("\nLa jugada no fue añadida como revancha")   
            
        
        #Limpiar pantalla para mejor visualización
       limpiar_pantalla()
       
       
       precio_total_saca3 = precio_saca3 + precio_revancha_saca3
       print(f"\nJugadas Aleatorias ingresadas: {jugadas}")
       print(f"\nJugadas con Revancha: {revancha_saca3}")
       print(f"\nPrecio total: ${precio_total_saca3}")        
       boleta_total_revancha()
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
            # Opcional: Revancha
            opcion = input("¿Deseas incluir esta jugada como revancha? (Si/No): ").capitalize()
            if opcion == "Si":
              precio_revancha_saca3 += 1
              revancha_saca3.append(jugadas)
              print("\nLa jugada fue añadida para Revancha")
            else:
              print("\nLa jugada no fue añadida como revancha")   
             
        # Mostrar resultados finales
        precio_total = precio_jugada_loteria + precio_revancha_saca3
        print(f"\nJugadas manuales ingresadas: {jugadas}")
        print(f"Jugadas con revancha: {revancha_saca3}")
        print(f"Precio total: ${precio_total}")
        boleta_total_revancha()
        aleatorio_saca3_reporte(jugadas)
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
        
    def boleta_total_revancha():
      global boleta_total_saca3 # Permite modificar la variable externa
      boleta_total_saca3 += 1 #  Suma 1 cada vez que se ejecuta
      
      total = boleta_total_saca3
      
      return total
            
            
            
    #--------------------------------------------------------------------------------------------------------------------------------------------------
    #Fin de la función Manual
    
    return  aleatorio_saca3, manual_saca3, boleta_total_revancha , jugadas , revancha_saca3

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



                                                #Esta función es la encargada de generar los premios y los sorteos
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def aleatorio_saca3_reporte(jugadas):
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
               premio = "Felicidades, acertaste los 3 numeros y ganaste un boleto gratis"
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

              
#--------------------------------------------------------------------------------------------------------------------------------------------------------



                             #Esta función es la encargada de generar los premios y los sorteos de la revancha
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def sorteo_saca3_revanchas(revanchas):
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
                premio = "Felicidades, ganaste los $100,000 dólares"
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
                    premio = "Felicidades, acertaste los 3 números y ganaste un boleto gratis"
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


#----------------------------------------------------------------------------------------------------------------- 
                                #Final de sorteo_saca 3 Revancha
                                
                                
