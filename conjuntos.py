# Descripcion: Procedimiento que crea las listas de numeros
# segun el tipo indicado
# Autor: Juan Ortiz & Rubmary Rojas
# email: 13-11021@usb.ve & rubmaryrojas@gmail.com

import sys, traceback, random, time


# Descripcion: crea la sequencia 1, 2, ..., N/2, N/2, N/2-1, ..., 2, 1
# Parametros:
#	N: Numero de elementos del arreglo
# Precondicion: N es un numero natural
# Postcondicion: Retorna un objeto lista con la sequencia indicada
def mitad(N):
    C = [0 for i in range(N)]
    for i in range(N//2):
        C[i] = i+1
    for i in range(N//2, N):
        C[i] = N-i
    return C

# Descripcion: crea una sequencia ordenada de N elementos e intercambia
# 16 pares de elementos separados 8 lugares
# Parametros:
#	N: Numero de elementos del arreglo
# Precondicion: N es un numero natural
# Postcondicion: Retorna un objeto lista con la sequencia indicada
def casi_ordenado1(N):
    C = sorted([random.randint(0, 100000) for x in range(N)])
    used = [False for i in range(N)]
    for j in range(16):
        i = 0
        while True:
            i = random.randint(0, N-9)
            if not (used[i] or used[i+8]):
                break
        C[i], C[i+8] = C[i+8], C[i]
        used[i] = True
        used[i+8] = True
    return C

# Descripcion: crea una sequencia ordenada de N elementos e intercambia
# N/4 pares de elementos separados 4 lugares
# Parametros:
#	N: Numero de elementos del arreglo
# Precondicion: N es un numero natural
# Postcondicion: Retorna un objeto lista con la sequencia indicada
def casi_ordenado2(N):
    C = sorted([random.randint(0, 100000) for x in range(N)])
    used = [False for i in range(N)]
    for j in range(N/4):
        while True:
            i = random.randint(0, N-5)
            if not (used[i] or used[i+4]):
                break
        C[i], C[i+4] = C[i+4], C[i]
        used[i]   = True
        used[i+4] = True
    return C


# Descripcion: crea arreglo con n valores que son generados de forma aleatoria
# Parametros:
#	n: Numero de elementos del arreglo
#	dataset: Tipo de datos que se generara
# Precondicion: N es un numero natural && 0<dataset<=7
# Postcondicion: Retorna un objeto lista con n valores del tipo que corresponda 
def obtenerArreglo(n, dataset):
    if dataset == 1:
        return [random.random() for x in range(n)]
    elif dataset == 2:
        return sorted([random.randint(0, 100000) for x in range(n)])
    elif dataset == 3:
        return sorted([random.randint(0, 100000) for x in range(n)], reverse=True)
    elif dataset == 4:
        return [random.randint(0, 1) for x in range(n)]
    elif dataset == 5:
        return mitad(n)
    elif dataset == 6:
        return casi_ordenado1(n)
    else:
        return casi_ordenado2(n)
