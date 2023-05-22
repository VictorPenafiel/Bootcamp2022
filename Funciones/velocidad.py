# Función para calcular el promedio de una lista
def promedio(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma/len(lista)

# Función para calcular las posiciones de los elementos mayores que un valor dado en una lista
def calcula_pos(lista,valor):
    resultado = []
    for pos, item in enumerate(lista):
        if item > valor:
            resultado.append(pos)
    return resultado

# Lista de velocidades
velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23,21]

# Calcular el promedio de las velocidades
prom = promedio(velocidad)

# Imprimir las posiciones de los elementos en la lista de velocidades que son mayores que el promedio
print(calcula_pos(velocidad,prom))

""" explicame este codigo:def promedio(lista): suma = 0 for i in lista: suma = suma + i return suma/len(lista) def calcula_pos(lista,valor): resultado = [] for pos, item in enumerate(lista): if item > valor: resultado.append(pos) return resultado velocidad = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19, 14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22, 14, 1, 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5, 23, 20, 23,21] prom = promedio(velocidad) print(calcula_pos(velocidad,prom))
Answer

Este código define dos funciones, promedio y calcula_pos, y luego utiliza estas funciones para calcular el promedio de una lista de velocidades y encontrar las posiciones de los valores en la lista que son mayores que el promedio.

La función promedio toma como argumento una lista y calcula el promedio de sus elementos. Para ello, realiza los siguientes pasos:

    Inicializa una variable suma en 0.
    Itera sobre cada elemento i de la lista y suma su valor a la variable suma.
    Una vez que se han sumado todos los elementos, divide la suma por la cantidad de elementos en la lista (len(lista)) y devuelve el resultado.

La función calcula_pos toma dos argumentos, una lista y un valor, y devuelve una lista con las posiciones de los elementos en la lista que son mayores que el valor proporcionado. Para ello, realiza los siguientes pasos:

    Inicializa una lista vacía llamada resultado.
    Itera sobre la lista usando la función enumerate, que devuelve tanto la posición (pos) como el elemento (item) en cada iteración.
    Si el elemento (item) es mayor que el valor proporcionado, agrega su posición (pos) a la lista resultado.
    Devuelve la lista resultado al finalizar la iteración.

El código luego crea una lista de velocidades y calcula su promedio utilizando la función promedio. Finalmente, imprime las posiciones de los elementos en la lista de velocidades que son mayores que el promedio calculado, utilizando la función calcula_pos.
 """