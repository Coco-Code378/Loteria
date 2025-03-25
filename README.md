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

#-------------------------------------------------------------------------------------------------------------#
# Función de creacion_sorteos()

#Función anidada para la comparación de boletas de jugadas con las boletas de sorteos
comparar_boletas(sorteo, total_boletas)

#Función anidada para generar sorteos en el juego de lotería:
generar_sorteo_loteria()

#Función anidada para generar sorteos en el juego de saca3
generar_sorteo_saca3()
```



## Recursos Adicionales:

## Desarrolladores:

- Jorge Maldonado - Scrum Master
- Christian Matias - Scrum Team
- Joel Maisoent - Scrum Team
