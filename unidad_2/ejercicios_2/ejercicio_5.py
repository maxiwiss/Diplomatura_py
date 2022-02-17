from cmath import pi


def perimetro_cir(radio):
    perimetro = 2 * pi * radio
    print("El perimetro de la circunferencia es: ", perimetro)


def area_cir(radio):
    area = pi * radio**2
    print("El area de la circunferencia es: ", area)


def incremento(numero):
    print("Valor ingresado incrementado un 10%: ", numero * 1.1)


valor = int(input("Ingrese el radio de una circunferencia: "))
perimetro_cir(valor)
area_cir(valor)
incremento(valor)
