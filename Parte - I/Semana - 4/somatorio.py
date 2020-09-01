x = int(input("Valor: "))
soma = 0

while (x > 0):
  valor = x % 10
  soma += valor
  x = x // 10
print(soma)