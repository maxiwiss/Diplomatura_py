# Defino listas
persona1 = ["Pepe Pedro", "Perez", 4, "12345678", "30000"]
persona2 = ["Anna", "Perez", 12, "12345622", "43000"]
persona3 = ["Josefa", "Rodriguez", 4, "12345563", "50000"]

# Lista de lista

lista_de_lsitas = [persona1, persona2, persona3]
# print(lista_de_lsitas)

# Defino diccionarios

dic_persona1 = {
    "nombre": "Pepe Pedro",
    "apellido": "Perez",
    "edad": 4,
    "telefono": "123445678",
    "sueldo": "30000",
}
dic_persona2 = {
    "nombre": "Anna",
    "apellido": "Perez",
    "edad": 12,
    "telefono": "12345622",
    "sueldo": "43000",
}
dic_persona3 = {
    "nombre": "Josefa",
    "apellido": "Rodriguez",
    "edad": 4,
    "telefono": "12345563",
    "sueldo": "50000",
}

# Diccionario de Diccionarios
# Simulé un diccionario que contiene los datos
# personales de un equipo de trabajo

Personal = {
    "senior": dic_persona1,
    "junior": dic_persona2,
    "projectm": dic_persona3,
}
# print(Personal)

# Lista de Diccionarios

lista_de_diccionarios = [dic_persona1, dic_persona2]
# print(lista_de_diccionarios)

# prueba de .append , .extend y .split

apend = lista_de_diccionarios
apend.append(dic_persona3)
print(apend)
# append agrega el objeto tal cual es
print("---" * 30)
exten = lista_de_diccionarios
exten.extend(dic_persona3)
print(exten)
# extend agrega el objeto en forma de elementos de lista
print(Personal["senior"]["nombre"].split()[-2])
print(dic_persona1["apellido"].split())
