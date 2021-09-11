""" => Ejercicio 5:
      Realizar una función asociar() que reciba como parametro dos listas 
      de la misma longitud de elementos y devuelva un diccionario de pares 
      clave-valor asociando cada elemento de ambas listas segun su indice. 

      Ej:
        empleado = ['Juli', 'Carlos', 'Roberto', 'Marta']
        categoria = ['Categoria B', 'Categoria C', 'Categoria A', 'Categoria D']

        diccionario = asociar(empleado, categoria)

        print(diccionario)

        >>> {
            'Juli': 'Categoria B', 
            'Carlos': 'Categoria C', 
            'Roberto': 'Categoria A', 
            'Marta': 'Categoria D'
          } """

""" método largo """

# empleado = ['Juli', 'Carlos', 'Roberto', 'Marta']
# categoria = ['Categoria B', 'Categoria C', 'Categoria A', 'Categoria D']

# def asociar(lista_emp, lista_cat):
#     diccionario = {}
#     cantidad_elementos = len(lista_emp)
#     x=0
#     while (x < cantidad_elementos):
#         diccionario[lista_emp[x]] = lista_cat[x]
#         x+=1
#     print(diccionario)
# asociar(empleado, categoria)



""" método corto usando zip() """

# def asociar2(lista_emp, lista_cat):
#     diccionario = dict(zip(lista_emp,lista_cat))
#     return diccionario

# diccionario_resultado = asociar2(empleado,categoria)
# print(diccionario_resultado)



