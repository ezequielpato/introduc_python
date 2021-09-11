"""  => Ejercicio 6:
      Extender el ejercicio anterior, crear una función ordenarPorCategoria 
      que reciba como param el diccionario, que devuelve la función asociar, 
      y devuelva un nuevo diccionario ordenado por categoria.

      Ej: 
        print(ordenarPorCategoria(diccionario))

        >>> {
          'Roberto': 'Categoria A', 
          'Juli': 'Categoria B', 
          'Carlos': 'Categoria C', 
          'Marta': 'Categoria D'
          } """

empleado = ['Juli', 'Carlos', 'Roberto', 'Marta']
categoria = ['Categoria B', 'Categoria C', 'Categoria A', 'Categoria D']

""" método corto usando la FN zip """
def asociar(lista_emp, lista_cat):
    diccionario = dict(zip(lista_emp,lista_cat))
    return diccionario
""" seleccionar elemento por el cual sorted ordena el diccionario """
def segundoElemento(una_lista):
    return una_lista[1]

def ordenarPorCategoria(lista_a_ordenar):
    # transformamos el diccionario en una lista para el metodo key
    print("lista completa:",lista_a_ordenar)
    # ordenamos la lista mediante el metodo
    return sorted(lista_a_ordenar.items(), key=segundoElemento)
    
diccionario_resultado = asociar(empleado, categoria)
diccionario_ordenado = ordenarPorCategoria(diccionario_resultado)

print(dict(diccionario_ordenado))


# def ordenarPorCategoria(dic_a_ordenar):
#     #transformamos el diccionario en una lista para el metodo key
#     lista = dic_a_ordenar.items()
#     #ordenamos la lista mediante el metodo sorted
#     lista_ordenada = sorted(lista, key=segundoElemento)
#     #antes de devolver la lista lo convertimos en diccionario
#     return dict(lista_ordenada)
# #creamos el diccionario
# diccionario_resultado = asociar(empleado, categoria)
# #mandamos a ordenar el diccionario mediante la Categoria
# diccionario_ordenado = ordenarPorCategoria(diccionario_resultado)
# #imprimimos el diccionario
# print(diccionario_ordenado)