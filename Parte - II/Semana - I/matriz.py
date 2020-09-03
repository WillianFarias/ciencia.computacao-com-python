def cria_matriz(num_linhas, num_colunas, valor):
  matriz = []
  for i in range(num_linhas):
    #cria a linha i
    linha = []
    for j in range(num_colunas):
      linha.append(valor)
    matriz.append(linha)
  
  return matriz

print(cria_matriz(3, 3, 1))