"""
Ejercicios para las funciones de orden superior

=> Ejercicio 1:
Realiza una función separar(lista) que tome una lista de números enteros 
y devuelva dos listas la primera con los números pares 
y la segunda con los números impares.

Ej:
  pares, impares = separar([6,5,2,1,7])
  print(pares)
  print(impares)

  >>> [2, 6]
  >>> [1, 5, 7]        
"""

numeros = [1,2,3,4,5,6,7,8,10]

def separar(iterable):
  numero_pares = list(filter(lambda x: x%2 == 0, iterable))
  numero_impares = list(filter(lambda x: x%2 != 0, iterable))
  return (numero_pares, numero_impares)

pares, impares = separar(numeros)

print("pares",pares)
print("impares",impares)

