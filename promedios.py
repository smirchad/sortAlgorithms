# Descripcion: Procedimientos que calculan los promedios pedidos e
# imprimen los resultados
# Autor: Juan Ortiz & Rubmary Rojas
# email: 13-11021@usb.ve & rubmaryrojas@gmail.com


# Descripcion: elimina el mejor y peor tiempo obtenido para cada algoritmo
# Parametros de entrada:
#   A: Arreglo de tamano 5xN, donde N es la cantidad de pruebas realizadas
#   que contiene los tiempos de ejecucion de cada algoritmo
# Precondicion: N>0
# Postcondicion: Se elimina el menor valor y el mayor valor de cada fila
def eliminarMejorPeor(A):
    i=0
    while i < 5:
        sorted(A[i])
        A[i].pop(0)
        A[i].pop(len(A[i])-1) 
        i=i+1

# Descripcion: calcula el tiempo promedio usado por cada algoritmo
# Parametros de entrada:
#	pruebas: tamano de las filas del arreglo
#   A: Arreglo de tamano 5xpruebas
# Postcondicion: promed[i] es igual al promedio de la fila A[i]
def calcularPromedio(A, promed, pruebas):
    i=0
    while i<5:
        m=0
        while m<pruebas:
            promed[i]=promed[i]+A[i][m]
            m=m+1
        promed[i]=promed[i]/(pruebas)
        i=i+1

# Descripcion: imprime el tiempo promedio empleado por cada algoritmo de ordenamiento
# Parametros de entrada: 
#   promed: Arreglo que contiene el tiempo promedio de cada algoritmo
def imprimirPromedio(promed):
    i=0 
    while i<5:
        if i ==0:
            algoritmo="heapsort"
        elif i==1:
            algoritmo="median of 3 quicksort"
        elif i==2:
            algoritmo="introsort"
        elif i ==3:
            algoritmo="Quicsort with 3-way partition"
        else:
            algoritmo="Dual pivot Quicksort"
        print("Tiempo promedio usando " + algoritmo + ": " + str(promed[i]))
        i=i+1
