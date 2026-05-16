import random as rd
import time

#---------Búsqueda Secuencial------------

def busqueda_secuencial(arr, num_buscar):
    for i in range(len(arr)):
        if arr[i] == num_buscar:
            return i
    return -1

#----------Búsqueda Binaria--------------

def busqueda_binaria(arr, num_buscar):
    izquierda = 0
    derecha = len(arr) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if arr[medio] == num_buscar:
            return medio

        elif arr[medio] < num_buscar:
            izquierda = medio + 1

        else:
            derecha = medio - 1

    return -1

#----------------MAIN-------------------

#Creo un arreglo con 1 millon de números aleatorios utilizando un generador random
array = [rd.randint(1, 1_000_000) for _ in range(1_000_000)]

numero = int(input("Ingrese el número que desea buscar: "))


#------BÚSQUEDA SECUENCIAL + TIEMPO----
inicio_sec = time.time()

resultado_sec = busqueda_secuencial(array, numero)

fin_sec = time.time()

tiempo_sec = fin_sec - inicio_sec


#----------BÚSQUEDA BINARIA + TIEMPO------

# Ordeno para realizar la búsqueda binaria
array_ordenado = sorted(array)

inicio_bin = time.time()

resultado_bin = busqueda_binaria(array_ordenado, numero)

fin_bin = time.time()

tiempo_bin = fin_bin - inicio_bin



#---------MUESTRO RESULTADOS-----------

print("\n===== RESULTADOS =====")

#Búsqueda Secuencial
if resultado_sec != -1:
    print(f"\nBúsqueda Secuencial:")
    print(f"Número encontrado")
    print(f"Posición: {resultado_sec}")
else:
    print(f"\nBúsqueda Secuencial:")
    print("Número no encontrado")

print(f"Tiempo de ejecución: {tiempo_sec:.6f} segundos")


#Búsqueda Binaria
if resultado_bin != -1:
    print(f"\nBúsqueda Binaria:")
    print("Número encontrado")
    print(f"Posición: {resultado_bin}")
else:
    print(f"\nBúsqueda Binaria:")
    print("Número no encontrado")

print(f"Tiempo de ejecución: {tiempo_bin:.6f} segundos")
