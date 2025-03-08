#Proyecto de loteria 
#Joel
#Christian
#Jorge Maldonado
'''
Muchachos les dejo mi granito de arena, de aqui en adelante modificaremos.
quiero que tengan la libertad de modificar lo que quieran, y reganarme.
'''
#librerias
import random #importamos la libreria random
import os #importamos os
import json #json

#Variables
data_dir = "data" 
boletas_dir = os.path.join(data_dir, "boletos")  
sorteos_dir = os.path.join(data_dir, "sorteos")
reportes_dir = os.path.join(data_dir, "reportes")

#creamos los directorios o carpetas de archivos 
os.makedirs(boletas_dir, exist_ok=True) #
os.makedirs(sorteos_dir, exist_ok=True)
os.makedirs(reportes_dir, exist_ok=True)

#funcion menu principal
def menu_principal(): 
    print("Bienvenido a la loteria")
    print("1. Crear boleta")
    print("2. Generar sorteo")
    print("3. Reportes")
    print("4. Salir")
    opcion = input("Seleccione una opcion: ")
    return opcion






