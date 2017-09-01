# Descripcion: Diversos algortmos de ordenamiento
# Autor: Juan Ortiz & Rubmary Rojas
# email: ortiz.juan14@gmail.com & rubmaryrojas@gmail.com

import sys, random, math

size_threshold = 15

######################### Insertion Sort ###############################
# Descripcion: algoritmo que ordena un elemento a la vez, comparandolo
# con los elementos ya ordenados e insertandolo en la posicion correcta
# Parametros de entrada:
# 	A: areglo de tamano N
#	p: extremo izquierdo del rango a ordenar
#	r: extremo derecho del rango a ordenar
# Precondicion: 0<=p<=q<N
# Postcondicion: el subarreglo A[p, p+1, ..., r] esta ordenado de forma
# no decreciente
def insertion_sort(A,p,r):
	i = p-1
	N = r+1
	while i < N:
		j = i
		while j > p and A[j-1] > A[j]:
			A[j-1], A[j] = A[j], A[j-1]
			j = j - 1
		i = i + 1

############################## Heapsort ###############################

# Descripcion: retorna el padre de un nodo
# Parametros de entrada:
#	i: indice del i-esimo elemento de la heap
# Precondicion: 0<i<=heap_size
# Postcondicion: Retorna el padre del nodo i
def Parent(i):
	return (int) ((i-1)/2);

# Descripcion: retorna el hijo izquierdo de un nodo
# Parametros de entrada:
#	i: indice del i-esimo elemento de la heap
# Precondicion: 0<=i<=heap_size
# Postcondicion: Retorna el hijo izquierdo del nodo i
def Left(i):
	return 2*i+1;


# Descripcion: retorna el hijo derecho un nodo
# Parametros de entrada:
#	i: indice del i-esimo elemento de la heap
# Precondicion: 0<=i<=heap_size
# Postcondicion: Retorna el hijo derecho del nodo i
def Right(i):
	return 2*(i+1);


# Descripcion: mantiene la propiedad de max-heap
# Parametros de entrada:
#	seq: arreglo con N elementos
#	i: raiz del subarbol que se arreglara
#	heap_size: tamano de la heap
# Precondicion: 0<=i<hep_size<=N
# Postcondicion: Permutacion del arreglo seq, que forma una heap valida
# enraizada en el nodo i
def Max_Heapify(seq, i, heap_size):
	l = Left(i)
	r = Right(i)
	if l < heap_size and seq[l] > seq[i]:
		largest = l
	else:
		largest = i
	if r < heap_size and seq[r] > seq[largest]:
		largest = r
	if largest != i:
		seq[i], seq[largest] = seq[largest], seq[i]
		Max_Heapify(seq, largest, heap_size)


# Descripcion: construye una heap binaria a partir de un arreglo.
# Se realiza de forma iterativa desde las hojas hasta la raiz
# Parametros de entrada:
#	seq: arreglo con N elementos
#	heap_size: tamano de la heap
# Precondicion: heap_size=N
# Postcondicion: Permutacion del arreglo A formando una heap valida
def Build_Max_Heap(seq, heap_size):
	i = (len(seq)-1)//2
	while i>=0:
		Max_Heapify(seq, i, heap_size)
		i = i-1

# Descripcion: algoritmo de ordenamiento basado en comparaciones que
# corre en tiempo O(nlogn). Ordena los elementos "in place" utilizando
# una estructura de datos denominada heap binaria
# Parametros de entrada:
#	seq: arreglo con N elementos a ordenar
# Precondicion: Los elementos son comparables
# Postcondicion: Permutacion del arreglo seq ordenado de forma no
# decreciente
def heap_sort(seq):
	heap_size = len(seq)
	Build_Max_Heap(seq, heap_size)
	i = (len(seq)-1)
	while i>0:
		seq[0], seq[i] = seq[i], seq[0]
		heap_size  = heap_size-1
		Max_Heapify(seq, 0, heap_size)
		i = i-1

# Descripcion: ordena un subarreglo utilizando heapsort
# Parametros de entrada:
#	A: arreglo de tamano N
#	f: extremo izquierdo del rango a ordenar
#	b: extremo derecho del rango a ordenar mas uno
# Precondicion: 0<=f<b<=N
# Postcondicion: el subarreglo A[f, f+1, ..., b-1] esta ordenado
# de forma no decreciente
def Heapsort(A, f, b):
	B = [A[i] for i in range(f, b)]
	heap_sort(B)
	for i in range(f, b):
		A[i] = B[i-f]

##################### Median-of-3 quicksort ############################

# Descripcion: retorna la mediana de tres elementos
# Parametros de entrada:
#	x, y, z: elementos a comparar
# Precondicion: x, y, z deben se comparables entre si
# Postcondicion: retorna la mediana de x, y, z
def median_of_3(x, y, z):
	S=[x, y, z]
	insertion_sort(S, 0, 2)
	return S[1]

