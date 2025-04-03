#Proyecto de loteria 
#Joel Maisonet
#Christian Matias 
#Jorge Maldonado

#librerias
import os
import random #importamos la libreria random
from files import *
from menu import *


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

 #Funcion Principal de creación de boletas para lotería
boleta_total_loteria = []

#-------------------------------------------------------------------------------------------------------

def creacion_boletas_loteria():
   

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
         boleta_total_loteria.append(boleta)  # Agrega cada boleta al total global
         boletas_aleatoria.append(boleta)  # Agrega a la lista local
         print(f"Esta es tu boleta aleatoria: {boletas_aleatoria}")
        
        # Comparar cada boleta existente con el número aleatorio generado
       for i, boleta in enumerate(boleta_total_loteria):
            coincidencias = set(boleta) & set(numero)  # Encuentra los números en común
            coincidencias_totales.append(coincidencias)
            premio = " "
            if coincidencias:
                print(f"Boleta {i + 1}: Le pegaste a {len(coincidencias)} número(s), coincidencias: {sorted(coincidencias)}")
                
                
                if len(coincidencias) == 3:
                    premio ="Felicidades, acertaste 3 numeros y ganaste un boleto gratis"
                    
                elif len(coincidencias) == 4:
                    premio = "Felicidades, acertaste 4 numeros y ganaste 75,000 dólares"
                elif len(coincidencias) == 5:
                    premio = "Felicidades, acertaste 5 numeros y ganaste 300,000 dólares"
                            
                elif len(coincidencias) == 6:
                    premio = "Felicidades, acertaste todos los numero y ganaste EL MILLON"
                                
                else:
                    premio = "Lo siento, no llegaste"
                      
            else:
                print(f"Boleta {i + 1}: No ganó.")
                
               
                 
      
           # Guardar los datos en un archivo
       with open(file, "a") as archivo:
          archivo.write(f"Su boleta es: {boletas_aleatoria}\n")
          archivo.write(f"El numero del sorteo es: {numero}\n")
          archivo.write(f"Coincidencias totales: {coincidencias_totales}\n")
          archivo.write(f"Este fue su premio: {premio}\n")
          archivo.write("=" * 50 + "\n")
        
     
        
        # Generar los boletos aleatorios solicitados
       
            
            
       return boleta_aleatoria
 #------------------------------------------------------------------------------------------------------------
 # Fin de la función Aleatoria
 
                #Función para aleatorio en revancha
#-------------------------------------------------------------------------------------------------------------

    def aleatorio_loteria_revancha():
      print(f"{'Bienvenidos a su boleta con revancha\n'}")
    
      try:
        # Pedir número de boletos con validación
        while True:
            boleto = int(input("¿Cuántos boletos desea? (solo puede escoger entre 1 a 2 boletas): "))
            if boleto in [1, 2]:
                break
            else:
                print("Por favor, ingrese un número válido entre 1 y 2.")
        
        #Listas
        boletas_aleatoria = []  
        coincidencias_totales = []  
        
        # Generar número aleatorio de sorteo
        numero = random.sample(range(0, 66), 6)
        print(f"El numero aleatorio del sorteo es: {numero}")
        
        # Generar las boletas y compararlas
        for i in range(boleto):
            boleta = random.sample(range(0, 66), 6) 
            boleta_total_loteria.append(boleta) 
            boletas_aleatoria.append(boleta) 
            premio = " "
            print(f"Boleta {i + 1}: {boleta}")
        
        # Comparar cada boleta con el número aleatorio generado
        for i, boleta in enumerate(boleta_total_loteria):
            coincidencias = set(boleta) & set(numero) 
            coincidencias_totales.append(coincidencias)
            if coincidencias:
                print(f"Boleta {i + 1}: Le pegaste a {len(coincidencias)} numero(s), coincidencias: {sorted(coincidencias)}")
                
               
                if coincidencias:
                 print(f"Boleta {i + 1}: Le pegaste a {len(coincidencias)} número(s), coincidencias: {sorted(coincidencias)}")
                
                
                 if len(coincidencias) == 3:
                      premio ="Felicidades, acertaste 3 numeros y ganaste un boleto gratis"
                    
                 elif len(coincidencias) == 4:
                      premio = "Felicidades, acertaste 4 numeros y ganaste 75,000 dólares"
                 elif len(coincidencias) == 5:
                    premio = "Felicidades, acertaste 5 numeros y ganaste 300,000 dólares"
                            
                 elif len(coincidencias) == 6:
                    premio = "Felicidades, acertaste todos los numero y ganaste EL MILLON"
                                
                 else:
                    premio = "Lo siento, no llegaste"
                
            else:
                print(f"Boleta {i + 1}: No gano.")
        
        # Guardar los datos en un archivo
        with open(file_revancha, "a") as archivo:
            archivo.write(f"Boletas generadas: {boletas_aleatoria}\n")
            archivo.write(f"Numero del sorteo: {numero}\n")
            archivo.write(f"Coincidencias totales: {coincidencias_totales}\n")
            archivo.write(f"Su premio es: {premio}")
            archivo.write("=" * 50 + "\n")
        print("Se guardaron los datos.")
    
      except ValueError:
        print("Error: Por favor ingrese un número válido.")
        
        return aleatorio_loteria_revancha
