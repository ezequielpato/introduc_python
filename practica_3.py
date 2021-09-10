""" 
=> Ejercicio 3:
Realiza una fn acumulado, que devuelva el valor acumulado 
de la suma de una lista de numeros mas 100.

Ej: 
  mis_numeros = [2, 4, 6]

  valor_final = acumulado(mis_numeros)

  print(mis_numeros)

  >>> 112
  
"""
from operator import itemgetter, add
from functools import reduce

mis_numeros = [2,4,6]

def acumulador(numeros):
  suma = reduce(lambda x, y: x + y, numeros)
  return suma + 100

print("suma ", acumulador(mis_numeros))