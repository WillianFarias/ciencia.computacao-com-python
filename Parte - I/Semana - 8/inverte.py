n = int(input("valor: "))
lista = []

while(n != 0):
  lista.append(n)
  
  n = int(input("valor: "))

tamanho = (len(lista) * -1) - 1

for i in range(-1, tamanho, -1):
  print(lista[i])
