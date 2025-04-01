
                            #Creo la funcion de boletas aleatorias
#-------------------------------------------------------------------------------------------------------------------------------------------
file = "boletas_aleatorias.txt"
def boleta_aleatoria(file):
    
    #Comenzamos el manejo de errores pero por existencia
    try: 
     with open(file, "x") :#Me ayuda crear el archivo y cerrarlo automaticamente
        print(f"Archivo {file} se creo bien")
        
    except FileExistsError:
        print("El archivo ya existe")
#-------------------------------------------------------------------------------------------------------------------------------------------

                       #Creo la funcion de boletas aleatorias en revancha
#-------------------------------------------------------------------------------------------------------------------------------------------
file_revancha = "boletas_aleatorias revancha.txt"
def boleta_aleatoria(file_revancha):
    
    #Comenzamos el manejo de errores pero por existencia
    try: 
     with open(file_revancha, "x") :#Me ayuda crear el archivo y cerrarlo automaticamente
        print(f"Archivo {file_revancha} se creo bien")
        
    except FileExistsError:
        print("El archivo ya existe")
#-------------------------------------------------------------------------------------------------------------------------------------------




                                            #Creo la función de boletas manuales
#-----------------------------------------------------------------------------------------------------------------------------------------
file2 = "boletas_manuales.txt"
def boleta_manual(file2):
    
    try:
     with open(file2 , "x"):
        print(f"Archivo {file2} se creo bien")
    
    except FileExistsError:
        print("El archivo ya existe")
#----------------------------------------------------------------------------------------------------------------------------------------
      
      
      
                        #Creo una función para crear un file para generar sorteo
#--------------------------------------------------------------------------------------
file3 = "boletas_sorteo_generado.txt"
def crear_archivo(file3):
    
    #Comenzamos el manejo de errores pero por existencia
    try: 
     with open(file3, "x") :#Me ayuda crear el archivo y cerrarlo automaticamente
        print(f"Archivo {file3} se creo bien")
        
    except FileExistsError:
        print("El archivo ya existe")
    
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







      
                                        #Leer las lineas en el file aleatorio
#----------------------------------------------------------------------------------------------------------------
def file_aleatorio(file):
    try:
        with open(file, "r"):
         lineas = file.readlines()
         print(lineas)
        
            
            
    except FileNotFoundError:
     print(f"El archivo no se encuetra")
   
  
  
                                        #Leer las lineas en el file manual
#---------------------------------------------------------------------------------------------------------------- 
def file_manual(file2):
    
    try:
        with open(file2, "r"):
            lineas = file2.readlines()
            print(lineas)

    except FileNotFoundError:
        print("El archivo no se encuentra")
        
        
        
        
                                                #Función para escoger boleta manual
#----------------------------------------------------------------------------------------------------------------
def escoger_boleta_manual():
      try: 
       escoger = str(input("Desea continuar? De lo contrario perdería su boleta:  ".lower())) #lo convierto en lower la contestación
                                      
       if escoger == "si":
        print("Excelente, su archivo tiene la boleta registrada")
        boleta_manual(file)
                                         
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
#----------------------------------------------------------------------------------------------------------------                    
    