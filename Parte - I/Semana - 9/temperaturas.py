def temperaturas(lista):
  
  maior_temperatura = menor_temperatura = lista[0]
  tamanho = len(lista)

  for i in range(tamanho):
    if(maior_temperatura < lista[i]):
      maior_temperatura = lista[i]
    
    if(menor_temperatura > lista[i]):
      menor_temperatura = lista[i]

  print(maior_temperatura, menor_temperatura)

lista = [20, 35, 10, 91, -1]

temperaturas(lista)
  