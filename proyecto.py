#Proyecto de loteria 
#Joel Maisonet
#Christian Matias 
#Jorge Maldonado

#librerias
import random #importamos la libreria random
from limpiar_pantalla import *
from files import *
from menu import *
from loteria import *
from saca3 import *
from reportes import *





#----------------------------------------------------------------------------------------
#Función para el programa Main
def main():
    #Referencias de funciones:
    principal, juego, boletas, premios_loteria, premios_saca3 = menu()
    aleatorio_loteria, manual_loteria, jugadas, revanchas, total_boletas = creacion_boletas_loteria()
    aleatorio_saca3,manual_saca3, boleta_total_revancha,jugada, revancha3= creacion_boleta_saca3()
    

    
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
                                print(f"\n {"-" * 15} Sorteos Para Jugadas... {"-" * 15}\n")
                                
                                print(f"La cantidad de boletas es {total_boletas()}")

                          
                                print(f"\n {"-" * 7}Comparación de Boletas...: {"-" * 7}")   
                                
                                #Llamando la función para comprar boletas y generar sorteo
                                sorteo_loteria_jugadas(jugadas)

                                elegir = input("¿Deseas pasar a los sorteos de revancha? (Si/No): ")
                                elegir = elegir.capitalize()

                                if elegir == "Si":
                                    limpiar_pantalla()
                                    print(f"\n {"-" * 15} Sorteos Para Revanchas... {"-" * 15}\n")
                                    print(f"\n {"-" * 7}Comparación de Boletas...: {"-" * 7}")  
                                    sorteo_loteria_revanchas(revanchas)
                          
                                
                                     
                                else:
                                    print("La revancha fue cancelada, perdiste dinero.")
                                                      
                                    
                                    
                                    #Este es el cuarto case del segundo Match Case para los reportes
                            #------------------------------------------------------------------------------------------------------------------------------------
                            case "3":
                                print(f"\n {"-" * 15} Reportes {"-" * 15}\n")
                                     
                                print("Le vamos a crear un archivo con las boletas\n")
                          
                                
                                
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
                    premios_saca3()
                    
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
                            opcion_boletas =input("\n Elige la opción a seleccionar: ")
                            
                            
                            
                                            #Este 2 Match Case es para el manejo de opciónes para hacer la boleta manual o aleatoriamente
                        #------------------------------------------------------------------------------------------------------------------------------
                            match opcion_boletas:
                                
                                
                                            #El case 1 es para la creación de boletas Manuales
                            #-------------------------------------------------------------------------------------------------------------------------
                                case "1":
                                    
                                    # Llamando la función Limpiar_pantalla
                                    limpiar_pantalla()
                                    
                                    print(f"\n {"-" * 15} Creación de Boletas Manuales: {"-" * 15}\n")
                                    manual_saca3()


                                                        #Este match case es para el manejo de la boleta Automatica
                            #-----------------------------------------------------------------------------------------------------------------------
                                case "2":
                                    # Llamando la función Limpiar_pantalla
                                    limpiar_pantalla()

                                    print(f"\n {"-" * 15} Creación de Boletas Automatica: {"-" * 15}\n")
                                    aleatorio_saca3()
                                    
                                    
                                    
                                    
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
                            print(f"\n {"-" * 15} Sorteos {"-" * 15}\n")
                            print(f"La cantidad de boletas es {boleta_total_revancha()}")
                                
                            print(f"\n {"-" * 7}Comparación de Boletas: {"-" * 7}")   
                            
                            aleatorio_saca3_reporte(jugada)

                            elegir = input("¿Deseas pasar a los sorteos de revancha? (Si/No): ")
                            elegir = elegir.capitalize()

                            if elegir == "Si":
                                    limpiar_pantalla()
                                    print(f"\n {"-" * 15} Sorteos Para Revanchas... {"-" * 15}\n")
                                    print(f"\n {"-" * 7}Comparación de Boletas...: {"-" * 7}")  
                                    sorteo_saca3_revanchas(revancha3)
                          
                                
                                     
                            else:
                                    print("La revancha fue cancelada, perdiste dinero.")

        
                        
                        
                               #Este es el tercero case para generar sorteos
                    #----------------------------------------------------------------------------------------------------------------------------------
                        
                        case "3":

                            # Llamando la función Limpiar_pantalla
                            limpiar_pantalla()

                          
                                                      
                            
                            
                            
                            
                            #Llamando la función generar_boletas()
                        #---------------------------------------------------------------------------------------------------------------------------------

                            
                            
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