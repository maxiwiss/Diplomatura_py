import os


def directorio(param1):

    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    ruta = os.path.join(BASE_DIR)

    objetivo = param1
    lista = objetivo.split("/")

    i = 0
    while i < len(lista):
        ruta = os.path.join(BASE_DIR, lista[i])
        i = +1
    return ruta
