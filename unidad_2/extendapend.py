lista2 = ["casa", "piedra", "jaula"]
lista1 = ["perro", "gato", "loro"]

lista_apend = lista1
lista_apend.append(lista2)
print(lista_apend)


lista1 = ["perro", "gato", "loro"]
lista2 = ["casa", "piedra", "jaula"]


lista_apend = lista1
lista_apend.extend(lista2)
print(lista_apend)
