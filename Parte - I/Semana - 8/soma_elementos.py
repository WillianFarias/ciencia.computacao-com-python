def soma_elementos(lista):

  soma = 0
  tamanho = len(lista)

  for i in range(tamanho):
    soma = soma + lista[i]
  
  return soma

lista = [1, 2, 3]

print(soma_elementos(lista))
