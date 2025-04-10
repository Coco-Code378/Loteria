# Proyecto de Lotería

 Este proyecto, desarrollado en Python, simula la gestión de una lotería. El programa está diseñado para crear directorios específicos para cada sección del menú y se divide en tres partes fundamentales: creación, sorteo y registro.

1.  **Creación**: En esta sección, los usuarios pueden generar boletas seleccionando los dígitos correspondientes según el tipo de juego de la lotería. Además, pueden elegir la cantidad de jugadas y la opción de revancha. Tras realizar estas selecciones, se procede a la compra de las boletas.

2. **Sorteo**: En esta fase, se valida la autenticidad de las jugadas y se registran los resultados.

3. **Registros**: En la sección final, se lleva a cabo todos los registros tanto de boletas como de sorteos y las diversas opciones que brinda el programa. 

## Funciones:

```Python


#------------------------------------------------------------------------------------------------------------#
# Principales:

#Función Main en donde se ejecutará el programa y contendrá los match case en donde el usuario podrá elegir lo que quiere realizar.
main()

#Función que abarcará todo tipo de menu interactivo para el usuario.
menu() 

#Función que se ejecuta para limpiar la terminal. Dicha función determinará si el sistema operativo es Windows o Unix. 
limpiar_pantalla()  

#------------------------------------------------------------------------------------------------------------#
# Funciones para Lotería y Saca 3:

#Función que abarcará la manera tanto automática como manual de creación de boletas tanto para lotería como para saca 3
creacion_boletas()

#Función que abarcará la creación y comparación de sorteos en las jugadas del usuario:
creacion_sorteos() 

#------------------------------------------------------------------------------------------------------------#
# Función de creacion_boletas()

#Función anidada que asigna una jugada de forma aleatoria para el juego de Lotería
aleatorio_loteria()

#Función anidada que asigna una jugada de forma manual, ingresando los dígitos del usuario en el juego de Lotería
manual_loteria()



    	                                    #Files
#-----------------------------------------------------------------------------------------------------------        
Este archivo contiene las dos funcioens que estaremos manejando para guardar la data en los archivos

#Esta función será la encargada de crear el archivo si no existiera en el entorno loteria
crear_archivos()

#Esta función será la encargada de crear un archivo si no existiera en el entorno saca3
crear_archivo_saca3() 
#-------------------------------------------------------------------------------------------------------------
                                        #Fin de files


                                        #Limpiar pantalla
#------------------------------------------------------------------------------------------------------------

Este archivo será el encargado de hacer un "cls" para que se limpie la 
pantalla y se vea mejor el código.

#Esta función abarca todo el file y se encarga de limpiar la linea de comandos
limpiar_pantalla() 
#-------------------------------------------------------------------------------------------------------------
                                            #Fin del limpiar pantalla





                                        #loteria
#-------------------------------------------------------------------------------------------------------------#
Este archivo será el encargado de tener la mayor de las instrucciones de lo que se estará manejando para 
el manejo de los sorteos, aquí podrán ver el mayor código ya que será la estructura de la loteria


#Esta función es la padre ya que de esta se crean otras
creacion_sorteos()


#Esta es la función anidada de creacion_sorteos y se encarga de auto-incrementar cada boleta 
boleta_total()


#Esta es la segunda función anidada de creación_sorteos y será la que mantenga la loteria
#aleatoria, suma la boleta, tiene las jugadas y lo lleva al archivo con la revancha si la hubiera escogido
aleatorio_loteria()


#Esta es la tercara función anidada de creacion_sorteos y será la que mantenga la loteria
#manual, suma la boleta, tiene las jugadas y lo lleva al archivo con la revancha si la hubiera escogido
manual_loteria()
#----------------------------------------------------------------------------------------------------
Estas serán las funciones en el mismo archivo pero sin anidar


#Función para generar sorteos en el juego de lotería:
generar_sorteo()

#Función anidada para generar sorteos en el juego de saca3
generar_sorteo_saca3()

                                #Sorteos
#---------------------------------------------------------------------------------------------------------



#Esta función será la encargada de si el usuario al marcar generar sorteo, la información y datos que suba sea 
#para la revancha y se marque más te diga lo que ganaste
sorteo_loteria_revancha()


#Esta función será la que se encarga de si el usuario al marcar generar sorteo, la información y datos que suba sea 
#para la jugada y se marque más te diga lo que ganaste
sorteo_loteria_jugadas()

#--------------------------------------------------------------------------------------------------------------
                                        #Fin de loterias



                                            #Menu
#------------------------------------------------------------------------------------------------------------
Este archivo va a contener todos los menus que hay se estarán utilizando para el proyecto de loteria

#Esta será la función principal (padre) que estará definiendo en otras funciones los menus de los diferentes 
#requisitos para operar correctamente
menu()

#Este es el primer menú que vemos al inicio cuando interpretamos el código y es la primera función anidada
menu_principal()


#Esta es la segunda función anidada que el usuario escogera que hacer y será una de las primordiales para la jugabilidad
menu_juegos()


#Esta es la tercera función anidada que será la que estará al escoger comprar boletas para escoger entre (manual) y (aleatorio)
menu_boletas()
#----------------------------------------------------------------------------------------------------------------------------


                                                #Premios del archivo menu
#----------------------------------------------------------------------------------------------------------------------------
Estas serán las funciones en el mismo archivo pero sin anidar


#En esta función podrán observar los premios que se estará atribuyendo a los que ganen en la loteria
premios_loteria()


#Esta función será la encargada de poder observar los premios que se estará ofreciendo a los que ganen en el saca3
premios_saca3()


                                            #Premios del archivo saca3
#----------------------------------------------------------------------------------------------------------------------------
Este archivo va a contener los datos para que el usuario registre lo que desee comprar y pueda ver los sorteos


#En esta función guardaré los datos que se estará guardando para llevarlo a los sorteos y se puede acumular siendo la función padre
creacion_sorteo_saca3()

#En esta función siendo la primera función anidada, es la encargada de generar los numerós aleatorios del saca 3 y los lleve al file
aleatorio_saca3()


#En esta función siendo la segunda fncion anidada, es la que el usuario podrá poner los números que desee y se guardará en el file
manual_saca3()


#En esta función se estará auto-incrementando la bóleta por cada vez que reinicie el juego
boleta_total_revancha()

#----------------------------------------------------------------------------------------------------------------------------------------------
                            Estas serán las funciones en el mismo archivo pero sin anidar


#Esta función es la encargada de generar los sorteos del saca 3 y mostrar las coincidencias con su premio y lo lleve al archivo
aleatorio_saca3_reporte()



#Esta función es la encarada de generar los sorteos del saca 3 en revancha y mostar las coincidencias con su premio y lo lleve al archivo
sorteo_saca3_revancha()
#--------------------------------------------------------------------------------------------------------------------------------------------------
```



## Recursos Adicionales:

[Documentacion Grupal](https://docs.google.com/document/u/1/d/1gEZ4BbPLp1j_7AjLEYFIwo63857CsqpK6Ptov6vumxw/mobilebasic?usp=gmail)

## Desarrolladores:

- Jorge Maldonado - Scrum Master
- Christian Matias - Scrum Team
- Joel Maisoent - Scrum Team
