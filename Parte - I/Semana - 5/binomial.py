def fatorial(x):
  if(x == 0):
    return 1

  elif(x > 0):
    i = 1
    fatorial = 1
    while(i <= x):
      fatorial *= i
      i += 1
    return fatorial

def principal():
  n = int(input("n: "))
  k = int(input("k: "))

  binomial = fatorial(n) / (fatorial(k) * fatorial(n - k))
  
  return print(binomial)

principal()