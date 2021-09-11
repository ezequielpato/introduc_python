
""" Ejercicio 4:
    Realizar una fn mostrar, que reciba una lista de frutas y un numero, e imprima 
    un numero y el elemento asociado. 

    Ej: 

      frutas = ['Banana', 'kiwi', 'Pera', 'Naranja', 'Manzana']

      mostrar(frutas, 100)

      >>> 100 Banana
      >>> 101 kiwi
      >>> 102 Pera
      >>> 103 Naranja
      >>> 104 Manzana  """





frutas = ['Banana', 'kiwi', 'Pera', 'Naranja', 'Manzana']



def mostrar(una_lista, un_numero):
    ''' Esta fn recibe una lista y un numero, como resultado imprime el numero y un elemento asociado. '''
    for i, ele in enumerate(una_lista, un_numero):
        print(i," => ", ele )


mostrar(frutas, 1)



# mostrar(frutas, 100)

# for indice, elemento in enumerate(mi_lista, 1):
#     print(indice, " => ", elemento)