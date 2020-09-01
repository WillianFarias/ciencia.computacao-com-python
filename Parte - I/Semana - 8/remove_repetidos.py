def remove_repetidos(lista):

  lista_ordenada = sorted(lista)
  lista_repetidos = []
  tamanho  = len(lista_ordenada) - 1
  
  for i in range (tamanho):
    if(lista_ordenada[i] != lista_ordenada[i + 1]):
      lista_repetidos.append(lista_ordenada[i])
      if(i == tamanho - 1):
        lista_repetidos.append(lista_ordenada[i + 1])
      #lista_repetidos.append(lista_ordenada[i + 1])
      #i = i + 1 

  return lista_repetidos
