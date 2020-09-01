largura = int(input("Largura: "))
altura = int(input("Altura: "))

j = 0
i = 0

while(altura > i):
  while(largura > j):
    if(i == 0 or i == (altura - 1)):
      print("#", end='')
      j = j + 1
    elif(j == 0 or j == (largura - 1)):
     print("#", end='')
    

  print("")
  j = 0
  i = i + 1 
