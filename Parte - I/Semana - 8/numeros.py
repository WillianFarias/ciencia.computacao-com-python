x = int(input("Valor: "))

if(x != 0):

  i = 0
  list = []
  list.append(x)

  while(x != 0):
    i = i + 1
    x = int(input("Valor: "))
    if(x != 0):
      list.append(x)

  j = - 1
  tamanho = len(list) * - 1

  while(tamanho <= j):
    print(list[j])
    j = j - 1
