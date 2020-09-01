valor = int(input("Valor: "))

while(valor >= 2):

  primo = True
  i = 2

  while(i < (valor // 2)):
    if(valor % i == 0):
      primo = False
    i = i + 1

  if(primo):
    print("Primo")
  else:
    print("Não primo")

  valor = int(input("Valor: "))

    
    

