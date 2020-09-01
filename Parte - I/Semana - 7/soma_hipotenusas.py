import math

def soma_hipotenusas(n):

  somador = 0
  j = i = 1

  while(i < n):
    while(j < n):
      if(math.sqrt((i**2) + (j**2)) == n):
        somador =somador + n
        n = n - 1
        
      j = j + 1

    j = 1
    i = i + 1
    
    if(i >= n):
      n = n - 1
      i = 1

  return somador

