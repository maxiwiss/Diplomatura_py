import sys

val1 = int(sys.argv[1])
val2 = int(sys.argv[2])
val3 = int(sys.argv[3])
res1 = val1 % 2
res2 = val2 % 2
res3 = val3 % 2
if res1 == 0:
    print(val1, "es numero par")
else:
    print(val1, "no es numero par")
if res2 == 0:
    print(val2, "es numero par")
else:
    print(val2, "no es numero par")
if res3 == 0:
    print(val3, "es numero par")
else:
    print(val3, "no es numero par")
