# Descripcion: Cliente que prueba algoritmos de ordenamiento
# con listas de numeros
# Autor: Juan Ortiz & Rubmary Rojas
# email: 13-11021@usb.ve & rubmaryrojas@gmail.com

import sys, traceback, random, time
from ordenamiento import *
from conjuntos import *
from promedios import *

# Descripcion: Procesa la linea de comandos del programa
# Parametros:
#	args: Arreglo de strings con los argumentos de la linea de comando
# La sipnosis de la linea de comandos es:
# pruebaOrdenamiento <numero de elementos> <dataset> <numero de pruebas>
# donde  <numero de elementos> indica el numero de elementos que va a tener 
# el arreglo a ordenar, <dataset> indica el tipo de datos que se ordenara
# y <numero de pruebas> la cantidad de pruebas que se haran por cada
# algoritmo
# Retorna: El numero de elementos a ordenar
def parseArgs(args):
    msg = "Error en la linea de comando:\npruebaOrdenamiento <numero de elementos> <dataset> <numero de pruebas>"
    if len(args) != 4:
        print(msg)
        sys.exit(1)

    return int(args[1]), int(args[2]), int(args[3])


# Descripcion: Comprueba si un arreglo esta ordenado.
# Parametros:
#	A: Un arreglo de elementos de tipo numerico
# Retorna: True si el arreglo esta ordenado, False en caso contrario.
def estaOrdenado(A):
    n = len(A)
    i = 0
    while(i < n-2):
        if A[i] > A[i+1]:
            print("Error, el arreglo no esta ordenado")
            sys.exit(1)
        i = i+1
    return True

# Descripcion: Prueba los algoritmos de ordenamientos con una lista de elementos.
# Parametros: 
#	datos: arreglo con elementos de tipo numerico
def probarAlgoritmos(datos):

    #print("Generando los datos para....")
    datos1 = datos[:]
    datos2 = datos[:]
    datos3 = datos[:]
    datos4 = datos[:]
    datos5 = datos[:]
      
    #print("Comenzando ordenamiento por heapsort")
    start_time = time.time()
    heap_sort(datos1)
    t_usado = time.time() - start_time
    tiempos[0].append(t_usado)
    ordenado = estaOrdenado(datos1)
    if not ordenado:
        print("Error, su algoritmo de ordenamiento por heapsort no ordeno correctamente")
    else:
        print("Tiempo usado en ordenamiento por heapsort: {0:.4f} segs".format(t_usado))

    #print("Comenzando ordenamiento por median of 3 quicksort")
    start_time = time.time()
    median_of_3_quicksort(datos2, 0, len(datos2))
    t_usado = time.time() - start_time
    tiempos[1].append(t_usado)
    ordenado = estaOrdenado(datos2)
    if not ordenado:
        print("Error, su algoritmo de ordenamiento por median of 3 quicksort no ordeno correctamente")
    else:
        print("Tiempo usado en ordenamiento por median of 3 quicksort: {0:.4f} segs".format(t_usado))

    #print("Comenzando ordenamiento por introsort")
    start_time = time.time()
    introsort(datos3, 0, len(datos3))
    t_usado = time.time() - start_time
    tiempos[2].append(t_usado)
    ordenado = estaOrdenado(datos3)
    if not ordenado:
        print("Error, su algoritmo de ordenamiento por introsort no ordeno correctamente")
    else:
        print("Tiempo usado en ordenamiento por introsort: {0:.4f} segs".format(t_usado))

    #print("Comenzando ordenamiento por Quicksort with 3-way partition")
    start_time = time.time()
    quicksort3(datos4, 0, len(datos4)-1)
    t_usado = time.time() - start_time
    tiempos[3].append(t_usado)
    ordenado = estaOrdenado(datos4)
    if not ordenado:
        print("Error, su algoritmo de ordenamiento por Quicksort with 3-way partition no ordeno correctamente")
    else:
        print("Tiempo usado en ordenamiento por Quicksort with 3-way partition: {0:.4f} segs".format(t_usado))

    #print("Comenzando ordenamiento por Dual pivot Quicksort")
    start_time = time.time()
    quicksort_yaroslavskiy(datos5, 0, len(datos5)-1)
    t_usado = time.time() - start_time
    tiempos[4].append(t_usado)
    ordenado = estaOrdenado(datos5)
    if not ordenado:
        print("Error, su algoritmo de ordenamiento por Dual pivot Quicksort no ordeno correctamente")
    else:
        print("Tiempo usado en ordenamiento por Dual pivot Quicksort: {0:.4f} segs".format(t_usado))
    
    print '\n'
    

################################
## Inicio de la Aplicacion
################################


if __name__ == "__main__":
    # Tiempos de ejecucion de cada algoritmo de ordenamiento
    tiempos=[[], [], [], [], []]
    promedio=[0, 0, 0, 0, 0]

    numElems, dataset, numPruebas = parseArgs(sys.argv)
    datos = obtenerArreglo(numElems, dataset)
    sys.setrecursionlimit(numElems+10)
	
    # Ejecutar los algortimos de ordenameinto 
    # tantas veces como indique numPruebas
    i=0
    while i < numPruebas:
        print('Prueba ' + str(i+1))
        probarAlgoritmos(datos)
        i=i+1

    eliminarMejorPeor(tiempos)
    calcularPromedio(tiempos, promedio, numPruebas-2)
    imprimirPromedio(promedio)
    

