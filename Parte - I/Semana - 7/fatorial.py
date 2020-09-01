valor = int(input("Valor: "))

while(valor >= 0):

  fatorial = 1
  i = 1

  if(valor == 0):
    print(fatorial)
  else:
    while(i <= valor):
      fatorial = fatorial * i
      i = i + 1
    
    print(fatorial)

  valor = int(input("Valor: "))
  