#------------------------------------------------------------------------------------------------------------------------------------------------


        
        
                                                #Función para la revancha en saca 3
#---------------------------------------------------------------------------------------------------------------------------------------------------
    def aleatorio_loteria_revancha_saca3():
     print(f"{'Bienvenidos a su boleta con revancha\n'}")
    
 
    
     try:
        # Pedir número de boletos con validación
        while True:
            boleto = int(input("¿Cuántos boletos desea? (solo puede escoger entre 1 a 2 boletas): "))
            if boleto in [1, 2]:
                break
            else:
                print("Por favor, ingrese un número válido entre 1 y 2.")
        #Listas
        boletas_aleatoria = []  
        coincidencias_totales = [] 
        
        # Generar número aleatorio de sorteo
        numero = random.sample(range(0, 9), 3)
        print(f"El numero aleatorio del sorteo es: {numero}")
        
        # Generar las boletas y compararlas
        for i in range(boleto):
            boleta = random.sample(range(0, 9), 3)
            boleta_total_loteria.append(boleta) 
            boletas_aleatoria.append(boleta) 
            print(f"Boleta {i + 1}: {boleta}")
        
        # Comparar cada boleta con el número aleatorio generado
        for i, boleta in enumerate(boleta_total_loteria):
            coincidencias = set(boleta) & set(numero) 
            coincidencias_totales.append(coincidencias)
            premio = " "
            if coincidencias:
                print(f"Boleta {i + 1}: Le pegaste a {len(coincidencias)} numero(s), coincidencias: {sorted(coincidencias)}")
                
                if coincidencias:
                   print(f"Boleta {i + 1}: Le pegaste a {len(coincidencias)} número(s), coincidencias: {sorted(coincidencias)}")
                
                
                   if len(coincidencias) == 3:
                    premio ="Felicidades, acertaste 3 numeros y ganaste un boleto gratis"
                    
                   elif len(coincidencias) == 4:
                    premio = "Felicidades, acertaste 4 numeros y ganaste 75,000 dólares"
                   elif len(coincidencias) == 5:
                    premio = "Felicidades, acertaste 5 numeros y ganaste 300,000 dólares"
                            
                   elif len(coincidencias) == 6:
                    premio = "Felicidades, acertaste todos los numero y ganaste EL MILLON"
                                
                   else:
                    premio = "Lo siento, no llegaste"
                      
            else:
                print(f"Boleta {i + 1}: No ganó.")
        
        # Guardar los datos en un archivo
        with open(file_revancha_saca3, "a") as archivo:
            archivo.write(f"Boletas generadas: {boletas_aleatoria}\n")
            archivo.write(f"Numero del sorteo: {numero}\n")
            archivo.write(f"Coincidencias totales: {coincidencias_totales}\n")
            archivo.write(f"Su premio es: {premio}")
            archivo.write("=" * 50 + "\n")
        print("Se guardaron los datos.")
    
     except ValueError:
        print("Error: Por favor ingrese un número válido.")
        
        return aleatorio_loteria_revancha_saca3
   
                    	#Función Secundaria para Manual Loteria
