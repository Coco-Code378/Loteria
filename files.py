
                                            #Creo la función de boletas manuales
#-----------------------------------------------------------------------------------------------------------------------------------------
file2 = "boletas_manuales.txt"
def crear_archivo_saca3(file2):
    
    try:
     with open(file2 , "x"):
        print(f"Archivo {file2} se creo bien")
    
    except FileExistsError:
        print("El archivo ya existe")
#----------------------------------------------------------------------------------------------------------------------------------------
      
    
#----------------------------------------------------------------------------------------
                                     #Fin de la creación 

                           #Creación del file para aleatorio
#------------------------------------------------------------------------------------------
file = "boletas.txt"
def crear_archivo(file):
    
    #Comenzamos el manejo de errores pero por existencia
    try: 
     with open(file, "x") :#Me ayuda crear el archivo y cerrarlo automaticamente
        print(f"Archivo {file} se creo bien")
        
    except FileExistsError:
        print("El archivo ya existe")
        
#--------------------------------------------------------------------------------------        
    
    