# Descripcion: calcula la posicion del pivote y particiona el un rango  
# del arreglo en dos subarreglos divididos por la posicion del pivote.
# Parametros de entrada:
#	A: arreglo con N elementos
#	p, q: extremos del rango que se particiona
#	x: elemento utilizado como pivote
# Precondicion: 0<=p<=r<N
# Postcondicion: Devuelve la posicion q del pivote, y el el subarreglo 
# A[p..r] reordenado tal que A[i]<=A[q]<=A[j], para todo p<=i<q<j<=r
def partition(A, p, r, x):
    i = p-1
    j = r
    while True:
        while True:
            j = j-1
            if A[j] <= x:
                break
        while True:
            i = i+1
            if A[i] >= x:
                break
        if i<j:
            A[i], A[j] = A[j], A[i]
        else:
            return i


# Descripcion: retorna una permutacion del arreglo casi ordenado
# Parametros de entrada:
#	A: arreglo con N elementos
#	f, b: extremos del rango que se procesa
# Precondicion: 0<=f<b<=N
# Postcondicion: El arreglo es permutado tal que A[i]<=A[j], para todo 
# i, j tales que f<=i<j<b y size_thereshold < j-i
def quicksort_loop(A, f, b):
    while b-f> size_threshold:
        p=partition(A, f, b, median_of_3(A[f], A[f+(b-f)//2], A[b-1]))
        if p-f >= b-p:
            quicksort_loop(A, p, b)
            b=p
        else:
            quicksort_loop(A, f, p)
            f=p

# Descripcion: version de quicksort que toma como pivote la mediana de 
# tres elementos, y utiliza a insertion_sort para ordenar rangos de menores
# a size_threshold
# Parametros de entrada:
#	A: arreglo de tamano N
#	f: extremo izquierdo del rango a ordenar
#	b: extremo derecho del rango a ordenar mas uno
# Precondicion: 0<=f<b<=N
# Postcondicio: Permutacion del subarreglo A[f...b-1] ordenado de forma 
# no decreciente
def median_of_3_quicksort(A, f, b):
	quicksort_loop(A, f, b)
	insertion_sort(A, f, b-1)



########################## Intro-sort ##################################

# Descripcion: retorna una permutacion del arreglo casi ordenado,
# limitando la profundidad de la recursion
# Parametros de entrada:
#	A: arreglo con N elementos
#	f, b: extremos del rango que se procesa
# Precondicion: 0<=f<b<=N
# Postcondicion: El arreglo es permutado tal que A[i]<=A[j], para todo 
# i, j tales que f<=i<j<b y size_thereshold < j-i
def introsort_loop(A, f, b, depth_limit):
    while b-f>size_threshold:
        if depth_limit == 0:
            Heapsort(A, f, b)
            return
        depth_limit=depth_limit-1
        p=partition(A, f, b, median_of_3(A[f], A[f+(b-f)//2], A[b-1]))
        introsort_loop(A, p, b, depth_limit)
        b=p


# Descripcion: funcion que retorna la parte entera del logaritmo en base
# 2 de un numero
# Parametros de entrada: k
# Precondicion: k>0
# Postcondicion: retorna la parten entera de log_2(k)
def floor_lg(k):
	return math.floor(math.log(k, 2))


# Descripcion: version de quicksort que limita la profundidad de la
# recursion llamando a heapsort cuando esta alcanza un limite. Utiliza
# a insertion_sort para ordenar rangos de menores a size_threshold:
# Parametros de entrada:
#	A: arreglo de tamano N
#	f: extremo izquierdo del rango a ordenar
#	b: extremo derecho del rango a ordenar mas uno
# Precondicion: 0<=f<b<=N
# Postcondicio: Permutacion del subarreglo A[f...b-1] ordenado de forma 
# no decreciente
def introsort(A, f, b):
	introsort_loop(A, f, b, 2*floor_lg(b-f))
	insertion_sort(A, f, b-1)


################### Quicksort with 3-way partitioning ##################

# Descripcion: version de quicksort que excluye de las proximas llamadas
# recursivas todos los elementos iguales al pivote
# Parametros de entrada:
#	A: arreglo de tamano N
#	l: extremo izquierdo del rango a ordenar
#	r: extremo derecho del rango a ordenar
# Precondicion: 0<=l<N && 0<=r<N
# Postcondicio: si l<=r, entonces el subarreglo A[l, l+1, ..., r] esta
# ordenado de forma no decreciente

def quicksort3(A, l, r):
	i = l-1
	j = r
	p = l-1
	q = r
	v = A[r]
	if r <= l:
		return
	while True:
		i = i+1
		while A[i] < v:
			i = i+1
		j = j-1
		while v < A[j]:
			if j==l:
				break
			j = j-1
		if i>=j:
			break
		A[i], A[j] = A[j], A[i]
		if A[i]==v:
			p = p+1
			A[p], A[i] = A[i], A[p]
		if v==A[j]:
			q = q-1
			A[j], A[q] = A[q], A[j]
	A[i], A[r] = A[r], A[i]
	j = i-1
	i = i+1
	k = l
	while k<p:
		A[k], A[j] = A[j], A[k]
		k = k+1
		j = j-1
	k = r-1
	while k>q:
		A[i], A[k] = A[k], A[i]
		k = k-1
		i = i+1
	quicksort3(A, l, j)
	quicksort3(A, i, r)

####################### Dual pivot Quicksort ###########################

# Descripcion: version de quicksort que utiliza dos pivotes, los cuales 
# son el extremo izquierdo y el extremo derecho del rango a ordenar
# Parametros de entrada:
#	A: arreglo de tamano N
#	left: extremo izquierdo del rango a ordenar
#	right: extremo derecho del rango a ordenar
# Precondicion: 0<=left<=right<N
# Postcondicion: el subarreglo A[left, left+1, ..., right] esta ordenado
# de forma no decreciente
def quicksort_yaroslavskiy(A, left, right):
	if right-left < size_threshold:
		insertion_sort(A, left, right)
	else:
		if A[left]>A[right]:
			p = A[right]
			q = A[left]
		else:
			p = A[left]
			q = A[right]
		l = left + 1
		g = right - 1
		k = l
		while k<=g:
			if A[k]<p:
				A[k], A[l] = A[l], A[k]
				l = l+1
			else:
				if A[k]>=q:
					while A[g]>q and k<g:
						g = g-1
					if A[g]>=p:
						A[k], A[g] = A[g], A[k]
					else:
						A[k], A[g] = A[g], A[k]
						A[k], A[l] = A[l], A[k]
						l = l+1
					g = g-1
			k = k+1
		l = l-1
		g = g+1
		A[left] = A[l]
		A[l] = p
		A[right] = A[g]
		A[g] = q
		quicksort_yaroslavskiy(A, left, l-1)
		quicksort_yaroslavskiy(A, l+1, g-1)
		quicksort_yaroslavskiy(A, g+1, right)


############# Quicksort with 3-way partitioning randomizado ############

# Descripcion: version de quicksort que excluye de las proximas llamadas
# recursivas todos los elemtentos iguales al pivote, el cual es elegido 
# al azar
# Parametros de entrada:
#	A: arreglo de tamano N
#	l: extremo izquierdo del rango a ordenar
#	r: extremo derecho del rango a ordenar
# Precondicion: 0<=l<N && 0<=r<N
# Postcondicio: si l<=r, entonces el subarreglo A[l, l+1, ..., r] esta
# ordenado de forma decreciente
def quicksort3_randomizado(A, l, r):
	i = l-1
	j = r
	p = l-1
	q = r
	if r <= l:
		return
	piv = random.randint(l, r)
	A[r], A[piv] = A[piv], A[r]
	v = A[r]
	while True:
		i = i+1
		while A[i] < v:
			i = i+1
		j = j-1
		while v < A[j]:
			if j==l:
				break
			j = j-1
		if i>=j:
			break
		A[i], A[j] = A[j], A[i]
		if A[i]==v:
			p = p+1
			A[p], A[i] = A[i], A[p]
		if v==A[j]:
			q = q-1
			A[j], A[q] = A[q], A[j]
	A[i], A[r] = A[r], A[i]
	j = i-1
	i = i+1
	k = l
	while k<p:
		A[k], A[j] = A[j], A[k]
		k = k+1
		j = j-1
	k = r-1
	while k>q:
		A[i], A[k] = A[k], A[i]
		k = k-1
		i = i+1
	quicksort3_randomizado(A, l, j)
	quicksort3_randomizado(A, i, r)

################# Dual pivot Quicksort randomizado #####################

# Descripcion: version de quicksort que utiliza dos pivotes, los cuales
# son escogidos al azar
# Parametros de entrada:
#	A: arreglo de tamano N
#	left: extremo izquierdo del rango a ordenar
#	right: extremo derecho del rango a ordenar
# Precondicion: 0<=left<=right<N
# Postcondicion: el subarreglo A[left, left+1, ..., right] esta ordenado
# de forma no decreciente

def quicksort_yaroslavskiy_randomizado(A, left, right):
	if right-left < size_threshold:
		insertion_sort(A, left, right)
	else:
		p = A[random.randint(left, right)]
		q = A[random.randint(left, right)]
		if(p>q):
			p, q = q, p
		l = left + 1
		g = right - 1
		k = l
		while k<=g:
			if A[k]<p:
				A[k], A[l] = A[l], A[k]
				l = l+1
			else:
				if A[k]>=q:
					while A[g]>q and k<g:
						g = g-1
					if A[g]>=p:
						A[k], A[g] = A[g], A[k]
					else:
						A[k], A[g] = A[g], A[k]
						A[k], A[l] = A[l], A[k]
						l = l+1
					g = g-1
			k = k+1
		l = l-1
		g = g+1
		A[left] = A[l]
		A[l] = p
		A[right] = A[g]
		A[g] = q
		quicksort_yaroslavskiy_randomizado(A, left, l-1)
		quicksort_yaroslavskiy_randomizado(A, l+1, g-1)
		quicksort_yaroslavskiy_randomizado(A, g+1, right)






