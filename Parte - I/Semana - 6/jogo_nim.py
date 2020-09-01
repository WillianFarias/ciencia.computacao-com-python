def computador_escolhe_jogada(n, m):
  
  valor_computador = m
  i = 1

  while(i <= m):

    if((n - i) % (m+1) == 0 ):
      valor_computador = i

    i = i + 1

  return valor_computador


def usuario_escolhe_jogada(n, m):
  
  retirada_usuario = int(input("\nQuantas peças você vai tirar: "))

  continua = True
  while(continua):
    if(retirada_usuario <= m and retirada_usuario > 0):
      continua = False
    else:
      print("\nOops! Jogada inválida! Tente de novo.\n")
      retirada_usuario = int(input("\nQuantas peças você vai tirar: "))

  return retirada_usuario

def jogo():
  
  n = int(input("\nTotal de peças: "))
  m = int(input("Máximo de peças por jogada: "))

  if(n % (m+1) == 0):
    print("\nVocê comeca!")

    while(n > 0):

      pecas_usuario = usuario_escolhe_jogada(n, m)
      print("\nVocê tirou {} peça(s)".format(pecas_usuario))
      n = n - pecas_usuario
      
      if(n > 0):

        print("\nAgora restam {} peça(s) no tabuleiro".format(n))

        pecas_computador = computador_escolhe_jogada(n, m)
        print("\nComputador tirou {} peça(s)".format(pecas_computador))
        n = n - pecas_computador

      if(n > 0):
        
        print("\nAgora restam {} peça(s) no tabuleiro".format(n))
        
      else:
        print("\nFim do jogo! Computador ganhou")

  else:
    print("\nComputador começa!")
    while(n > 0):

      pecas_computador = computador_escolhe_jogada(n, m)
      print("\nComputador tirou {} peça(s)".format(pecas_computador))
      n = n - pecas_computador
      
      if(n > 0):

        print("\nAgora restam {} peças no tabuleiro".format(n))

        pecas_usuario = usuario_escolhe_jogada(n, m)
        print("\nVocê tirou {} peça(s)\n".format(pecas_usuario))
        n = n - pecas_usuario

        print("\nAgora restam {} peças no tabuleiro".format(n))

      else:
        print("\nFim do jogo! Computador ganhou")

def partida():

  print("Bem vindo ao jogo do NIM! Escolha:")
  print("\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato")

  escolha = int(input())

  if(escolha == 1):
    jogo()
  elif(escolha == 2):
    i = 1
    while(i <= 3):
      print("**** Rodada {} ****".format(i))
      jogo()
      i = i + 1
    print("**** Final do campeonato! ****\n\nPlacar: Você 0 X 3 Computador")

partida()