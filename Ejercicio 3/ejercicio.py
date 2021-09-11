from functools import reduce
from operator import add
"""   => Ejercicio 3:
    Realiza una fn acumulado, que devuelva el valor acumulado 
    de la suma de una lista de numeros mas 100.

    Ej: 
      mis_numeros = [2, 4, 6]

      valor_final = acumulado(mis_numeros)

      print(mis_numeros)

      >>> 112 """

# lista de numeros
mis_numeros = [2, 4, 6]


def acumulado(una_lista: list[int], inicio_acumulador=0) -> int:
    """ La fn recibe como param una lista de numeros,
      devuelve el valor acumulado inicializando el acumulador 
      en un valor determinado."""
    return reduce(add, una_lista, inicio_acumulador)


valor_final = acumulado(mis_numeros, 100)

print(valor_final)
