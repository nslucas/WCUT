altura = int(input('Qual é a altura? '))
largura = int(input('Qual é a largura? '))
profundidade = int(input('Qual é a profundidade? '))
pergunta_fundo = str(input('Fundo encaixado por dentro? '))
largura_aux = largura - 30
altura_aux = altura - 45
profundidade_fundo_encaixado = profundidade + 15 + 6
profundidade_fundo_fora = profundidade + 15
espessura = 15
espessura_fundo = 6
profundidade_superior = profundidade + 15
profundidade_base = 430

if pergunta_fundo == 'sim':
    lat_micro = ('2x {}*{}*{} (1+/1-) lateral mod micro'.format(altura, profundidade_fundo_encaixado, espessura))
    print(lat_micro)

    superior_micro = (
        '1x {}*{}*{} (1+) superior mod micro'.format(largura_aux, profundidade_fundo_encaixado, espessura))
    print(superior_micro)

    base_micro = ('2x {}*{}*{} (2-/1+) (DOBRAR) base mod micro'.format(largura_aux, profundidade_base, espessura))
    print(base_micro)

    fundo_micro = ('1x {}*{}*{} (1+) fundo mod micro (FIQUE ATENTO A ESPESSURA, DEPENDENDO DA COR DO MÓDULO ELA DEVERÁ SER ALTERADA!!!!!!!)'.format(altura_aux, largura_aux, espessura))
    print(fundo_micro)

else:
    lat_micro = ('2x {}*{}*{} (1+/1-) lateral mod micro'.format(altura, profundidade_fundo_fora, espessura))
    print(lat_micro)

    superior_micro = ('1x {}*{}*{} (1+) superior mod micro'.format(largura_aux, profundidade_fundo_fora, espessura))
    print(superior_micro)

    base_micro = ('2x {}*{}*{} (2-/1+) (DOBRAR) base mod micro'.format(largura_aux, profundidade_base, espessura))
    print(base_micro)

    fundo_micro = ('1x {}*{}*{} (2+/1-) fundo mod micro (FIQUE ATENTO A ESPESSURA, DEPENDENDO DA COR DO MÓDULO ELA DEVERÁ SER ALTERADA!!!!!!!)'.format(altura_aux, largura_aux, espessura_fundo))
    print(fundo_micro)
