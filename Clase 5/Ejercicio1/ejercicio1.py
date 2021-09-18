"""Ejercicio 1
Genenerar su propia funcion map, que tome como parametro 
una funcion y una coleccion, aplicando dicha fn recibida como
param y se la aplique a cada elemento de la coleccion, retornando 
un objeto generador.
Luego pasar el objeto resultante por una fn list() e imprimirlo.

  Ej: 
    objeto_resultante = myMap(lambda x: x + 3, range(10))

    print(list(objeto_resultante))
    
    >>> [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""

# Método 1

def miFuncion(mi_lista):
    for ele in mi_lista:
        yield ele

retorno = miFuncion(range(3,13))

print(list(retorno))

#Método 2

def miFuncion(func,mi_lista):
    for ele in mi_lista:
        yield func(ele)    

retorno = miFuncion(lambda x: x + 3, range(10))

print(list(retorno))

