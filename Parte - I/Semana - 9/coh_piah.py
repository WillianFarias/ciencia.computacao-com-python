import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma 
    assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista 
    contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do 
    texto'''
    #expressao regular
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da 
    sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras 
    que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras 
    diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver
    o grau de similaridade nas assinaturas.'''
    valor_absoluto = 0

    for i in range(0, len(as_a), 1):
        valor_absoluto += abs(as_a[i] - as_b[i])
    
    valor_absoluto /= 6

    return valor_absoluto

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do 
    texto.'''
    #Tamanho médio de palavras
    valores_assinatura = []

    tamanho_medio_palavras = 0

    sentencas = separa_sentencas(texto)

    frases = []
    caracteres_frase = 0

    for sentenca in sentencas:
        frases.append(separa_frases(sentenca))

    palavras = []

    qtd_frases = 0

    for frase in frases:
        for fra in frase:
            palavras.append(separa_palavras(fra))
            qtd_frases += 1
            caracteres_frase += len(fra)
        
    tamanho = 0
    contador_de_palavras = 0

    palavras_sem_pontuacao = []

    for palavra in palavras:
        for pala in palavra:
            tamanho += len(pala)
            contador_de_palavras += 1
            palavras_sem_pontuacao.append(pala)

    tamanho_medio_palavras = (tamanho/contador_de_palavras)

    #Relação Type-Token
    palavras_diferentes = n_palavras_diferentes(palavras_sem_pontuacao)
    
    type_token = (palavras_diferentes/contador_de_palavras)

    #Razão Hapax Legomana
    palavras_unicas = n_palavras_unicas(palavras_sem_pontuacao)

    hapax_legomana = (palavras_unicas / contador_de_palavras)

    #Tamanho médio de sentença erro
    qtd_caracter_senteca = 0
    for sent in sentencas:
        qtd_caracter_senteca += len(sent)

    tamanho_medio_senteca = qtd_caracter_senteca / len(sentencas)

    #Complexidade de sentença
    complexidade_sentenca = qtd_frases / len(sentencas)

    #Tamanho médio de frase erro
    tamanho_medio_frase = caracteres_frase / qtd_frases

    valores_assinatura.append(tamanho_medio_palavras)
    valores_assinatura.append(type_token)
    valores_assinatura.append(hapax_legomana)
    valores_assinatura.append(tamanho_medio_senteca)
    valores_assinatura.append(complexidade_sentenca)
    valores_assinatura.append(tamanho_medio_frase)

    return valores_assinatura
    

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura 
    ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de 
    ter sido infectado por COH-PIAH.'''

    calculo_de_assinaturas = []

    for texto in textos:
        calculo_de_assinaturas.append(calcula_assinatura(texto))

    print(calculo_de_assinaturas)
    valores_medio_assinatura = []

    for padroes in calculo_de_assinaturas:
        valores_medio_assinatura.append(compara_assinatura(ass_cp, padroes))

    menor = valores_medio_assinatura[0]
    indice = 1

    for x in range(0,len(valores_medio_assinatura), 1):
        if menor > valores_medio_assinatura[x]:
            menor = x
            indice = x + 1

    return indice







