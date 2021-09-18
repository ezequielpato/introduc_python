"""Ejercicio 4
Genenerar su propia funcion enumerate que agrega un contador a un 
iterable y lo devuelva en forma de objeto enumerador. 
Por ultimo convertirlo en un diccionario e imprimirlo.

  Ej: 
    objeto_enumerado = myEnumerate(
    ["Pasta", "Ensalada", "Bebida", "Carne", "Aperitivo"], 10)

    print(dict(list(objeto_enumerado)))
    
    >>> {10: 'Pasta', 11: 'Ensalada', 12: 'Bebida', 13: 'Carne', 14: 'Aperitivo'}
"""

comidas = ["Pasta", "Ensalada", "Bebida", "Carne", "Aperitivo"]

def myEnumerate(param, cont):
    for ele in param:
       yield (cont, ele)
       cont += 1

#resultado = myEnumerate(comidas, 10)

#print(dict(list(resultado)))

#print(  dict( list( myEnumerate(comidas,10) ) ) )
