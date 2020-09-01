x = int(input())

if(x == 0):
  print(1)

elif(x > 0):
  i = 1
  fatorial = 1
  while(i <= x):
    fatorial *= i
    i += 1
  print(fatorial)