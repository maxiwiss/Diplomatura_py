"""...ejercicio 2 unidad 1: modulo sys, desde la terminal
se pasan 3 parametros y se determinan
si los numeros son multiplo de 2.."""
import sys

if _name_ == "_main_":
    if len(sys.argv) != 4:
        print("debe ingresar 3 numeros")
        sys.exit(1)
    else:
        n1 = int(sys.argv[1]) % 2
        n2 = int(sys.argv[2]) % 2
        n3 = int(sys.argv[3]) % 2
        if n1 == 0:
            print("el primer numero es multiplo de 2 ")
        else:
            print("el primer parametro no es multiplo de 2")
        if n2 == 0:
            print("el segundo numero es multiplo de 2 ")
        else:
            print("el segundo parametro no es multiplo de 2")
        if n3 == 0:
            print("el tercer numero es multiplo de 2 ")
        else:
            print("el tercer parametro no es multiplo de 2")
sys.exit(0)
