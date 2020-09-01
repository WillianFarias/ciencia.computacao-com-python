#se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi
#dado na entrada.

x = int(input())

if(x % 5 == 0):
  print("Buzz")
else:
  print(x)