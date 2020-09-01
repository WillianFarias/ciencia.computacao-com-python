valor = int(input("Valor: "))

if(valor > 0):
  
  i = 2

  while(i <= (valor)):
    if(valor % i == 0):
      valor = valor // i
      print(i)
    else:
      i = i + 1