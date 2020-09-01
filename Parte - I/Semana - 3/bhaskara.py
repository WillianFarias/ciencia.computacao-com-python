#equações quadráticas apenas de números inteiros
import math

a = int(input())
b = int(input())
c = int(input())

possuiRaiz = (b**2 - 4 * a * c) >= 0

if(possuiRaiz):
  delta = b**2 - 4 * a * c
  if(delta > 0):
    x = (-b + math.sqrt(delta))/2*a
    y = (-b - math.sqrt(delta))/2*a
    if(x < y):
      print("as raízes da equação são {} e {}".format(x, y))
    else:
      print("as raízes da equação são {} e {}".format(y, x))
  else:
    x = (-b + math.sqrt(delta))/2*a
    print("a raiz desta equação é {}".format(x))

else:
  print("esta equação não possui raízes reais")




