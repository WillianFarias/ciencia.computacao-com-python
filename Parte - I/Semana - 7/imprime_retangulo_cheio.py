largura = int(input("Largura: "))
altura = int(input("Altura: "))

i = 0
j = 0

while(altura > i):
  while(largura > j):
    print("#", end='')
    j = j + 1

  print()
  j = 0
  i = i + 1 

