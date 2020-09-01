x = int(input())
verificador = 0

if(x > 0 and x != 1):
  i = 2
  while(x > i):
    if(x % i == 0):
      print("não primo")
      verificador = 1
      break
    i += 1
  if(verificador == 0):
    print("primo")
else:
  print("não primo")