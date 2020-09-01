x = int(input())

if(x > 0):
  contador = 0
  i = 1
  while(x > contador):
    if(i % 2 != 0):
      print(i)
      contador += 1
    i += 1
