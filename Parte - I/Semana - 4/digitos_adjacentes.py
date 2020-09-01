x = int(input())

adjacente = True

if(x != 0):
  while adjacente:
    valor1 = x % 10
    #print("valor1", valor1)
    resto = x // 10
    #print(resto)

    valor2 = resto % 10
    #print("valor2",valor2)
    x = resto 
    #print("novo x: ",x)

    if(valor1 == valor2):
      adjacente = False

    if(x == 0):
      break
  if(not adjacente):
    print("sim")
  else:
    print("não")
else:
  print("não")