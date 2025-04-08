
                                            #Creo la función de boletas manuales
#-----------------------------------------------------------------------------------------------------------------------------------------
file2 = ".\\Archivos\\boletas_saca3.txt"
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
file = ".\\Archivos\\boletas_loteria.txt"
def crear_archivo(file):
    
    #Comenzamos el manejo de errores pero por existencia
    try: 
     with open(file, "x") :#Me ayuda crear el archivo y cerrarlo automaticamente
        print(f"Archivo {file} se creo bien")
        
    except FileExistsError:
        print("El archivo ya existe")
        
#--------------------------------------------------------------------------------------        
    
file3 = ".\\Archivos\\Reportes_Loteria.txt"   
                          #Creación del file para reportes
#------------------------------------------------------------------------------------------
file = ".\\Archivos\\boletas_loteria.txt"
def crear_archivo(file3):
    
    #Comenzamos el manejo de errores pero por existencia
    try: 
     with open(file3, "x") :#Me ayuda crear el archivo y cerrarlo automaticamente
        print(f"Archivo {file3} se creo bien")
        
    except FileExistsError:
        print("El archivo ya existe")
        
#--------------------------------------------------------------------------------------       
