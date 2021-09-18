"""Ejercicio 2
Genenerar su propia funcion filter, que tome como parametro 
una funcion y una coleccion, devolviendo solo aquellos elementos
que cumplan con la condicion de dicha fn pasada como param.
Luego pasar el objeto resultante por una fn list() e imprimirlo.

  Ej: 
    objeto_resultante = myFilter(lambda x: x > 3, [3, 1, 10, 8, 6, 2])

    print(list(objeto_resultante))
    
    >>> [10, 8, 6]
"""

# filter devuelve un bool.

numbers = [3,1,10,8,6,2]

def filtro(func,coleccion):
    for i in coleccion:
        if func(i):       # segunda condición 
            yield i

resultado = filtro(lambda x: x > 3, numbers)

print(list(resultado)) 