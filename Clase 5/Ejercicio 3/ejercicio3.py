import functools

"""Ejercicio 3
Genenerar su propia funcion reduce, que tome como parametro 
una funcion y una coleccion, devolviendo el acumulador resultante.
Luego imprimirlo.

  Ej: 
    acumulador = myReduce(lambda x, b: x + b, [3, 1, 10, 8, 6, 2])

    print(acumulador)
    
    >>> 30
"""
#Método 1

#list = [3, 1, 10, 8, 6, 2]

print(functools.reduce(lambda x, b: x + b, [3, 1, 10, 8, 6, 2]))

#Método 2

def my_reduce(func,numbers,acumulador=0):
    for i in numbers:
        acumulador = func(acumulador, i)
    return acumulador

resultado = my_reduce(lambda x, b: x + b, [3, 1, 10, 8, 6, 2])

#print(resultado)