# => Ejercicio 1:
#     Realiza una función separar(lista) que tome una lista de números enteros.
#     y devuelva dos listas la primera con los números pares.
#     y la segunda con los números impares.

#     Ej:
#         pares, impares = separar([6,5,2,1,7])
#         print(pares)
#         print(impares)

#         >>> [2, 6]
#         >>> [1, 5, 7]


# INICIO DE EJERCICIO:

numeros = [6,5,2,1,7]

def separar(iterable: list[int]) -> tuple [list, list]:

    """
    La función recibe como parámetro una colección de números y devuelve una tupla
    de listas.

    La primera es una lista de números pares.
    La segunda es una lista de números impares.
    """

    numeros_pares = list(filter(lambda x: x % 2 == 0, iterable))
    numeros_impares = list(filter(lambda x: x % 2 != 0, iterable))
    return (numeros_pares, numeros_impares)

pares, impares = separar(numeros)

print(pares)
print(impares)