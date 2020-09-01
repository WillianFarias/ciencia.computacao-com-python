largura = int(input("Largura: "))
altura = int(input("Altura: "))

i = 0
j = 0

while(altura > i):
  while(largura > j):
    if(i == 0 or i == (altura - 1)):
      print("#", end='')
    elif(j == 0 or j == (largura - 1)):
      print("#", end='')
    else:
      print(" ", end='')
    j = j + 1

  print("")
  j = 0
  i = i + 1 

