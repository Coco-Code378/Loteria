import random
from limpiar_pantalla import *
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
      
       
      
       cantidad_jugadas = int(input("¿Cuántas jugadas desea realizar?: "))
       
    
       for jugada in range(cantidad_jugadas):
         precio_saca3 += 2
         jugada = random.sample(range(0, 9), 3)  # Genera una nueva boleta aleatoria
      
         jugadas.append(jugada)  # Agrega a la lista local
         print(f"Tu jugada aleatoria: {jugada}")
         opcion = input("\n¿Deseas incluir esta jugada como revancha? (Si/No): ")
         opcion = opcion.capitalize()
         if opcion == "Si":
            precio_revancha_saca3 += 1
            revancha_saca3.append(jugada)
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
                        revancha_saca3.append(jugadas)
                        print("\nLa jugada fue añadida para Revancha")
                    else:
                        print("\nLa jugada no fue añadida como revancha")   

                    
                
                #Limpiar pantalla para mejor visualización
                limpiar_pantalla()
                
                precio_total = precio_jugada_loteria + precio_revancha_loteria
                print(f"\nJugadas manuales ingresadas: {jugadas}")
                print(f"\nJugadas con Revancha: {revancha_saca3}")
                print(f"\nPrecio total: ${precio_total}")
                boleta_total_revancha()
                try:
                 with open(file2 , "a") as archivo:
                  archivo.write(f"{'=' *50}\n")
                  archivo.write(f"{'-' * 7} Saca 3 Boleta Manual {'-' * 7}\n")
                  archivo.write(f"{'=' *50}\n")
                  archivo.write(f"Boleta {boleta_total_saca3}\n")
                  archivo.write(f"Jugadas : {jugadas}\n" )
                  archivo.write(f"Jugadas de revancha: {revancha_saca3}\n")
                  archivo.write(f"Precio total ${precio_total}: \n")
             
             
             
                except FileExistsError:
                 print("Lo siento pero no encontramos su archivo")
          
                except Exception as error:
                 print(f"Lo siento, el archivo tuvo un problema tipo: {error}")
                
                
                
            except ValueError as value:
                print(f"\n Ingresaste un valor diferente a lo que se pide, por favor, inténtelo de nuevo. Error: {value} ")
         #Cerrando el ciclo While True
        
        
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



                                                #Esta función es la encargada de generar los premios y los sorteos
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def aleatorio_saca3_reporte(jugadas):
    
    #Aquí se registran los premios (o se guardan mejor dicho)
     premio = " "
     sorteo_jugadas = generar_sorteo_saca3()
     
     
     
     print(f"Sorteo generado: {sorteo_jugadas}")
     #Guardo los datos en el file
     with open(file2 , "a") as archivo:
       archivo.write(f"{'=' * 50}\n")
       archivo.write(f"{'-' * 7 } Generar sorteo {'-' * 7}\n ")
       archivo.write(f"El sorteo generado es: {sorteo_jugadas}\n")
       archivo.write(f"{'=' * 50}\n")
       
     print("\nComparación de Boletas:")
    #Búcle para la comparación de boleta
     for i, boleta in enumerate(jugadas):
        coincidencias = set(boleta) & set(sorteo_jugadas)  # Comparamos cada boleta con el sorteo
        
       #Aquí verán los premios que se harán a los que acierten
        if coincidencias:
            print(f"Jugada {i + 1}: Le pegaste a {len(coincidencias)} número(s), coincidencias: {sorted(coincidencias)}")

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
                    else:
                         print(f"La jugada {i + 1} no ganó.")
                         premio = "No pudo ganar ningun premio"
                        
                        
            else:
             print(f"Boleta {i + 1}: No ganó.")

            #Aquí guardará lo que gano
            try:
             with open(file2, "a") as archivo:
                archivo.write(f"Boleta {i + 1}: {boleta}\n")
                archivo.write(f"Sorteo generado: {sorteo_jugadas}\n")
                archivo.write(f"Coincidencias: {sorted(coincidencias)}\n")
                archivo.write(f"Premio: {premio}\n")
                archivo.write("=" * 50 + "\n")
            except FileNotFoundError:
              print("Error: El archivo no fue encontrado.")
            except Exception as e:
              print(f"Error: {e}")
              
#--------------------------------------------------------------------------------------------------------------------------------------------------------



                             #Esta función es la encargada de generar los premios y los sorteos de la revancha
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def sorteo_saca3_revanchas(revanchas):
     #Aquí se registran los premios (o se guardan mejor dicho)
     premio = " "
     sorteo_revanchas = generar_sorteo_saca3()
     
     
     print(f"Saca 3 Sorteo Revanchas")  

     with open(file2, "a") as archivo:
         archivo.write(f"{'=' * 50}\n")
         archivo.write(f"{'-' * 7} Saca 3 Sorteo {'-' * 7}\n")
         archivo.write(f"El sorteo generado es: {sorteo_revanchas}\n")
         archivo.write(f"{'=' * 50}\n")

     print("\nComparación de Boletas Revancha:")

    # Bucle para la comparación de boletas
     for i, boleta in enumerate(revanchas):
         coincidencias = set(boleta) & set(sorteo_revanchas)
         
          
       #Aquí verán los premios que se harán a los que acierten
         if coincidencias:
             print(f"Jugada {i + 1}: Le pegaste a {len(coincidencias)} número(s), coincidencias: {sorted(coincidencias)}")

             if len(coincidencias) == 3:
                premio = "Felicidades, acertaste 3 números y ganaste un boleto gratis"
             elif len(coincidencias) == 2:
                premio = "Acertaste 2 números. ¡Casi lo logras!"
             elif len(coincidencias) == 1:
                premio = "Acertaste 1 número"
             else:
                premio = "No pudo ganar ningún premio"
         else:
             print(f"Jugada {i + 1}: No ganó.")
             premio = "No pudo ganar ningún premio"
             coincidencias = set()
             
               
        # Escribimos resultado en el archivo
         with open(file2, "a") as archivo:
             archivo.write(f"Su boleta es: {boleta}\n")
             archivo.write(f"La del sorteo es: {sorteo_revanchas}\n")
             archivo.write(f"Iguales: {sorted(coincidencias)}\n")
             archivo.write(f"Su premio es: {premio}\n")
             archivo.write("=" * 50 + "\n")


#----------------------------------------------------------------------------------------------------------------- 
                                #Final de sorteo_saca 3 Revancha