#-----------------------------------------------------------------------------------------------------------
    def manual_loteria():
        #Variables y listas
        precio_jugada = 0
        precio_revancha = 0
        
        
        #Prints 
        print(f"{"=" * 8} Costos: {"=" * 8}")
        print(f"Cada jugada cuesta $2.00")
        print(f"Cada revancha cuesta $1.00")
 
        #Variable para la cantidad de jugadas
        cantidad_jugadas = int(input("Ingrese la cantidad de jugadas a realizar: "))
        
        #inicializando las jugadas en una lista
        jugadas = []
        while True:
            try:
               
                for i in range(cantidad_jugadas):
                    
                    #Listas inicializadas en el For
                    precio_jugada += 2
                    valores_jugadas = []
                    valores_unicos = set()
                    revanchas = []
                    
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
                            elif numeros == "":
                                print("\n Elegiste un número no correspondido a lo que se pide.")    
                    opcion = input("¿Deseas incluir esta jugada como revancha? (Si/No): ")
                    opcion = opcion.capitalize()
                    if opcion == "Si":
                        precio_revancha += 1
                        revanchas.append(jugadas)
                        boleta_total_loteria.append(revanchas)
                        print("\nLa jugada fue añadida para Revancha")
                    else:
                        print("\nLa jugada no fue añadida como revancha")   

                    #Ingresando y limpiando las listas
                    valores_unicos.clear()             
                    jugadas.append(valores_jugadas)
                    boleta_total_loteria.append(jugadas)
                
                #Limpiar pantalla para mejor visualización
                limpiar_pantalla()
                precio_total = precio_jugada + precio_revancha
                print(f"\nJugadas manuales ingresadas: {jugadas}")
                print(f"\nJugadas con Revancha: {revanchas}")
                print(f"\nPrecio total: ${precio_total}")
                break
           
                
            except ValueError as value:
                print(f"\n Ingresaste un valor diferente a lo que se pide, por favor, inténtelo de nuevo. Error: {value} ")
         #Cerrando el ciclo While True
              
#-----------------------------------------------------------------------------------------------------------------------------------------




    	                                        #Función para hacer Manual saca 3               
#-----------------------------------------------------------------------------------------------------------------------------------------
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
                            numeros = int(input(f"Ingrese un valor: {j + 1} del 0 al {9 - 1} en la jugada {i + 1}, (No se puede repetir): "))
                    
                            if 0 <=  numeros <= 9:
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
                    boleta_total_loteria.append(valores_jugadas)
                
                print(f"Boletas manuales ingresadas: {jugadas}")
                break
            except ValueError as value:
                print(f"\n Ingresaste un valor diferente a lo que se pide, por favor, inténtelo de nuevo. Error: {value} ")
            
            
            
            
    #--------------------------------------------------------------------------------------------------------------------------------------------------
    #Fin de la función Manual
    
    #Returns de la función Creación_Boletas:
    return aleatorio_loteria,aleatorio_loteria_revancha,aleatorio_loteria_revancha_saca3, manual_loteria, boleta_total_loteria, manual_saca3
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
     for i, boleta in enumerate(boleta_total_loteria):
        coincidencias = set(boleta) & set(sorteo2)  # Comparamos cada boleta con el sorteo
        
       
        if coincidencias:
             print(f"Boleta {i + 1}: Le pegaste a {len(coincidencias)} número(s), coincidencias: {sorted(coincidencias)}") #Compara las coindicencias
           
        else:
             print(f"Boleta {i + 1}: No ganó.")
             
        with open(file , "a") as archivo:
            archivo.write(f"su boleta es: {boleta}\n la del sorteo es: {sorteo2} \n iguales: {coincidencias}\n")
            
            archivo.write("=" * 50)
