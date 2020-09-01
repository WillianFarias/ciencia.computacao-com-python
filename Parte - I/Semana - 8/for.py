frutas = ["maçã", "pera"]

for fruta in frutas:
  print(fruta)

for i in range(5):
  print(i)

for i in range(10, 15):
  print("\n",i)

for i in range(10, 15, 3):
  print(i)

#pares de 0 a 40
pares = range(0, 40, 2)

for i in pares:
  print(i)

print("Regressao")
#regressao
for i in range(0, -10, -1):
  print(i)

primos = [2, 3, 5, 7, 11]

print("AQUI")
for i in range(len(primos)):
  primos[i] = primos[i] ** 3

print(primos)

pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
for x in range(5, 10):
    print(pares[x])

print("NOVO AQUI")
valores = []
for i in range(1, 10, 2):
    valores.append(i)
print(valores)

primos = [2, 3, 5, 7, 11, 13, 17]

#imprime o intervalo definido onde o ultimo valor é menos um
print(primos[1:3])

#do primeiro ao 3 - 1
print(primos[:3])

#do 3 ao ultimo
print(primos[3:])

lista1 = ["vermelho", "verde", "azul"]

def clone(lista):
  clone = []
  for x in lista:
    clone.append(x)
  return clone

lista2 = clone(lista1)
lista2[0] = "rosa"
print(lista2)
print(lista1)

#a funcao clone é o mesmo que lista2 = lista1[:]

#in verifica se esta contido
if "vermelho" in lista1:
  print("Está")

#concatenacao de listas
lista3 = lista1 + lista2
print(lista3)

#triplica lista
triplicada = lista1 * 3
print(triplicada)

#deletar elemento da lista
del triplicada[0]

del triplicada[1:5]

print(triplicada)