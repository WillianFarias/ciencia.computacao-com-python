def maior_elemento(lista):
  
  tamanho = len(lista)
  maior = lista[0]

  for i in range(tamanho):
    if(maior < lista[i]):
      maior = lista[i]

  return maior
