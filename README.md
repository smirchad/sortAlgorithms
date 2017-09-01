# Estudio experimental de algoritmos de ordenamiento

Se realizo un estudio experimental sobre algoritmos de ordenamiento, comparando heapsort y algunas variantes de de quicksort. Para cada uno de los algoritmos se hicieron pruebas con arreglos de diferentes tamaños con los conjuntos numéricos especificados. También se hicieron unas pruebas adicionales con un par de algoritmos modificados.

# Uso
El proyecto fue desarrollado con Python en su versión 2.7 y se ejecuta con la siguiente llamada:
<br />  >python prueba_proyecto1 <numero de elementos> <dataset> <numero de pruebas>
<br />
<br>Donde el parámetro < numero de elementos > es el número de elementos que va a tener el arreglo a ordenar, < dataset > es el número del conjunto de datos a ejecutar, dada la numeración descrita anteriormente, y < numero de pruebas > es la cantidad de pruebas a realizar. Tenga en cuenta que como se elimina el peor y el mejor tiempo de cada prueba, entonces el menor número de pruebas permitido es 3. Un ejemplo de la llamado de la línea de comando es:
<br />  >python prueba_proyecto1 4096 7 10
