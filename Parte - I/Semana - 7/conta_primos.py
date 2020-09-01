def n_primos(x):

  contador = 0
  
  while(x >= 2):

    primo = True

    i = 2
    if(x == 2):
      primo = True
      contador = contador + 1
    else:
      while(x > i):
        if(x % i == 0):
          primo = False
        i = i + 1
      #return primo
      if(primo) :
        contador = contador + 1

    x = x - 1

  return contador
  




