""" 

=> Ejercicio 2:
  Realiza una función que tome como parametro una frase y devuelva una 
  lista de palabras en mayuscula. 

    Ej: 
      mi_frase = "Este sabado tenemos el ultimo encuentro online"

      palabras = convertir(mi_frase)

      print(palabras)

      >>> ["ESTE", "SABADO", "TENEMOS", "EL", "ULTIMO", "ENCUENTRO", "ONLINE"]
      
"""
from operator import itemgetter, add
from functools import reduce

mi_frase = "Este sabado tenemos el ultimo encuentro online"

def convertir(frase):
  return frase.split(' ')

print("frase completa ",mi_frase)

mi_frase = convertir(mi_frase)

print("frase separada ",mi_frase)