def cria_matriz():

  num_linhas = int(input("Linha(s): "))
  num_colunas = int(input("Coluna(s): "))
  matriz = []

  for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
      valor = int(input("Informe o valor da posição [{}][{}]: ".format(i, j)))
      linha.append(valor)
    matriz.append(linha)
  
  return matriz


def imprime_matriz(matriz):
  for i in range(len(matriz)):
    print(matriz[i])

imprime_matriz(cria_matriz())