import random


#-------------------------------------------------------------------------------------------------------------
def creacion_boleta_saca3():

    #Creación de boletas para Saca3
    boleta_total_saca3 = []
    revancha_saca3 = []
    precio_saca3 = 0
    precio_revancha_saca3 = 0
    precio_total_saca3 = precio_saca3 + precio_revancha_saca3

    #Funcion Anidada de Aleatorio Saca3
#-------------------------------------------------------------------------------------------------------------
    def aleatorio_saca3():
        print("Bienvenidos a su boleta con revancha\n")

        try:
            # Pedir número de boletos con validación
            while True:
                boleto = int(input("¿Cuántos boletos desea? (solo puede escoger entre 1 a 2 boletas): "))
                if boleto in [1, 2]:
                    break
                else:
                    print("Por favor, ingrese un número válido entre 1 y 2.")

            # Listas
            boletas_aleatoria = []
            coincidencias_totales = []

            # Generar número aleatorio de sorteo
            numero = random.sample(range(0, 9), 3)
            print(f"El número aleatorio del sorteo es: {numero}")

            # Generar las boletas y compararlas
            boleta_total_loteria = []
            for i in range(boleto):
                boleta = random.sample(range(0, 9), 3)
                boleta_total_loteria.append(boleta)
                boletas_aleatoria.append(boleta)
                print(f"Boleta {i + 1}: {boleta}")

            # Comparar cada boleta con el número aleatorio generado
            for i, boleta in enumerate(boleta_total_loteria):
                coincidencias = set(boleta) & set(numero)
                coincidencias_totales.append(coincidencias)
                premio = "Lo siento, no llegaste"

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
                    print(f"Boleta {i + 1}: No ganó.")

            # Guardar los datos en un archivo
            with open("file_revancha_saca3.txt", "a") as archivo:
                archivo.write(f"Boletas generadas: {boletas_aleatoria}\n")
                archivo.write(f"Número del sorteo: {numero}\n")
                archivo.write(f"Coincidencias totales: {coincidencias_totales}\n")
                archivo.write(f"Su premio es: {premio}\n")
                archivo.write("=" * 50 + "\n")

            print("Se guardaron los datos.")

        except ValueError:
            print("Error: Por favor ingrese un número válido.")
        
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
                    boleta_total_saca3.append(valores_jugadas)
                
                print(f"Boletas manuales ingresadas: {jugadas}")
                break
            except ValueError as value:
                print(f"\n Ingresaste un valor diferente a lo que se pide, por favor, inténtelo de nuevo. Error: {value} ")
            
            
            
            
    #--------------------------------------------------------------------------------------------------------------------------------------------------
    #Fin de la función Manual
    
    return aleatorio_saca3, manual_saca3, boleta_total_saca3

#-------------------------------------------------------------------------------------------------------------