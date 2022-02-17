import sys

val1 = int(sys.argv[1])
val2 = int(sys.argv[2])
val3 = int(sys.argv[3])

res1 = val1 % 2
res2 = val2 % 2
res3 = val3 % 2

print("Si el resto del numero dividido 2 es 0, se trata de un numero par")
print("el resto de", val1, "dividido 2 es:", res1)
print("el resto de", val2, "dividido 2 es:", res2)
print("el resto de", val3, "dividido 2 es:", res3)
