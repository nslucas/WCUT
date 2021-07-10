import math

nome_cliente = str(input('Qual o nome do(a) cliente? '))



while True:

    tipo = str(input('O que você deseja criar? \n Opções: \n 1 - Armário comum \n 2 - Armário comum inferior de cozinha \n 3 - Microondas \n 4 - Nicho \n 5 - Porta-tempeiro \n 6 - Gaveteiro com puxador sem rodapé \n 7 - Gaveteiro sem puxador e sem rodapé  \n 8 - Gaveteiro com puxador e com rodapé \n 9 - Gaveteiro sem puxador e com rodapé \n Selecione uma opção: '  ))

    arquivo = open(r"C:\Users\lucas\Desktop\PLANOS DE CORTE\Plano de corte " + nome_cliente + '.txt', "a")

    if tipo == '1':
        altura = int(input('Qual é a altura? '))
        largura = int(input('Qual é a largura? '))
        subtracao_largura = largura - 30
        profundidade_modulo = int(input('Qual é a profundidade? '))
        numero_portas = int(input('Quantas portas? '))
        subtracao2 = profundidade_modulo - 50
        if numero_portas > 0:
            porta = str(input('Porta com puxador? '))
        prat_int = int(input('Quantas prateleiras internas? '))
        largura_aux = largura - 10
        espessura = 15
        espessura_fundo = 6

        lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidade_modulo, espessura)
        print(lateral)
        arquivo.write(lateral)

        printBaseSuperior = '2x {}*{}*{} (1+) base/superior\n'.format(subtracao_largura, profundidade_modulo, espessura)
        print(printBaseSuperior)
        arquivo.write(printBaseSuperior)
        if prat_int == 1:
            uma_prateleira = ('1x {}*{}*{} (1+) prat interna\n'.format(subtracao_largura, subtracao2, espessura))
            print(uma_prateleira)
            arquivo.write(uma_prateleira)
        if prat_int == 2:
            duas_prateleiras = ('2x {}*{}*{} (1+) prat interna\n'.format(subtracao_largura, subtracao2, espessura))
            print(duas_prateleiras)
            arquivo.write(duas_prateleiras)
        if numero_portas > 0:
            porta_puxador = altura - 45
            porta_sem_puxador = altura - 10
            porta_largura = largura - 10
            porta_largura_two = math.floor(porta_largura / 2)

            if porta == 'sim':
                if numero_portas == 1:
                    uma_porta_puxador = ('1x {}*{}*{} (4L) porta\n'.format(porta_puxador, porta_largura, espessura))
                    print(uma_porta_puxador)
                    arquivo.write(uma_porta_puxador)
                if numero_portas == 2:
                    duas_portas_puxador = ('2x {}*{}*{} (4L) porta\n'.format(porta_puxador, porta_largura_two, espessura))
                    print(duas_portas_puxador)
                    arquivo.write(duas_portas_puxador)

            if porta == 'não':
                if numero_portas == 1:
                    uma_porta_sem_puxador = (
                        '1x {}*{}*{} (4L) porta\n'.format(porta_sem_puxador, porta_largura, espessura))
                    print(uma_porta_sem_puxador)
                    arquivo.write(uma_porta_sem_puxador)
                if numero_portas == 2:
                    duas_portas_sem_puxador = (
                        '2x {}*{}*{} (4L) porta\n'.format(porta_sem_puxador, porta_largura_two, espessura, ))
                    print(duas_portas_sem_puxador)
                    arquivo.write(duas_portas_sem_puxador)

            fundo_armario_comum = ('1x {}*{}*{} fundo\n'.format(largura, altura, espessura_fundo))
            print(fundo_armario_comum)
            arquivo.write(fundo_armario_comum)

    if tipo == '2':
        altura = int(input('Qual é a altura? '))
        largura = int(input('Qual é a largura? '))
        profundidade_modulo = int(input('Qual é a profundidade? '))
        prat_int = int(input('Quantas prateleiras internas? '))
        numero_portas = int(input('Quantas portas? '))
        if numero_portas > 0:
            porta = str(input('Porta com puxador? '))

        subtracao_largura = largura - 30
        largura_aux = largura - 10
        espessura = 15
        espessura_fundo = 6
        subtracao2 = profundidade_modulo - 50

        lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidade_modulo, espessura)
        print(lateral)
        arquivo.write(lateral)

        base_com_batente = '1x {}*{}*{} (1+) base\n'.format(subtracao_largura, profundidade_modulo, espessura)
        print(base_com_batente)
        batente = '1x {}*{}*{} (2+) batente\n'.format(subtracao_largura, 60, espessura)
        print(batente)
        arquivo.write(base_com_batente + batente)

        if prat_int == 1:
            uma_prateleira_amario_inf = ('1x {}*{}*{} (1+) prat interna\n'.format(subtracao_largura, subtracao2, espessura))
            print(uma_prateleira_amario_inf)
            arquivo.write(uma_prateleira_amario_inf)
        if prat_int == 2:
            duas_prateleiras_amario_inf = ('2x {}*{}*{} (1+) prat interna\n'.format(subtracao_largura, subtracao2, espessura))
            print(duas_prateleiras_amario_inf)
            arquivo.write(duas_prateleiras_amario_inf)
        if numero_portas > 0:
            porta_puxador = altura - 45
            porta_sem_puxador = altura - 10
            porta_largura = largura - 10
            porta_largura_two = math.floor(porta_largura / 2)

            if porta == 'sim':
                if numero_portas == 1:
                    uma_porta_puxador_inf = ('1x {}*{}*{} (4L) porta\n'.format(porta_puxador, porta_largura, espessura))
                    print(uma_porta_puxador_inf)
                    arquivo.write(uma_porta_puxador_inf)
                if numero_portas == 2:
                    duas_portas_puxador_inf = (
                        '2x {}*{}*{} (4L) porta\n'.format(porta_puxador, porta_largura_two, espessura))
                    print(duas_portas_puxador_inf)
                    arquivo.write(duas_portas_puxador_inf)

            if porta == 'não':
                if numero_portas == 1:
                    uma_porta_sem_puxador_inf = (
                        '1x {}*{}*{} (4L) porta\n'.format(porta_sem_puxador, porta_largura, espessura))
                    print(uma_porta_sem_puxador_inf)
                    arquivo.write(uma_porta_sem_puxador_inf)
                if numero_portas == 2:
                    duas_portas_sem_puxador_inf = (
                        '2x {}*{}*{} (4L) porta\n'.format(porta_sem_puxador, porta_largura_two, espessura, ))
                    print(duas_portas_sem_puxador_inf)
                    arquivo.write(duas_portas_sem_puxador_inf)

    if tipo =='3':
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
            lateral_micro = (
                '2x {}*{}*{} (1+/1-) lateral mod micro'.format(altura, profundidade_fundo_encaixado, espessura))
            print(lateral_micro)
            arquivo.write(lateral_micro)

            superior_micro = (
                '1x {}*{}*{} (1+) superior mod micro'.format(largura_aux, profundidade_fundo_encaixado, espessura))
            print(superior_micro)
            arquivo.write(superior_micro)

            base_micro = (
                '2x {}*{}*{} (2-/1+) (DOBRAR) base mod micro'.format(largura_aux, profundidade_base, espessura))
            print(base_micro)
            arquivo.write(base_micro)

            fundo_micro = (
                '1x {}*{}*{} (1+) fundo mod micro (FIQUE ATENTO A ESPESSURA, DEPENDENDO DA COR DO MÓDULO ELA DEVERÁ SER ALTERADA!!!!!!!)'.format(
                    altura_aux, largura_aux, espessura))
            print(fundo_micro)
            arquivo.write(fundo_micro)

        else:
            lat_micro = ('2x {}*{}*{} (1+/1-) lateral mod micro'.format(altura, profundidade_fundo_fora, espessura))
            print(lat_micro)
            arquivo.write(lat_micro)

            superior_micro = (
                '1x {}*{}*{} (1+) superior mod micro'.format(largura_aux, profundidade_fundo_fora, espessura))
            print(superior_micro)
            arquivo.write(superior_micro)
            base_micro = (
                '2x {}*{}*{} (2-/1+) (DOBRAR) base mod micro'.format(largura_aux, profundidade_base, espessura))
            print(base_micro)
            arquivo.write(base_micro)
            fundo_micro = (
                '1x {}*{}*{} (2+/1-) fundo mod micro (FIQUE ATENTO A ESPESSURA, DEPENDENDO DA COR DO MÓDULO ELA DEVERÁ SER ALTERADA!!!!!!!)'.format(
                    altura, largura, espessura_fundo))
            print(fundo_micro)
            arquivo.write(fundo_micro)

    if tipo == '4':
        altura = int(input('Qual é a altura? '))
        largura = int(input('Qual é a largura? '))
        subtracao_largura = largura - 30
        profundidade_modulo = int(input('Qual é a profundidade? '))
        espessura = 15
        fundo = str(input('Tem fundo? É encaixado por dentro? '))
        espessura_fundo = 6
        lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidade_modulo, espessura)
        print(lateral)
        arquivo.write(lateral)
        printBaseSuperiorNicho = '2x {}*{}*{} (1+) base/superior\n'.format(subtracao_largura, profundidade_modulo, espessura)
        print(printBaseSuperiorNicho)
        arquivo.write(printBaseSuperiorNicho)
        if fundo == 'sim':
            fundoNicho = ('1x {}*{}*{} fundo (CUIDADO COM A ESPESSURA)\n'.format(largura-30, altura-30, 15))
            print(fundoNicho)
            arquivo.write(fundoNicho)
        else:
            fundoNicho = ('1x {}*{}*{} fundo (CUIDADO COM A ESPESSURA)\n'.format(largura, altura, 15))
            print(fundoNicho)
            arquivo.write(fundoNicho)
    if tipo == '5':
        altura = int(input('Qual é a altura? '))
        largura = int(input('Qual é a largura? '))
        subtracao_largura = largura - 30
        largura_aux = largura - 10
        espessura = 15
        espessura_fundo = 6
        profundidade_modulo = int(input('Qual é a profundidade? '))
        porta_puxador = altura - 45
        largura_aux = largura - 10
        espessura = 15
        espessura_fundo = 6
        lateral_int = altura - 105
        frente_verso = 85
        largura_aux_2 = largura - 89
        fundo = frente_verso + 15
        altura_int = 85

        lateral_caixa = (
            '2x {}*{}*{} (1+/1-) lateral mod porta tempero\n'.format(altura, profundidade_modulo, espessura, ))
        base_caixa = ('1x {}*{}*{} (1+) base mod porta tempero\n'.format(subtracao_largura, profundidade_modulo,
                                                                         espessura))
        batente_caixa = ('1x {}*{}*{} (2+) batente\n'.format(subtracao_largura, 60, espessura))
        frente_caixa = (
            '1x {}*{}*{} (4L) frente mod porta tempero\n'.format(porta_puxador, largura_aux, espessura))
        lateral_maior_interna = ('1x {}*{}*{} (1+/1-) lateral maior mod porta tempero\n'.format(lateral_int,
                                                                                            profundidade_modulo - 50,
                                                                                            espessura))
        lateral_menor_interna = (
            '2x {}*{}*{} (1+/1-) lateral menor mod porta tempero\n'.format(altura_int, profundidade_modulo - 50,
                                                                           espessura))
        frente_verso_interna = (
            '4x {}*{}*{} (1+) frente/verso mod porta tempero\n'.format(frente_verso, largura_aux_2, espessura))
        fundo_tempero = (
            '2x {}*{}*{} (2+) fundo porta tempero\n'.format(profundidade_modulo - 50, largura_aux_2 + 15,
                                                            espessura_fundo))
        print(lateral_caixa)
        print(base_caixa)
        print(batente_caixa)
        print(frente_caixa)
        print(lateral_maior_interna)
        print(lateral_menor_interna)
        print(frente_verso_interna)
        print(fundo_tempero)
        arquivo.write(
            lateral_caixa + base_caixa + batente_caixa + frente_caixa + lateral_maior_interna + lateral_menor_interna + frente_verso_interna + fundo_tempero)


    if tipo == '6':
            arquivo = open(r"C:\Users\lucas\Desktop\PLANOS DE CORTE\Plano de corte " + nome_cliente + '.txt', "a")
            quantidadeGavetas = int(input('Quantas gavetas? '))
            altura = int(input('Qual é a altura? '))
            largura = int(input('Qual é a largura? '))
            subtracao_largura = largura - 30
            largura_aux = largura - 10
            espessura = 15
            espessura_fundo = 6
            profundidade_modulo = int(input('Qual é a profundidade? '))

            if quantidadeGavetas == 1:
                sub_altura = altura - 10
                fundo_gav = largura - 57
                gaveta = sub_altura - 35

                lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidade_modulo, espessura)
                print(lateral)
                arquivo.write(lateral)

                base_com_batente = '1x {}*{}*{} (1+) base\n'.format(subtracao_largura, profundidade_modulo, espessura)
                print(base_com_batente)
                batente = '1x {}*{}*{} (2+) batente\n'.format(subtracao_largura, 60, espessura)
                print(batente)
                arquivo.write(base_com_batente + batente)

                frete_uma_gaveta = ('1x {}*{}*{} (4L) frente gav\n'.format(gaveta, largura_aux, espessura))
                arquivo.write(frete_uma_gaveta)

                if profundidade_modulo >= 470:
                    lateral_uma_gaveta = ('2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, '420', espessura))
                    fundo_uma_gaveta = ('1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                    print(lateral_uma_gaveta)
                    print(fundo_uma_gaveta)
                    arquivo.write(lateral_uma_gaveta)
                    arquivo.write(fundo_uma_gaveta)
                else:
                    lateral_uma_gaveta = (
                        '2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, profundidade_modulo - 50, espessura))
                    fundo_uma_gaveta = (
                        '1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50, espessura_fundo))
                    print(lateral_uma_gaveta)
                    print(fundo_uma_gaveta)
                    arquivo.write(lateral_uma_gaveta + fundo_uma_gaveta)
                    frente_verso = largura - 87
                    frente_verso_uma_gaveta = (
                        '2x {}*{}*{} (1+) frente/verso gav\n'.format(gaveta - 35, frente_verso, espessura))
                    print(frente_verso_uma_gaveta)
                    arquivo.write(frente_verso_uma_gaveta)

            if quantidadeGavetas == 2:
                sub_altura = altura - 15
                gaveta_aux = (sub_altura / 2)
                gaveta_menor = math.floor(gaveta_aux - 35)
                gaveta_aux2 = gaveta_aux % 1
                gaveta_maior = math.ceil(gaveta_aux + gaveta_aux2 - 35)
                fundo_gav = largura - 57
                total = gaveta_aux - 35
                lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidade_modulo, espessura)
                print(lateral)
                arquivo.write(lateral)

                base_com_batente = '1x {}*{}*{} (1+) base\n'.format(subtracao_largura, profundidade_modulo, espessura)
                print(base_com_batente)
                batente = '1x {}*{}*{} (2+) batente\n'.format(subtracao_largura, 60, espessura)
                print(batente)
                arquivo.write(base_com_batente + batente)
                if total > sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                    rest = sub_altura - total
                    gaveta_maior = gaveta_maior + rest
                frente_gav_maior_duas_gavetas = ("1x {}*{}*{} (4L) frente gav menor\n".format(gaveta_menor, largura_aux, espessura))
                print(frente_gav_maior_duas_gavetas)
                arquivo.write(frente_gav_maior_duas_gavetas)
                frente_gaveta_maior_duas_gavetas = ("1x {}*{}*{} (4L) frente gav maior\n".format(gaveta_maior, largura_aux, espessura))
                print(frente_gaveta_maior_duas_gavetas)
                arquivo.write(frente_gaveta_maior_duas_gavetas)

                if total == sub_altura:
                    frente_gaveta_2 = ('2x {}*{}*{} frente gav\n '.format(gaveta_aux - 35, largura_aux, espessura, ))
                    print(frente_gaveta_2)
                    arquivo.write(frente_gaveta_2)
                if profundidade_modulo >= 470:
                    lateral_maior_duas_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                    lateral_menor_duas_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                    fundo_duas_gavetas = ('2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                    print(lateral_maior_duas_gavetas)
                    print(lateral_menor_duas_gavetas)
                    print(fundo_duas_gavetas)
                    arquivo.write(lateral_maior_duas_gavetas + lateral_menor_duas_gavetas + fundo_duas_gavetas)
                else:
                    lateral_duas_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, profundidade_modulo - 50,
                                                                      espessura))
                    lateral_menor_duas_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, profundidade_modulo - 50,
                                                                      espessura))
                    fundo_duas_gavetas = (
                        '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50, espessura_fundo))
                    print(lateral_duas_gavetas)
                    print(lateral_menor_duas_gavetas)
                    print(fundo_duas_gavetas)
                    arquivo.write(lateral_duas_gavetas + lateral_menor_duas_gavetas + fundo_duas_gavetas)
                frente_verso = largura - 87
                frente_verso_maior_duas_gavetas = (
                    '2x {}*{}*{} (1+) frente/verso gav menor\n'.format(gaveta_menor - 35, frente_verso, espessura))
                frente_verso_menor_duas_gavetas = (
                    '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(gaveta_maior - 35, frente_verso, espessura))
                print(frente_verso_maior_duas_gavetas)
                print(frente_verso_menor_duas_gavetas)
                arquivo.write(frente_verso_maior_duas_gavetas + frente_verso_menor_duas_gavetas)

            if quantidadeGavetas == 3:
                tamanho = str(input('São do mesmo tamanho? '))

                if tamanho == 'não':
                    sub_altura = altura - 20
                    fundo_gav = largura - 57
                    gaveta_aux = sub_altura / 4
                    gaveta_menor = math.floor(gaveta_aux - 35)  ###math.floor() arredonda para baixo
                    gaveta_maior = math.ceil(gaveta_aux * 2) - 35  ###math.ceil() arredonda para cima
                    largura_aux = largura - 10
                    total = (2 * gaveta_menor) + gaveta_maior + 105
                    lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidade_modulo, espessura)
                    print(lateral)
                    arquivo.write(lateral)

                    base_com_batente = '1x {}*{}*{} (1+) base\n'.format(subtracao_largura, profundidade_modulo, espessura)
                    print(base_com_batente)
                    batente = '1x {}*{}*{} (2+) batente\n'.format(subtracao_largura, 60, espessura)
                    print(batente)
                    arquivo.write(base_com_batente + batente)
                    if total < sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                        rest = sub_altura - total
                        gaveta_maior = gaveta_maior + rest
                    frente_gav_menor_3 = (
                        '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
                    frente_gav_maior_3 = ('1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, largura_aux, espessura))
                    print(frente_gav_menor_3)
                    print(frente_gav_maior_3)
                    arquivo.write(frente_gav_menor_3 + frente_gav_maior_3)
                    if profundidade_modulo >= 470:
                        lateral_gav_maior_tres_gavetas = (
                            '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                        lateral_gav_menor_tres_gavetas = (
                            '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                        fundo_tres_gavetas = ('3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                        print(lateral_gav_maior_tres_gavetas)
                        print(lateral_gav_menor_tres_gavetas)
                        print(fundo_tres_gavetas)
                        arquivo.write(lateral_gav_maior_tres_gavetas + lateral_gav_menor_tres_gavetas + fundo_tres_gavetas)
                    else:
                        lateral_gav_maior_tres_gavetas = (
                            '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, profundidade_modulo - 50,
                                                                          espessura))
                        lateral_gav_menor_tres_gavetas = (
                            '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, profundidade_modulo - 50,
                                                                          espessura))
                        fundo_tres_gavetas = (
                            '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50, espessura_fundo))
                        print(lateral_gav_maior_tres_gavetas)
                        print(lateral_gav_menor_tres_gavetas)
                        print(fundo_tres_gavetas)
                        arquivo.write(lateral_gav_maior_tres_gavetas + lateral_gav_menor_tres_gavetas + fundo_tres_gavetas)
                    frente_verso = largura - 87
                    frente_verso_menor_tres_gavetas = (
                        '4x {}*{}*{} (1+) frente/verso gav menor\n'.format(frente_verso, gaveta_menor - 35, espessura))
                    frente_verso_maior_tres_gavetas = (
                        '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(frente_verso, gaveta_maior - 35, espessura))
                    print(frente_verso_menor_tres_gavetas)
                    print(frente_verso_maior_tres_gavetas)
                    arquivo.write(frente_verso_menor_tres_gavetas + frente_verso_maior_tres_gavetas)
                if tamanho == 'sim':
                    sub_altura = altura - 20
                    fundo_gav = largura - 57
                    gaveta_aux = sub_altura / 3
                    gaveta_menor = math.floor(gaveta_aux - 35)  ###math.floor() arredonda para baixo
                    gaveta_maior = math.ceil(gaveta_aux) - 35  ###math.ceil() arredonda para cima
                    largura_aux = largura - 10
                    rest = sub_altura
                    total = gaveta_menor + rest
                    rest2 = sub_altura - total

                    lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidade_modulo, espessura)
                    print(lateral)

                    base_com_batente = '1x {}*{}*{} (1+) base\n'.format(subtracao_largura, profundidade_modulo,
                                                                        espessura)
                    print(base_com_batente)
                    batente_2 = '1x {}*{}*{} (2+) batente\n'.format(subtracao_largura, 60, espessura)
                    print(batente_2)

                    if total < sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                        rest = sub_altura - total
                        gaveta_maior = gaveta_maior + rest
                    frente_gav_menor_3 = (
                        '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
                    frente_gav_maior_3 = (
                        '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, largura_aux, espessura))
                    print(frente_gav_menor_3)
                    print(frente_gav_maior_3)

                    if profundidade_modulo >= 470:
                        lateral_gav_maior_tres_gavetas = (
                            '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                        lateral_gav_menor_tres_gavetas = (
                            '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                        fundo_tres_gavetas = ('3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                        print(lateral_gav_maior_tres_gavetas)
                        print(lateral_gav_menor_tres_gavetas)
                        print(fundo_tres_gavetas)

                    else:
                        lateral_maior_tres_gavetas = (
                            '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, profundidade_modulo - 50,
                                                                          espessura))
                        lateral_menor_tres_gavetas = (
                            '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, profundidade_modulo - 50,
                                                                          espessura))
                        fundo_tres_gavetas = (
                            '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50, espessura_fundo))
                        print(lateral_maior_tres_gavetas)
                        print(lateral_menor_tres_gavetas)
                        print(fundo_tres_gavetas)

                    frente_verso = largura - 87
                    frente_verso_gav_menor_tres_gavetas = (
                        '4x {}*{}*{} (1+) frente/verso gav menor\n'.format(frente_verso, gaveta_menor - 35, espessura))
                    frente_verso_gav_maior_tres_gavetas = (
                        '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(frente_verso, gaveta_maior - 35, espessura))
                    print(frente_verso_gav_menor_tres_gavetas)
                    print(frente_verso_gav_maior_tres_gavetas)

            if quantidadeGavetas == 4:
                sub_altura = altura - 25
                gaveta_aux = (sub_altura / 4)
                gaveta_menor = math.floor(gaveta_aux - 35)
                gaveta_aux2 = gaveta_aux % 1
                gaveta_maior = math.ceil(gaveta_aux + gaveta_aux2 - 35)
                largura_aux = largura - 10
                total = gaveta_aux - 35
                fundo_gav = largura - 57
                lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidade_modulo, espessura)
                print(lateral)
                arquivo.write(lateral)

                base_com_batente = '1x {}*{}*{} (1+) base\n'.format(subtracao_largura, profundidade_modulo, espessura)
                print(base_com_batente)
                batente = '1x {}*{}*{} (2+) batente\n'.format(subtracao_largura, 60, espessura)
                print(batente)
                arquivo.write(base_com_batente + batente)
                if total > sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                    rest = sub_altura - total
                    gaveta_maior = gaveta_maior + rest
                frente_gav_menor_quatro_gavetas = (
                    '3x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
                frente_gav_maior_quatro_gavetas = ('1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, largura_aux, espessura))
                print(frente_gav_menor_quatro_gavetas)
                print(frente_gav_maior_quatro_gavetas)
                arquivo.write(frente_gav_menor_quatro_gavetas + frente_gav_maior_quatro_gavetas)
                if profundidade_modulo >= 470:
                    lateral_quatro_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                    lateral_menor_quatro_gavetas = (
                        '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                    fundo_quatro_gavetas = ('3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                    print(lateral_quatro_gavetas)
                    print(lateral_menor_quatro_gavetas)
                    print(fundo_quatro_gavetas)
                    arquivo.write(lateral_quatro_gavetas + lateral_menor_quatro_gavetas + fundo_quatro_gavetas)
                else:
                    lateral_quatro_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, profundidade_modulo - 50,
                                                                      espessura))
                    lateral_menor_quatro_gavetas = (
                        '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, profundidade_modulo - 50,
                                                                      espessura))
                    fundo_quatro_gavetas = (
                        '4x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50, espessura_fundo))
                    print(lateral_quatro_gavetas)
                    print(lateral_menor_quatro_gavetas)
                    print(fundo_quatro_gavetas)
                    arquivo.write(lateral_quatro_gavetas + lateral_menor_quatro_gavetas + fundo_quatro_gavetas)
                frente_verso = largura - 87
                frente_verso_menor_quatro_gavetas = (
                    '6x {}*{}*{} (1+) frente/verso gav menor\n'.format(frente_verso, gaveta_menor - 35, espessura))
                frente_verso_maior_quatro_gavetas = (
                    '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(frente_verso, gaveta_maior - 35, espessura))
                print(frente_verso_menor_quatro_gavetas)
                print(frente_verso_maior_quatro_gavetas)
                arquivo.write(frente_verso_menor_quatro_gavetas + frente_verso_maior_quatro_gavetas)
    if tipo == '7':
        altura = int(input('Qual é a altura? '))
        largura = int(input('Qual é a largura? '))
        subtracao_largura = largura - 30
        largura_aux = largura - 10
        espessura = 15
        espessura_fundo = 6
        profundidade_modulo = int(input('Qual é a profundidade? '))
        quantidade_gavetas = int(input('Quantas gavetas? '))
        if quantidade_gavetas == 1:
            sub_altura = altura - 10
            fundo_gav = largura - 57
            gaveta = sub_altura
            one_drawer = ('1x {}*{}*{} (4L) frente gav\n'.format(gaveta, largura_aux, espessura))
            arquivo.write(one_drawer)

            if profundidade_modulo >= 470:
                lateral_uma_gaveta = ('2x {}*{}*{} (1+) lateral gav\n'.format(gaveta, '420', espessura))
                fundo_uma_gaveta = ('1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                print(lateral_uma_gaveta)
                print(fundo_uma_gaveta)
                arquivo.write(lateral_uma_gaveta)
                arquivo.write(fundo_uma_gaveta)
            else:
                lateral_uma_gaveta = (
                    '2x {}*{}*{} (1+) lateral gav\n'.format(gaveta, profundidade_modulo - 50,
                                                            espessura))
                fundo_uma_gaveta = (
                    '1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                          espessura_fundo))
                print(lateral_uma_gaveta)
                print(fundo_uma_gaveta)
                arquivo.write(lateral_uma_gaveta + fundo_uma_gaveta)
            frente_verso = largura - 87
            frente_verso_uma_gaveta = (
                '2x {}*{}*{} (1+) frente/verso gav\n'.format(gaveta, frente_verso, espessura))
            print(frente_verso_uma_gaveta)
            arquivo.write(frente_verso_uma_gaveta)

        if quantidade_gavetas == 2:
            sub_altura = altura - 15
            gaveta_aux = (sub_altura / 2)
            gaveta_menor = math.floor(gaveta_aux)
            gaveta_aux2 = gaveta_aux % 1
            gaveta_maior = math.ceil(gaveta_aux + gaveta_aux2)
            fundo_gav = largura - 57
            total = gaveta_aux - 35
            if total > sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                rest = sub_altura - total
                gaveta_maior = gaveta_maior + rest
                frente_gav_2 = (
                    "1x {}*{}*{} (4L) frente gav menor\n".format(gaveta_menor, largura_aux, espessura))
                frente_gav_maior_2 = (
                    "1x {}*{}*{} (4L) frente gav maior\n".format(gaveta_maior, largura_aux, espessura))
                print(frente_gav_2)
                print(frente_gav_maior_2)
                arquivo.write(frente_gav_2 + frente_gav_maior_2)

            if total == sub_altura:
                frente_gav2 = ('2x {}*{}*{} frente gav\n '.format(gaveta_aux, largura_aux, espessura, ))
                print(frente_gav2)
                arquivo.write(frente_gav2)
            if profundidade_modulo >= 470:
                lateral_duas_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                lateral_menor_duas_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                fundo_duas_gavetas = (
                    '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                print(lateral_duas_gavetas)
                print(lateral_menor_duas_gavetas)
                print(fundo_duas_gavetas)
                arquivo.write(lateral_duas_gavetas + lateral_menor_duas_gavetas + fundo_duas_gavetas)
            else:
                lateral_duas_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                  profundidade_modulo - 50, espessura))
                lateral_menor_duas_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                  profundidade_modulo - 50, espessura))
                fundo_duas_gavetas = (
                    '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                          espessura_fundo))
                print(lateral_duas_gavetas)
                print(lateral_menor_duas_gavetas)
                print(fundo_duas_gavetas)
                arquivo.write(lateral_duas_gavetas + lateral_menor_duas_gavetas + fundo_duas_gavetas)

            frente_verso_duas_gavetas = (
                '2x {}*{}*{} (1+) frente/verso gav menor\n'.format(gaveta_menor - 35, frente_verso, espessura))
            frente_verso_menor_duas_gavetas = (
                '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(gaveta_maior - 35, frente_verso, espessura))
            print(frente_verso_duas_gavetas)
            print(frente_verso_menor_duas_gavetas)
            arquivo.write(frente_verso_duas_gavetas + frente_verso_menor_duas_gavetas)

        if quantidade_gavetas == 3:
            tamanho = str(input('São do mesmo tamanho? '))

            if tamanho == 'não':
                sub_altura = altura - 20
                fundo_gav = largura - 57
                gaveta_aux = sub_altura / 4
                gaveta_menor = math.floor(gaveta_aux)  ###math.floor() arredonda para baixo
                gaveta_maior = math.ceil(gaveta_aux * 2)  ###math.ceil() arredonda para cima
                largura_aux = largura - 10
                total = (2 * gaveta_menor) + gaveta_maior + 105
                if total < sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                    rest = sub_altura - total
                    gaveta_maior = gaveta_maior + rest
                frente_gav_menor_3 = (
                    '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
                frente_gav_3 = (
                    '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior +1, largura_aux, espessura))
                print(frente_gav_menor_3)
                print(frente_gav_3)

                if profundidade_modulo >= 470:
                    lateral_tres_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                    lateral_menor_tres_gavetas = (
                        '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                    fundo_tres_gavetas = (
                        '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                    print(lateral_tres_gavetas)
                    print(lateral_menor_tres_gavetas)
                    print(fundo_tres_gavetas)

                else:
                    lateral_tres_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                      profundidade_modulo - 50, espessura))
                    lateral_menor_tres_gavetas = (
                        '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                      profundidade_modulo - 50, espessura))
                    fundo_tres_gavetas = (
                        '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                              espessura_fundo))
                    print(lateral_tres_gavetas)
                    print(lateral_menor_tres_gavetas)
                    print(fundo_tres_gavetas)

                frente_verso = largura - 87
                frente_verso_menor_tres_gavetas = (
                    '4x {}*{}*{} (1+) frente/verso gav menor\n'.format(frente_verso, gaveta_menor - 35, espessura))
                frente_verso_tres_gavetas = (
                    '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(frente_verso, gaveta_maior - 35, espessura))
                print(frente_verso_menor_tres_gavetas)
                print(frente_verso_tres_gavetas)

            if tamanho == 'sim':

                sub_altura = altura - 20
                fundo_gav = largura - 57
                gaveta_aux = sub_altura / 3
                gaveta_menor = math.floor(gaveta_aux - 35)  ###math.floor() arredonda para baixo
                gaveta_maior = math.ceil(gaveta_aux) - 35  ###math.ceil() arredonda para cima
                largura_aux = largura - 10
                rest = sub_altura
                total = gaveta_menor + rest
                rest2 = sub_altura - total

                lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidade_modulo, espessura)
                print(lateral)

                base_com_batente = '1x {}*{}*{} (1+) base\n'.format(subtracao_largura, profundidade_modulo,
                                                                    espessura)
                print(base_com_batente)
                batente_2 = '1x {}*{}*{} (2+) batente\n'.format(subtracao_largura, 60, espessura)
                print(batente_2)

                if total < sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                    rest = sub_altura - total
                    gaveta_maior = gaveta_maior + rest
                frente_gav_menor_3 = (
                    '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
                frente_gav_maior_3 = (
                    '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, largura_aux, espessura))
                print(frente_gav_menor_3)
                print(frente_gav_maior_3)

                if profundidade_modulo >= 470:
                    lateral_gav_maior_tres_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                    lateral_gav_menor_tres_gavetas = (
                        '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                    fundo_tres_gavetas = ('3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                    print(lateral_gav_maior_tres_gavetas)
                    print(lateral_gav_menor_tres_gavetas)
                    print(fundo_tres_gavetas)

                else:
                    lateral_maior_tres_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, profundidade_modulo - 50,
                                                                      espessura))
                    lateral_menor_tres_gavetas = (
                        '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, profundidade_modulo - 50,
                                                                      espessura))
                    fundo_tres_gavetas = (
                        '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50, espessura_fundo))
                    print(lateral_maior_tres_gavetas)
                    print(lateral_menor_tres_gavetas)
                    print(fundo_tres_gavetas)

                frente_verso = largura - 87
                frente_verso_gav_menor_tres_gavetas = (
                    '4x {}*{}*{} (1+) frente/verso gav menor\n'.format(frente_verso, gaveta_menor - 35, espessura))
                frente_verso_gav_maior_tres_gavetas = (
                    '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(frente_verso, gaveta_maior - 35, espessura))
                print(frente_verso_gav_menor_tres_gavetas)
                print(frente_verso_gav_maior_tres_gavetas)

        if quantidade_gavetas == 4:
            sub_altura = altura - 25
            gaveta_aux = (sub_altura / 4)
            gaveta_menor = math.floor(gaveta_aux)
            gaveta_aux2 = gaveta_aux % 1
            gaveta_maior = math.ceil(gaveta_aux + gaveta_aux2)
            largura_aux = largura - 10
            total = gaveta_aux - 35
            fundo_gav = largura - 57
            if total > sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                rest = sub_altura - total
                gaveta_maior = gaveta_maior + rest
            frente_gav_menor_quatro_gavetas  = (
                '3x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
            frente_gav_quatro_gavetas = (
                '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, largura_aux, espessura))
            print(frente_gav_menor_quatro_gavetas)
            print(frente_gav_quatro_gavetas)
            arquivo.write(frente_gav_menor_quatro_gavetas + frente_gav_quatro_gavetas)
            if profundidade_modulo >= 470:
                lateral_quatro_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                lateral_menor_quatro_gavetas = (
                    '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                fundo_quatro_gavetas = (
                    '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                print(lateral_quatro_gavetas)
                print(lateral_menor_quatro_gavetas)
                print(fundo_quatro_gavetas)
                arquivo.write(lateral_quatro_gavetas + lateral_menor_quatro_gavetas + fundo_quatro_gavetas)
            else:
                lateral_quatro_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                  profundidade_modulo - 50, espessura))
                lateral_menor_quatro_gavetas = (
                    '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                  profundidade_modulo - 50, espessura))
                fundo_quatro_gavetas = (
                    '4x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                          espessura_fundo))
                print(lateral_quatro_gavetas)
                print(lateral_menor_quatro_gavetas)
                print(fundo_quatro_gavetas)
                arquivo.write(lateral_quatro_gavetas + lateral_menor_quatro_gavetas + fundo_quatro_gavetas)
            frente_verso = largura - 87
            frente_verso_menor_quatro_gavetas = (
                '6x {}*{}*{} (1+) frente/verso gav menor\n'.format(frente_verso, gaveta_menor - 35, espessura))
            frente_verso_maior_quatro_gavetas = (
                '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(frente_verso, gaveta_maior - 35, espessura))
            print(frente_verso_menor_quatro_gavetas)
            print(frente_verso_maior_quatro_gavetas)
            arquivo.write(frente_verso_menor_quatro_gavetas + frente_verso_maior_quatro_gavetas)


    if tipo == '8':

            quantidade_gavetas = int(input('Quantas gavetas? '))
            altura = int(input('Qual é a altura? '))
            largura = int(input('Qual é a largura? '))
            subtracao_largura = largura - 30
            largura_aux = largura - 10
            espessura = 15
            espessura_fundo = 6
            profundidade_modulo = int(input('Qual é a profundidade? '))

            lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidade_modulo, espessura)
            print(lateral)
            arquivo.write(lateral)

            base_com_batente = '1x {}*{}*{} (1+) base\n'.format(subtracao_largura, profundidade_modulo, espessura)
            print(base_com_batente)
            batente = '1x {}*{}*{} (2+) batente\n'.format(subtracao_largura, 60, espessura)
            print(batente)
            arquivo.write(base_com_batente + batente)

            if quantidade_gavetas == 1:
                sub_altura = altura - 10 - 80
                fundo_gav = largura - 57
                gaveta = sub_altura - 35

                frente_uma_gaveta = ('1x {}*{}*{} (4L) frente gav\n'.format(gaveta, largura_aux, espessura))
                arquivo.write(frente_uma_gaveta)

                if profundidade_modulo >= 470:
                    lateral_uma_gaveta = ('2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, '420', espessura))
                    fundo_uma_gaveta = ('1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                    print(lateral_uma_gaveta)
                    print(fundo_uma_gaveta)
                    arquivo.write(lateral_uma_gaveta)
                    arquivo.write(fundo_uma_gaveta)
                else:
                    lateral_uma_gaveta = (
                        '2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, profundidade_modulo - 50,
                                                                espessura))
                    fundo_uma_gaveta = (
                        '1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                              espessura_fundo))
                    print(lateral_uma_gaveta)
                    print(fundo_uma_gaveta)
                    arquivo.write(lateral_uma_gaveta + fundo_uma_gaveta)
                frente_verso = largura - 87
                frente_verso_uma_gaveta = (
                    '2x {}*{}*{} (1+) frente/verso gav\n'.format(gaveta - 35, frente_verso, espessura))
                print(frente_verso_uma_gaveta)
                arquivo.write(frente_verso_uma_gaveta)

            if quantidade_gavetas == 2:
                sub_altura = altura - 15 - 80
                gaveta_aux = (sub_altura / 2)
                gaveta_menor = math.floor(gaveta_aux - 35)
                gaveta_aux2 = gaveta_aux % 1
                gaveta_maior = math.ceil(gaveta_aux + gaveta_aux2 - 35)
                fundo_gav = largura - 57
                total = gaveta_aux - 35
                if total > sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                    rest = sub_altura - total
                    gaveta_maior = gaveta_maior + rest
                    frente_gav_2 = (
                        "1x {}*{}*{} (4L) frente gav menor\n".format(gaveta_menor, largura_aux, espessura))
                    frente_gav_maior_2 = (
                        "1x {}*{}*{} (4L) frente gav maior\n".format(gaveta_maior, largura_aux, espessura))
                    print(frente_gav_2)
                    print(frente_gav_maior_2)
                    arquivo.write(frente_gav_2 + frente_gav_maior_2)

                if total == sub_altura:
                    frente_gav2 = ('2x {}*{}*{} frente gav\n '.format(gaveta_aux - 35, largura_aux, espessura, ))
                    print(frente_gav2)
                    arquivo.write(frente_gav2)
                if profundidade_modulo >= 470:
                    lateral_duas_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                    lateral_menor_duas_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                    fundo_duas_gavetas = (
                        '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                    print(lateral_duas_gavetas)
                    print(lateral_menor_duas_gavetas)
                    print(fundo_duas_gavetas)
                    arquivo.write(lateral_duas_gavetas + lateral_menor_duas_gavetas + fundo_duas_gavetas)
                else:
                    lateral_duas_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                      profundidade_modulo - 50, espessura))
                    lateral_menor_duas_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                      profundidade_modulo - 50, espessura))
                    fundo_duas_gavetas = (
                        '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                              espessura_fundo))
                    print(lateral_duas_gavetas)
                    print(lateral_menor_duas_gavetas)
                    print(fundo_duas_gavetas)
                    arquivo.write(lateral_duas_gavetas + lateral_menor_duas_gavetas + fundo_duas_gavetas)

                frente_verso_duas_gavetas = (
                    '2x {}*{}*{} (1+) frente/verso gav menor\n'.format(gaveta_menor - 35, frente_verso, espessura))
                frente_verso_menor_duas_gavetas = (
                    '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(gaveta_maior - 35, frente_verso, espessura))
                print(frente_verso_duas_gavetas)
                print(frente_verso_menor_duas_gavetas)
                arquivo.write(frente_verso_duas_gavetas + frente_verso_menor_duas_gavetas)

            if quantidade_gavetas == 3:
                tamanho = str(input('São do mesmo tamanho? '))

                if tamanho == 'não':
                    sub_altura = altura - 20 - 80
                    fundo_gav = largura - 57
                    gaveta_aux = sub_altura / 4
                    gaveta_menor = math.floor(gaveta_aux - 35)  ###math.floor() arredonda para baixo
                    gaveta_maior = math.ceil(gaveta_aux * 2) - 35  ###math.ceil() arredonda para cima
                    largura_aux = largura - 10
                    total = (2 * gaveta_menor) + gaveta_maior + 105
                    if total < sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                        rest = sub_altura - total
                        gaveta_maior = gaveta_maior + rest
                        frente_gav_menor_3 = (
                            '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
                        frente_gav_3 = (
                            '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, largura_aux, espessura))
                        print(frente_gav_menor_3)
                        print(frente_gav_3)

                        if profundidade_modulo >= 470:
                            lateral_tres_gavetas = (
                                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                            lateral_menor_tres_gavetas = (
                                '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                            fundo_tres_gavetas = (
                                '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                            print(lateral_tres_gavetas)
                            print(lateral_menor_tres_gavetas)
                            print(fundo_tres_gavetas)

                        else:
                            lateral_tres_gavetas = (
                                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                              profundidade_modulo - 50, espessura))
                            lateral_menor_tres_gavetas = (
                                '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                              profundidade_modulo - 50, espessura))
                            fundo_tres_gavetas = (
                                '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                                      espessura_fundo))
                            print(lateral_tres_gavetas)
                            print(lateral_menor_tres_gavetas)
                            print(fundo_tres_gavetas)

                        frente_verso = largura - 87
                        frente_verso_menor_tres_gavetas = (
                            '4x {}*{}*{} (1+) frente/verso gav menor\n'.format(frente_verso, gaveta_menor - 35,
                                                                               espessura))
                        frente_verso_tres_gavetas = (
                            '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(frente_verso, gaveta_maior - 35,
                                                                               espessura))
                        print(frente_verso_menor_tres_gavetas)
                        print(frente_verso_tres_gavetas)

                if tamanho == 'sim':
                    sub_altura = altura - 20 - 80
                    fundo_gav = largura - 57
                    gaveta_aux = sub_altura / 3
                    gaveta_menor = math.floor(gaveta_aux - 35)  ###math.floor() arredonda para baixo
                    gaveta_maior = math.ceil(gaveta_aux) - 35  ###math.ceil() arredonda para cima
                    largura_aux = largura - 10
                    total = (gaveta_menor) + gaveta_maior + 105
                    if total < sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                        rest = sub_altura - total
                        gaveta_maior = gaveta_maior + rest - gaveta_menor
                        frente_gav_menor_3 = (
                            '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
                        frente_gav_3 = (
                            '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, largura_aux, espessura))
                        print(frente_gav_menor_3)
                        print(frente_gav_3)

                        if profundidade_modulo >= 470:
                            lateral_tres_gavetas = (
                                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                            lateral_menor_tres_gavetas = (
                                '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                            fundo_tres_gavetas = (
                                '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                            print(lateral_tres_gavetas)
                            print(lateral_menor_tres_gavetas)
                            print(fundo_tres_gavetas)

                        else:
                            lateral_tres_gavetas = (
                                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                              profundidade_modulo - 50, espessura))
                            lateral_menor_tres_gavetas = (
                                '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                              profundidade_modulo - 50, espessura))
                            fundo_tres_gavetas = (
                                '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                                      espessura_fundo))
                            print(lateral_tres_gavetas)
                            print(lateral_menor_tres_gavetas)
                            print(fundo_tres_gavetas)

                        frente_verso = largura - 87
                        frente_verso_menor_tres_gavetas = (
                            '4x {}*{}*{} (1+) frente/verso gav menor\n'.format(frente_verso, gaveta_menor - 35,
                                                                               espessura))
                        frente_verso_tres_gavetas = (
                            '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(frente_verso, gaveta_maior - 35,
                                                                               espessura))
                        print(frente_verso_menor_tres_gavetas)
                        print(frente_verso_tres_gavetas)

            if quantidade_gavetas == 4:
                sub_altura = altura - 25 - 80
                gaveta_aux = (sub_altura / 4)
                gaveta_menor = math.floor(gaveta_aux - 35)
                gaveta_aux2 = gaveta_aux % 1
                gaveta_maior = math.ceil(gaveta_aux + gaveta_aux2 - 35)
                largura_aux = largura - 10
                total = gaveta_aux - 35
                fundo_gav = largura - 57
                if total > sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                    rest = sub_altura - total
                    gaveta_maior = gaveta_maior + rest
                frente_gav_menor_quatro_gavetas = (
                    '3x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
                frente_gav_quatro_gavetas = (
                    '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, largura_aux, espessura))
                print(frente_gav_menor_quatro_gavetas)
                print(frente_gav_quatro_gavetas)
                arquivo.write(frente_gav_menor_quatro_gavetas + frente_gav_quatro_gavetas)
                if profundidade_modulo >= 470:
                    lateral_quatro_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                    lateral_menor_quatro_gavetas = (
                        '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                    fundo_quatro_gavetas = (
                        '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                    print(lateral_quatro_gavetas)
                    print(lateral_menor_quatro_gavetas)
                    print(fundo_quatro_gavetas)
                    arquivo.write(lateral_quatro_gavetas + lateral_menor_quatro_gavetas + fundo_quatro_gavetas)
                else:
                    lateral_quatro_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                      profundidade_modulo - 50, espessura))
                    lateral_menor_quatro_gavetas = (
                        '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                      profundidade_modulo - 50, espessura))
                    back_four_drawers = (
                        '4x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                              espessura_fundo))
                    print(lateral_quatro_gavetas)
                    print(lateral_menor_quatro_gavetas)
                    print(fundo_quatro_gavetas)
                    arquivo.write(lateral_quatro_gavetas + lateral_menor_quatro_gavetas + fundo_quatro_gavetas)
                frente_verso = largura - 87
                frente_verso_menor_quatro_gavetas = (
                    '6x {}*{}*{} (1+) frente/verso gav menor\n'.format(frente_verso, gaveta_menor - 35, espessura))
                frente_verso_maior_quatro_gavetas = (
                    '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(frente_verso, gaveta_maior - 35, espessura))
                print(frente_verso_menor_quatro_gavetas)
                print(frente_verso_maior_quatro_gavetas)
                arquivo.write(frente_verso_menor_quatro_gavetas + frente_verso_maior_quatro_gavetas)

    if tipo == '9':
        quantidade_gavetas = int(input('Quantas gavetas? '))
        altura = int(input('Qual é a altura? '))
        largura = int(input('Qual é a largura? '))
        subtracao_largura = largura - 30
        largura_aux = largura - 10
        espessura = 15
        espessura_fundo = 6
        profundidade_modulo = int(input('Qual é a profundidade? '))

        lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidade_modulo, espessura)
        print(lateral)
        arquivo.write(lateral)

        base_com_batente = '1x {}*{}*{} (1+) base\n'.format(subtracao_largura, profundidade_modulo, espessura)
        print(base_com_batente)
        batente = '1x {}*{}*{} (2+) batente\n'.format(subtracao_largura, 60, espessura)
        print(batente)
        arquivo.write(base_com_batente + batente)

        if quantidade_gavetas == 1:
            sub_altura = altura - 10 - 80
            fundo_gav = largura - 57
            gaveta = sub_altura

            frente_uma_gaveta = ('1x {}*{}*{} (4L) frente gav\n'.format(gaveta, largura_aux, espessura))
            arquivo.write(frente_uma_gaveta)


            if profundidade_modulo >= 470:
                lateral_uma_gaveta = ('2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, '420', espessura))
                fundo_uma_gaveta = ('1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                print(lateral_uma_gaveta)
                print(fundo_uma_gaveta)
                arquivo.write(lateral_uma_gaveta)
                arquivo.write(fundo_uma_gaveta)
            else:
                lateral_uma_gaveta = (
                    '2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, profundidade_modulo - 50,
                                                            espessura))
                fundo_uma_gaveta = (
                    '1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                          espessura_fundo))
                print(lateral_uma_gaveta)
                print(fundo_uma_gaveta)
                arquivo.write(lateral_uma_gaveta + fundo_uma_gaveta)
            frente_verso = largura - 87
            frente_verso_uma_gaveta = (
                '2x {}*{}*{} (1+) frente/verso gav\n'.format(gaveta - 35, frente_verso, espessura))
            print(frente_verso_uma_gaveta)
            arquivo.write(frente_verso_uma_gaveta)

        if quantidade_gavetas == 2:
            sub_altura = altura - 15 - 80
            gaveta_aux = (sub_altura / 2)
            gaveta_menor = math.floor(gaveta_aux)
            gaveta_aux2 = gaveta_aux % 1
            gaveta_maior = math.ceil(gaveta_aux + gaveta_aux2)
            fundo_gav = largura - 57
            total = gaveta_aux - 35
            if total > sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                rest = sub_altura - total
                gaveta_maior = gaveta_maior + rest
                frente_gav_2 = (
                    "1x {}*{}*{} (4L) frente gav menor\n".format(gaveta_menor, largura_aux, espessura))
                frente_gav_maior_2 = (
                    "1x {}*{}*{} (4L) frente gav maior\n".format(gaveta_maior, largura_aux, espessura))
                print(frente_gav_2)
                print(frente_gav_maior_2)
                arquivo.write(frente_gav_2 + frente_gav_maior_2)

            if total == sub_altura:
                frente_gav_2 = ('2x {}*{}*{} frente gav\n '.format(gaveta_aux - 35, largura_aux, espessura, ))
                print(frente_gav_2)
                arquivo.write(frente_gav_2)
            if profundidade_modulo >= 470:
                lateral_duas_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                lateral_menor_duas_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                fundo_duas_gavetas = (
                    '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                print(lateral_duas_gavetas)
                print(lateral_menor_duas_gavetas)
                print(fundo_duas_gavetas)
                arquivo.write(lateral_duas_gavetas + lateral_menor_duas_gavetas + fundo_duas_gavetas)
            else:
                lateral_duas_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                  profundidade_modulo - 50, espessura))
                lateral_menor_duas_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                  profundidade_modulo - 50, espessura))
                back_two_drawers = (
                    '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                          espessura_fundo))
                print(lateral_duas_gavetas)
                print(lateral_menor_duas_gavetas)
                print(fundo_duas_gavetas)
                arquivo.write(lateral_duas_gavetas + lateral_menor_duas_gavetas + fundo_duas_gavetas)

            frente_verso_duas_gavetas = (
                '2x {}*{}*{} (1+) frente/verso gav menor\n'.format(gaveta_menor - 35, frente_verso, espessura))
            frente_verso_menor_duas_gavetas = (
                '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(gaveta_maior - 35, frente_verso, espessura))
            print(frente_verso_duas_gavetas)
            print(frente_verso_menor_duas_gavetas)
            arquivo.write(frente_verso_duas_gavetas + frente_verso_menor_duas_gavetas)

        if quantidade_gavetas == 3:
            tamanho = str(input('São do mesmo tamanho? '))

            if tamanho == 'não':
                sub_altura = altura - 20 - 80
                fundo_gav = largura - 57
                gaveta_aux = sub_altura / 4
                gaveta_menor = math.floor(gaveta_aux)  ###math.floor() arredonda para baixo
                gaveta_maior = math.ceil(gaveta_aux * 2)  ###math.ceil() arredonda para cima
                largura_aux = largura - 10
                total = (2 * gaveta_menor) + gaveta_maior + 105
                if total < sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                    rest = sub_altura - total
                    gaveta_maior = gaveta_maior + rest
                frente_gav_menor_3 = (
                    '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
                frente_gav_3 = (
                    '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior +1, largura_aux, espessura))
                print(frente_gav_menor_3)
                print(frente_gav_3)

                if profundidade_modulo >= 470:
                    lateral_tres_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                    lateral_menor_tres_gavetas = (
                        '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                    fundo_tres_gavetas = (
                        '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                    print(lateral_tres_gavetas)
                    print(lateral_menor_tres_gavetas)
                    print(fundo_tres_gavetas)

                else:
                    lateral_tres_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                      profundidade_modulo - 50, espessura))
                    lateral_menor_tres_gavetas = (
                        '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                      profundidade_modulo - 50, espessura))
                    fundo_tres_gavetas = (
                        '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                              espessura_fundo))
                    print(lateral_tres_gavetas)
                    print(lateral_menor_tres_gavetas)
                    print(fundo_tres_gavetas)

                frente_verso = largura - 87
                frente_verso_menor_tres_gavetas = (
                    '4x {}*{}*{} (1+) frente/verso gav menor\n'.format(frente_verso, gaveta_menor - 35, espessura))
                frente_verso_tres_gavetas = (
                    '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(frente_verso, gaveta_maior - 35, espessura))
                print(frente_verso_menor_tres_gavetas)
                print(frente_verso_tres_gavetas)

            if tamanho == 'sim':
                sub_altura = altura - 20 - 80
                fundo_gav = largura - 57
                gaveta_aux = sub_altura / 3
                gaveta_menor = math.floor(gaveta_aux)  ###math.floor() arredonda para baixo
                gaveta_maior = math.ceil(gaveta_aux)  ###math.ceil() arredonda para cima
                largura_aux = largura - 10
                total = (gaveta_menor) + gaveta_maior + 105
                if total > sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                    rest = sub_altura - total
                    gaveta_maior = gaveta_maior + rest - gaveta_menor
                frente_gav_menor_3 = (
                    '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
                frente_gav_3 = (
                    '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, largura_aux, espessura))
                print(frente_gav_menor_3)
                print(frente_gav_3)

                if profundidade_modulo >= 470:
                    lateral_tres_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                    lateral_menor_tres_gavetas = (
                        '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                    fundo_tres_gavetas = (
                        '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                    print(lateral_tres_gavetas)
                    print(lateral_menor_tres_gavetas)
                    print(fundo_tres_gavetas)

                else:
                    lateral_tres_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                      profundidade_modulo - 50, espessura))
                    lateral_menor_tres_gavetas = (
                        '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                      profundidade_modulo - 50, espessura))
                    fundo_tres_gavetas = (
                        '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                              espessura_fundo))
                    print(lateral_tres_gavetas)
                    print(lateral_menor_tres_gavetas)
                    print(fundo_tres_gavetas)

                frente_verso = largura - 87
                frente_verso_menor_tres_gavetas = (
                    '4x {}*{}*{} (1+) frente/verso gav menor\n'.format(frente_verso, gaveta_menor - 35, espessura))
                frente_verso_tres_gavetas = (
                    '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(frente_verso, gaveta_maior - 35, espessura))
                print(frente_verso_menor_tres_gavetas)
                print(frente_verso_tres_gavetas)

        if quantidade_gavetas == 4:
            sub_altura = altura - 25 - 80
            gaveta_aux = (sub_altura / 4)
            gaveta_menor = math.floor(gaveta_aux)
            gaveta_aux2 = gaveta_aux % 1
            gaveta_maior = math.ceil(gaveta_aux + gaveta_aux2)
            largura_aux = largura - 10
            total = gaveta_aux - 35
            fundo_gav = largura - 57
            if total > sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                rest = sub_altura - total
                gaveta_maior = gaveta_maior + rest
            frente_gav_menor_quatro_gavetas = (
                '3x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
            frente_gav_quatro_gavetas = (
                '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, largura_aux, espessura))
            print(frente_gav_menor_quatro_gavetas)
            print(frente_gav_quatro_gavetas)
            arquivo.write(frente_gav_menor_quatro_gavetas + frente_gav_quatro_gavetas)
            if profundidade_modulo >= 470:
                lateral_quatro_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                lateral_menor_quatro_gavetas = (
                    '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                fundo_quatro_gavetas = (
                    '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                print(lateral_quatro_gavetas)
                print(lateral_menor_quatro_gavetas)
                print(fundo_quatro_gavetas)
                arquivo.write(lateral_quatro_gavetas + lateral_menor_quatro_gavetas + fundo_quatro_gavetas)
            else:
                lateral_quatro_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                  profundidade_modulo - 50, espessura))
                lateral_menor_quatro_gavetas = (
                    '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                  profundidade_modulo - 50, espessura))
                fundo_quatro_gavetas = (
                    '4x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                          espessura_fundo))
                print(lateral_quatro_gavetas)
                print(lateral_menor_quatro_gavetas)
                print(fundo_quatro_gavetas)
                arquivo.write(lateral_quatro_gavetas + lateral_menor_quatro_gavetas + fundo_quatro_gavetas)
            frente_verso = largura - 87
            frente_verso_menor_quatro_gavetas = (
                '6x {}*{}*{} (1+) frente/verso gav menor\n'.format(frente_verso, gaveta_menor - 35, espessura))
            frente_verso_maior_quatro_gavetas = (
                '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(frente_verso, gaveta_maior - 35, espessura))
            print(frente_verso_menor_quatro_gavetas)
            print(frente_verso_maior_quatro_gavetas)
            arquivo.write(frente_verso_menor_quatro_gavetas + frente_verso_maior_quatro_gavetas)

