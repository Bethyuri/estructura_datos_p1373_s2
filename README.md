# estructura_datos_p1373_s2
# Tarea 1: Gestión de Memoria Dinámica y Estructuras Lineales

## Descripción del proyecto: Este proyecto implementa dos algoritmos de búsqueda en Python para un arreglo:
- Búsqueda Secuencial
- Búsqueda Binaria

El programa genera un arreglo de 1 millón de números enteros aleatorios y permite al usuario ingresar un número desde el teclado para buscarlo utilizando ambos algoritmos.

Este programa nos muestra como resultado:
- Si el número fue encontrado o no.
- La posición en donde se encuentra el número.
- El tiempo de ejecución de cada algoritmo.

El objetivo es comparar el rendimiento entre ambos métodos de búsqueda.

## Pre-requisitos
Para ejecutar este proyecto se necesita:

- Python 3.10 o superior

Librerías utilizadas:
- random
- time

Estas librerías ya vienen incluidas en Python, por lo que no es necesario instalar paquetes adicionales.


## Instrucciones para ejecutar el programa

1. Descargar o copiar el archivo del programa.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el archivo:
4. Ingresar un número cuando el programa lo solicite.
5. El programa mostrará los resultados de ambas búsquedas.

## Explicación de los algoritmos

La búsqueda secuencial recorre el arreglo elemento por elemento hasta encontrar el número ingresado.

Características:
- No necesita que el arreglo esté ordenado.
- Puede ser lenta con grandes cantidades de datos.

La búsqueda binaria divide el arreglo en mitades sucesivamente para encontrar el número.

Características:
- Requiere que el arreglo esté ordenado.
- Mucho más rápida en arreglos grandes.

## Resultados obtenidos

Durante las pruebas realizadas se observó que:

- La búsqueda secuencial tarda más tiempo porque revisa los elementos uno por uno.
- La búsqueda binaria es considerablemente más rápida debido a que reduce el espacio de búsqueda a la mitad en cada iteración.

Con un arreglo de 1 millón de elementos, la diferencia de rendimiento es grande.
