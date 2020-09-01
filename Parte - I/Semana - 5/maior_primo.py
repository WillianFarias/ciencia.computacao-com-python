def primo(x):

  if(x == 1):
    return False

  elif(x > 1):
    i = 2
    primo = True

    while(x > i):
      if(x % i == 0):
        primo = False
      i = i + 1
    return primo

def maior_primo(x):

  while(x >= 1):
    if(primo(x)):
      return x
    else:
      x = x - 1

