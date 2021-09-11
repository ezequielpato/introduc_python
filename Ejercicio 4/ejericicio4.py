""" => Ejercicio 4:
    Realizar una fn mostrar, que reciba una lista de frutas y un numero, e imprima 
    un numero y el elemento asociado. 

    Ej: 

      frutas = ['Banana', 'kiwi', 'Pera', 'Naranja', 'Manzana']

      mostrar(frutas, 100)

      >>> 100 Banana
      >>> 101 kiwi
      >>> 102 Pera
      >>> 103 Naranja
      >>> 104 Manzana 
 """


frutas = ['Banana', 'kiwi','Pera','Naranja','Manzana']

def mostrar(lista, numero):
	for i, ele in enumerate(lista, numero):
		print(i, " =>", ele )

mostrar(frutas, 1)