#-----------------------------------------------------------------------------------------------------------------


def comparar_boletas_manual():

     sorteo2 = generar_sorteo()
     print(f"Sorteo generado: {sorteo2}")
     print("\nComparación de Boletas:")
    #Búcle para la comparación de boleta
     for i, boleta in enumerate(boleta_total_loteria):
        coincidencias = set(boleta) & set(sorteo2)  # Comparamos cada boleta con el sorteo
        
       
        if coincidencias:
             print(f"Boleta {i + 1}: Le pegaste a {len(coincidencias)} número(s), coincidencias: {sorted(coincidencias)}") #Compara las coindicencias
           
        else:
             print(f"Boleta {i + 1}: No ganó.")
             
        with open(file2 , "a") as archivo:
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
    principal, juego, boletas, premios_loteria, premios_saca3 = menu()
    aleatorio_loteria,aleatorio_revancha,aleatorio_revancha_saca3, manual_loteria, total_boletas, manual_saca3= creacion_boletas_loteria()
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
                        print(f"{"=" * 40} Loteria {"=" * 40}")
                        juego()
                        opcion_loteria = str(input("\n Elige la opción a seleccionar: "))
                        
                        
                                                        #segundo case por si marca la opción "1"
                        #------------------------------------------------------------------------------------------------------------------
                        match opcion_loteria:

                                #Comprar boletas
                            case "1":
                                 try:
                                      limpiar_pantalla()
                                      
                                      boletas()
                                      choose = input("Seleccione su opción): ")
                                     
                                      match choose:
                                          
                                          #Case para seleccionar de forma manual las jugadas
                                          case "1":
                                              limpiar_pantalla()
                                              print(f"{"-" * 15} Manual {"-" * 15}")
                                              
                                              manual_loteria()

                                              #Este lo lleva a una función para generar sorteo aleatoriamente
                                              sorteo = generar_sorteo() 
                                              print(f"El sorteo es: {sorteo}")
                                        
                                              #Lo lleva a la función de comparación de boletas
                                              comparar_boletas_manual()
                                              
                                          #Case para seleccionar de forma aleatoria las jugadas
                                          case "2":
                                                limpiar_pantalla()
                                                print(f"{"-" * 15} Aleatorio {"-" * 15}")       

                                                aleatorio_loteria() 
                                                       
                                          case _:
                                               print("Hubo un error al intentar seleccionar la opción deseada.")
                                                             #Tercer Match Case para que el usuario escoga entre aleatorio o manual
                                     #-------------------------------------------------------------------------------------------------------
                                     
                                         
                                 except TypeError as typo:
                                       print(f"Tiene un error {typo}")
                                 
                             #-------------------------------------------------------------------------------------------------------------------------------
                            
                                          
                            
                            
                             #Este es el tercer case del segundo match case para generar sorteo aleatoriamente
                             #--------------------------------------------------------------------------------------------------------------------------------       
                            case "2":
                                print(f"\n {"-" * 15} Generar Sorteo {"-" * 15}\n")
                                
                                
                                print(f"\n {"-" * 7}Comparación de Boletas: {"-" * 7}")   
                                #Llamando la función generar_boletas()
                                
                                
                               #Voy a la función de generar sorteo para que comparé, crea y los lleva al file
                                generar_sort()                                
                                    
                                    
                                    
                                    #Este es el cuarto case del segundo Match Case para los reportes
                            #------------------------------------------------------------------------------------------------------------------------------------
                            case "3":
                                print(f"\n {"-" * 15} Reportes {"-" * 15}\n")
                                     
                                print("Le vamos a crear un archivo con las boletas\n")
                                     
                                escoger()#llamo a la función para que escoja lo que desea hacer
                                
                                
                                
                                     #Función para salir del programa
                            #------------------------------------------------------------------------------------------------------------------------------------         
                            case "4":
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
                            limpiar_pantalla()
                            
                            aleatorio_revancha_saca3()
                        
                        
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