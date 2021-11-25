import math

nome_cliente = str(input('Qual o nome do(a) cliente? '))

while True:

    tipo = str(input(
        'Selecione o tipo de módulo desejado: '
        '\n 1 - Armário comum '
        '\n 2 - Armário comum inferior de cozinha'
        ' \n 3 - Microondas '
        '\n 4 - Nicho '
        '\n 5 - Porta-tempeiro'
        '\n 6 - Gaveteiro com puxador sem rodapé'
        '\n 7 - Gaveteiro sem puxador e sem rodapé'
        '\n 8 - Gaveteiro com puxador e com rodapé'
        '\n 9 - Gaveteiro sem puxador e com rodapé'
        '\n Selecione uma opção: '))

    arquivo = open(r"C:\Users\lucas\Desktop\TRABALHO\Plano de corte " + nome_cliente + '.txt', "a")

    if tipo == '1':
        altura = int(input('Qual é a altura? '))
        largura = int(input('Qual é a largura? '))
        larguraBase = largura - 30
        profundidadeModulo = int(input('Qual é a profundidade? '))
        numeroPortas = int(input('Quantas portas? '))
        if numeroPortas > 0:
            porta = str(input('Porta com puxador? '))
        subtracao2 = profundidadeModulo - 50
        pratInt = int(input('Quantas prateleiras internas? '))
        larguraAux = largura - 10
        espessura = 15
        espessuraFundo = 6

        lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidadeModulo, espessura)
        print(lateral)
        arquivo.write(lateral)

        printBaseSuperior = '2x {}*{}*{} (1+) base/superior\n'.format(larguraBase, profundidadeModulo, espessura)
        print(printBaseSuperior)
        arquivo.write(printBaseSuperior)
        if pratInt == 1:
            umaPrat = ('1x {}*{}*{} (1+) prat interna\n'.format(larguraBase, subtracao2, espessura))
            print(umaPrat)
            arquivo.write(umaPrat)
        else:
            duasPrat = ('2x {}*{}*{} (1+) prat interna\n'.format(larguraBase, subtracao2, espessura))
            print(duasPrat)
            arquivo.write(duasPrat)
        if numeroPortas > 0:
            portaPuxador = altura - 45
            portaSemPuxador = altura - 10
            porta_largura = largura - 10
            porta_largura_two = math.floor(porta_largura / 2)

            if porta == 'sim':
                if numeroPortas == 1:
                    uma_porta_puxador = ('1x {}*{}*{} (4L) porta\n'.format(portaPuxador, porta_largura, espessura))
                    print(uma_porta_puxador)
                    arquivo.write(uma_porta_puxador)
                if numeroPortas == 2:
                    duasPortasPuxador = ('2x {}*{}*{} (4L) porta\n'.format(portaPuxador, porta_largura_two, espessura))
                    print(duasPortasPuxador)
                    arquivo.write(duasPortasPuxador)

            else:
                if numeroPortas == 1:
                    umaPortaSemPuxador = (
                        '1x {}*{}*{} (4L) porta\n'.format(portaSemPuxador, porta_largura, espessura))
                    print(umaPortaSemPuxador)
                    arquivo.write(umaPortaSemPuxador)
                if numeroPortas == 2:
                    duasPortasSemPuxador = (
                        '2x {}*{}*{} (4L) porta\n'.format(portaSemPuxador, porta_largura_two, espessura, ))
                    print(duasPortasSemPuxador)
                    arquivo.write(duasPortasSemPuxador)

            fundoArmarioComum = ('1x {}*{}*{} fundo\n'.format(largura, altura, espessuraFundo))
            print(fundoArmarioComum)
            arquivo.write(fundoArmarioComum)

    elif tipo == '2':
        altura = int(input('Qual é a altura? '))
        largura = int(input('Qual é a largura? '))
        profundidadeModulo = int(input('Qual é a profundidade? '))
        pratInt = int(input('Quantas prateleiras internas? '))
        numeroPortas = int(input('Quantas portas? '))
        if numeroPortas > 0:
            porta = str(input('Porta com puxador? '))

        larguraBase = largura - 30
        larguraAux = largura - 10
        espessura = 15
        espessuraFundo = 6
        subtracao2 = profundidadeModulo - 50

        lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidadeModulo, espessura)
        print(lateral)
        arquivo.write(lateral)

        basecomBatente = '1x {}*{}*{} (1+) base\n'.format(larguraBase, profundidadeModulo, espessura)
        print(basecomBatente)
        batente = '1x {}*{}*{} (2+) batente\n'.format(larguraBase, 60, espessura)
        print(batente)
        arquivo.write(basecomBatente + batente)

        if pratInt == 1:
            umaPrateleiraArmarioInf = ('1x {}*{}*{} (1+) prat interna\n'.format(larguraBase, subtracao2, espessura))
            print(umaPrateleiraArmarioInf)
            arquivo.write(umaPrateleiraArmarioInf)
        else:
            duasPratArmarioInf = ('2x {}*{}*{} (1+) prat interna\n'.format(larguraBase, subtracao2, espessura))
            print(duasPratArmarioInf)
            arquivo.write(duasPratArmarioInf)
        if numeroPortas > 0:
            portaPuxador = altura - 45
            portaSemPuxador = altura - 10
            larguraPorta = largura - 10
            larguraDuasPortas = math.floor(larguraPorta / 2)

            if porta == 'sim':
                if numeroPortas == 1:
                    umaPortaPuxadorInf = ('1x {}*{}*{} (4L) porta\n'.format(portaPuxador, larguraPorta, espessura))
                    print(umaPortaPuxadorInf)
                    arquivo.write(umaPortaPuxadorInf)
                else:
                    duasPortasPuxadorInf = (
                        '2x {}*{}*{} (4L) porta\n'.format(portaPuxador, larguraDuasPortas, espessura))
                    print(duasPortasPuxadorInf)
                    arquivo.write(duasPortasPuxadorInf)

            else:
                if numeroPortas == 1:
                    umaPortaSemPuxadorInf = (
                        '1x {}*{}*{} (4L) porta\n'.format(portaSemPuxador, larguraPorta, espessura))
                    print(umaPortaSemPuxadorInf)
                    arquivo.write(umaPortaSemPuxadorInf)
                else:
                    duasPortasSemPuxadorInf = (
                        '2x {}*{}*{} (4L) porta\n'.format(portaSemPuxador, larguraDuasPortas, espessura, ))
                    print(duasPortasSemPuxadorInf)
                    arquivo.write(duasPortasSemPuxadorInf)

    elif tipo == '3':
        altura = int(input('Qual é a altura? '))
        largura = int(input('Qual é a largura? '))
        profundidade = int(input('Qual é a profundidade? '))
        perguntaFundo = str(input('Fundo encaixado por dentro? '))
        larguraBase = largura - 30
        portaPuxador = altura - 45
        profundidadeFundoEncaixado = profundidade + 15 + 6
        profundidadeFundoFora = profundidade + 15
        espessura = 15
        espessuraFundo = 6
        profundidadeSuperior = profundidade + 15
        profundidadeBase = 430

        if perguntaFundo == 'sim':
            lateralMicro = (
                '2x {}*{}*{} (1+/1-) lateral mod micro'.format(altura, profundidadeFundoEncaixado, espessura))
            print(lateralMicro)
            arquivo.write(lateralMicro)

            superiorMicro = (
                f'1x {larguraBase}*{profundidadeFundoEncaixado}*{espessura} (1+) superior mod micro')
            print(superiorMicro)
            arquivo.write(superiorMicro)

            baseMicro = (
                '2x {}*{}*{} (2-/1+) (DOBRAR) base mod micro'.format(larguraBase, profundidadeBase, espessura))
            print(baseMicro)
            arquivo.write(baseMicro)

            fundoMicro = (
                f'1x {portaPuxador}*{larguraBase}*{espessura} (1+) fundo mod micro (FIQUE ATENTO A ESPESSURA')
            print(fundoMicro)
            arquivo.write(fundoMicro)

        else:
            lateralMicro = ('2x {}*{}*{} (1+/1-) lateral mod micro'.format(altura, profundidadeFundoFora, espessura))
            print(lateralMicro)
            arquivo.write(lateralMicro)

            superiorMicro = (
                '1x {}*{}*{} (1+) superior mod micro'.format(larguraBase, profundidadeFundoFora, espessura))
            print(superiorMicro)
            arquivo.write(superiorMicro)
            baseMicro = (
                '2x {}*{}*{} (2-/1+) (DOBRAR) base mod micro'.format(larguraBase, profundidadeBase, espessura))
            print(baseMicro)
            arquivo.write(baseMicro)
            fundoMicro = (
                f'1x {altura}*{largura}*{espessuraFundo} (2+/1-) fundo mod micro (FIQUE ATENTO A ESPESSURA')
            print(fundoMicro)
            arquivo.write(fundoMicro)

    elif tipo == '4':
        altura = int(input('Qual é a altura? '))
        largura = int(input('Qual é a largura? '))
        larguraBase = largura - 30
        profundidadeModulo = int(input('Qual é a profundidade? '))
        espessura = 15
        fundo = str(input('Tem fundo? É encaixado por dentro? '))
        espessuraFundo = 6
        lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidadeModulo, espessura)
        print(lateral)
        arquivo.write(lateral)
        printBaseSuperiorNicho = '2x {}*{}*{} (1+) base/superior\n'.format(larguraBase, profundidadeModulo, espessura)
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
    elif tipo == '5':
        altura = int(input('Qual é a altura? '))
        largura = int(input('Qual é a largura? '))
        larguraBase = largura - 30
        larguraAux = largura - 10
        espessura = 15
        espessuraFundo = 6
        profundidadeModulo = int(input('Qual é a profundidade? '))
        porta_puxador = altura - 45
        lateral_int = altura - 105
        frente_verso = 85
        larguraAux_2 = largura - 89
        fundo = frente_verso + 15
        altura_int = 85

        lateral_caixa = (
            '2x {}*{}*{} (1+/1-) lateral mod porta tempero\n'.format(altura, profundidadeModulo, espessura, ))
        base_caixa = ('1x {}*{}*{} (1+) base mod porta tempero\n'.format(larguraBase, profundidadeModulo,
                                                                         espessura))
        batente_caixa = ('1x {}*{}*{} (2+) batente\n'.format(larguraBase, 60, espessura))
        frente_caixa = (
            '1x {}*{}*{} (4L) frente mod porta tempero\n'.format(porta_puxador, larguraAux, espessura))
        lateral_maior_interna = (f'1x {lateral_int}*{profundidadeModulo - 50}*{espessura} '
                                 f'(1+/1-) lateral maior mod porta tempero\n')

        lateral_menor_interna = (
            '2x {}*{}*{} (1+/1-) lateral menor mod porta tempero\n'.format(altura_int, profundidadeModulo - 50,
                                                                           espessura))
        frente_verso_interna = (
            '4x {}*{}*{} (1+) frente/verso mod porta tempero\n'.format(frente_verso, larguraAux_2, espessura))
        fundo_tempero = (
            '2x {}*{}*{} (2+) fundo porta tempero\n'.format(profundidadeModulo - 50, larguraAux_2 + 15,
                                                            espessuraFundo))
        print(lateral_caixa)
        print(base_caixa)
        print(batente_caixa)
        print(frente_caixa)
        print(lateral_maior_interna)
        print(lateral_menor_interna)
        print(frente_verso_interna)
        print(fundo_tempero)
        arquivo.write(lateral_caixa + base_caixa + batente_caixa + frente_caixa + lateral_maior_interna
                      + lateral_menor_interna + frente_verso_interna + fundo_tempero)

    elif tipo == '6':
        quantidadeGavetas = int(input('Quantas gavetas? '))
        altura = int(input('Qual é a altura? '))
        largura = int(input('Qual é a largura? '))
        larguraBase = largura - 30
        larguraAux = largura - 10
        espessura = 15
        espessuraFundo = 6
        profundidadeModulo = int(input('Qual é a profundidade? '))

        if quantidadeGavetas == 1:
            sub_altura = altura - 10
            fundo_gav = largura - 57
            gaveta = sub_altura - 35

            lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidadeModulo, espessura)
            print(lateral)
            arquivo.write(lateral)

            base_com_batente = '1x {}*{}*{} (1+) base\n'.format(larguraBase, profundidadeModulo, espessura)
            print(base_com_batente)
            batente = '1x {}*{}*{} (2+) batente\n'.format(larguraBase, 60, espessura)
            print(batente)
            arquivo.write(base_com_batente + batente)

            frete_uma_gaveta = ('1x {}*{}*{} (4L) frente gav\n'.format(gaveta, larguraAux, espessura))
            arquivo.write(frete_uma_gaveta)

            if profundidadeModulo >= 470:
                lateral_uma_gaveta = ('2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, '420', espessura))
                fundo_uma_gaveta = ('1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                print(lateral_uma_gaveta)
                print(fundo_uma_gaveta)
                arquivo.write(lateral_uma_gaveta)
                arquivo.write(fundo_uma_gaveta)
            else:
                lateral_uma_gaveta = f'2x {gaveta-35}*{profundidadeModulo-50}*{espessura} (1+) lateral gav\n'
                fundo_uma_gaveta = f'1x {fundo_gav}*{profundidadeModulo -50}*{espessuraFundo} (2+) fundo gav\n'
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
                lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidadeModulo, espessura)
                print(lateral)
                arquivo.write(lateral)

                base_com_batente = '1x {}*{}*{} (1+) base\n'.format(larguraBase, profundidadeModulo, espessura)
                print(base_com_batente)
                batente = '1x {}*{}*{} (2+) batente\n'.format(larguraBase, 60, espessura)
                print(batente)
                arquivo.write(base_com_batente + batente)
            # pega o resto e coloca na medida da gaveta maior#
                if total > sub_altura:
                    rest = sub_altura - total
                    gaveta_maior = gaveta_maior + rest
                frente_gav_maior_duas_gavetas = f"1x {gaveta_menor}*{larguraAux}*{espessura} (4L) frente gav menor\n"
                print(frente_gav_maior_duas_gavetas)
                arquivo.write(frente_gav_maior_duas_gavetas)
                frenteGavetaMaiorDuasGavs = f"1x {gaveta_maior}*{larguraAux}*{espessura} (4L) frente gav maior\n"
                print(frenteGavetaMaiorDuasGavs)
                arquivo.write(frenteGavetaMaiorDuasGavs)

                if total == sub_altura:
                    frente_gaveta_2 = ('2x {}*{}*{} frente gav\n '.format(gaveta_aux - 35, larguraAux, espessura, ))
                    print(frente_gaveta_2)
                    arquivo.write(frente_gaveta_2)
                if profundidadeModulo >= 470:
                    lateral_maior_duas_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                    lateral_menor_duas_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                    fundo_duas_gavetas = ('2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                    print(lateral_maior_duas_gavetas)
                    print(lateral_menor_duas_gavetas)
                    print(fundo_duas_gavetas)
                    arquivo.write(lateral_maior_duas_gavetas + lateral_menor_duas_gavetas + fundo_duas_gavetas)
                else:
                    lateral_duas_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, profundidadeModulo - 50,
                                                                      espessura))
                    lateral_menor_duas_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, profundidadeModulo - 50,
                                                                      espessura))
                    fundo_duas_gavetas = (
                        '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50, espessuraFundo))
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
                    gaveta_menor = math.floor(gaveta_aux - 35)
                    gaveta_maior = math.ceil(gaveta_aux * 2) - 35
                    larguraAux = largura - 10
                    total = (2 * gaveta_menor) + gaveta_maior + 105
                    lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidadeModulo, espessura)
                    print(lateral)
                    arquivo.write(lateral)

                    base_com_batente = '1x {}*{}*{} (1+) base\n'.format(larguraBase, profundidadeModulo, espessura)
                    print(base_com_batente)
                    batente = '1x {}*{}*{} (2+) batente\n'.format(larguraBase, 60, espessura)
                    print(batente)
                    arquivo.write(base_com_batente + batente)
                    if total < sub_altura:  # pega o resto e coloca na medida da gaveta maior
                        rest = sub_altura - total
                        gaveta_maior = gaveta_maior + rest
                    frente_gav_menor_3 = (
                        '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, larguraAux, espessura))
                    frente_gav_maior_3 = ('1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, larguraAux, espessura))
                    print(frente_gav_menor_3)
                    print(frente_gav_maior_3)
                    arquivo.write(frente_gav_menor_3 + frente_gav_maior_3)
                    if profundidadeModulo >= 470:
                        lateral_gav_maior_tres_gavetas = (
                            '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                        lateral_gav_menor_tres_gavetas = (
                            '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                        fundo_tres_gavetas = ('3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                        print(lateral_gav_maior_tres_gavetas)
                        print(lateral_gav_menor_tres_gavetas)
                        print(fundo_tres_gavetas)
                        arquivo.write(lateral_gav_maior_tres_gavetas + lateral_gav_menor_tres_gavetas + fundo_tres_gavetas)
                    else:
                        lateral_gav_maior_tres_gavetas = (
                            '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, profundidadeModulo - 50,
                                                                          espessura))
                        lateral_gav_menor_tres_gavetas = (
                            '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, profundidadeModulo - 50,
                                                                          espessura))
                        fundo_tres_gavetas = (
                            '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50, espessuraFundo))
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
                    gaveta_menor = math.floor(gaveta_aux - 35)  # math.floor() arredonda para baixo
                    gaveta_maior = math.ceil(gaveta_aux) - 35  # math.ceil() arredonda para cima
                    larguraAux = largura - 10
                    rest = sub_altura
                    total = gaveta_menor + rest
                    rest2 = sub_altura - total

                    lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidadeModulo, espessura)
                    print(lateral)

                    base_com_batente = '1x {}*{}*{} (1+) base\n'.format(larguraBase, profundidadeModulo,
                                                                        espessura)
                    print(base_com_batente)
                    batente_2 = '1x {}*{}*{} (2+) batente\n'.format(larguraBase, 60, espessura)
                    print(batente_2)

                    if total < sub_altura:  # pega o resto e coloca na medida da gaveta maior
                        rest = sub_altura - total
                        gaveta_maior = gaveta_maior + rest
                    frente_gav_menor_3 = (
                        '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, larguraAux, espessura))
                    frente_gav_maior_3 = (
                        '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, larguraAux, espessura))
                    print(frente_gav_menor_3)
                    print(frente_gav_maior_3)

                    if profundidadeModulo >= 470:
                        lateral_gav_maior_tres_gavetas = (
                            '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                        lateral_gav_menor_tres_gavetas = (
                            '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                        fundo_tres_gavetas = ('3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                        print(lateral_gav_maior_tres_gavetas)
                        print(lateral_gav_menor_tres_gavetas)
                        print(fundo_tres_gavetas)

                    else:
                        lateral_maior_tres_gavetas = (
                            '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, profundidadeModulo - 50,
                                                                          espessura))
                        lateral_menor_tres_gavetas = (
                            '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, profundidadeModulo - 50,
                                                                          espessura))
                        fundo_tres_gavetas = (
                            '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50, espessuraFundo))
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
                larguraAux = largura - 10
                total = gaveta_aux - 35
                fundo_gav = largura - 57
                lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidadeModulo, espessura)
                print(lateral)
                arquivo.write(lateral)

                base_com_batente = '1x {}*{}*{} (1+) base\n'.format(larguraBase, profundidadeModulo, espessura)
                print(base_com_batente)
                batente = '1x {}*{}*{} (2+) batente\n'.format(larguraBase, 60, espessura)
                print(batente)
                arquivo.write(base_com_batente + batente)
                if total > sub_altura:  # pega o resto e coloca na medida da gaveta maior
                    rest = sub_altura - total
                    gaveta_maior = gaveta_maior + rest
                frente_gav_menor_quatro_gavetas = (
                    '3x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, larguraAux, espessura))
                frente_gav_maior_quatro_gavetas = ('1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, larguraAux, espessura))
                print(frente_gav_menor_quatro_gavetas)
                print(frente_gav_maior_quatro_gavetas)
                arquivo.write(frente_gav_menor_quatro_gavetas + frente_gav_maior_quatro_gavetas)
                if profundidadeModulo >= 470:
                    lateral_quatro_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                    lateral_menor_quatro_gavetas = (
                        '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                    fundo_quatro_gavetas = ('3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                    print(lateral_quatro_gavetas)
                    print(lateral_menor_quatro_gavetas)
                    print(fundo_quatro_gavetas)
                    arquivo.write(lateral_quatro_gavetas + lateral_menor_quatro_gavetas + fundo_quatro_gavetas)
                else:
                    lateral_quatro_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, profundidadeModulo - 50,
                                                                      espessura))
                    lateral_menor_quatro_gavetas = (
                        '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, profundidadeModulo - 50,
                                                                      espessura))
                    fundo_quatro_gavetas = (
                        '4x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50, espessuraFundo))
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
    elif tipo == '7':
        altura = int(input('Qual é a altura? '))
        largura = int(input('Qual é a largura? '))
        larguraBase = largura - 30
        larguraAux = largura - 10
        espessura = 15
        espessuraFundo = 6
        profundidadeModulo = int(input('Qual é a profundidade? '))
        quantidade_gavetas = int(input('Quantas gavetas? '))
        if quantidade_gavetas == 1:
            sub_altura = altura - 10
            fundo_gav = largura - 57
            gaveta = sub_altura
            one_drawer = ('1x {}*{}*{} (4L) frente gav\n'.format(gaveta, larguraAux, espessura))
            arquivo.write(one_drawer)

            if profundidadeModulo >= 470:
                lateral_uma_gaveta = ('2x {}*{}*{} (1+) lateral gav\n'.format(gaveta, '420', espessura))
                fundo_uma_gaveta = ('1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                print(lateral_uma_gaveta)
                print(fundo_uma_gaveta)
                arquivo.write(lateral_uma_gaveta)
                arquivo.write(fundo_uma_gaveta)
            else:
                lateral_uma_gaveta = (
                    '2x {}*{}*{} (1+) lateral gav\n'.format(gaveta, profundidadeModulo - 50,
                                                            espessura))
                fundo_uma_gaveta = (
                    '1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50,
                                                          espessuraFundo))
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
            if total > sub_altura:  # pega o resto e coloca na medida da gaveta maior
                rest = sub_altura - total
                gaveta_maior = gaveta_maior + rest
                frente_gav_2 = (
                    "1x {}*{}*{} (4L) frente gav menor\n".format(gaveta_menor, larguraAux, espessura))
                frente_gav_maior_2 = (
                    "1x {}*{}*{} (4L) frente gav maior\n".format(gaveta_maior, larguraAux, espessura))
                print(frente_gav_2)
                print(frente_gav_maior_2)
                arquivo.write(frente_gav_2 + frente_gav_maior_2)

            if total == sub_altura:
                frente_gav2 = ('2x {}*{}*{} frente gav\n '.format(gaveta_aux, larguraAux, espessura, ))
                print(frente_gav2)
                arquivo.write(frente_gav2)
            if profundidadeModulo >= 470:
                lateral_duas_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                lateral_menor_duas_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                fundo_duas_gavetas = (
                    '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                print(lateral_duas_gavetas)
                print(lateral_menor_duas_gavetas)
                print(fundo_duas_gavetas)
                arquivo.write(lateral_duas_gavetas + lateral_menor_duas_gavetas + fundo_duas_gavetas)
            else:
                lateral_duas_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                  profundidadeModulo - 50, espessura))
                lateral_menor_duas_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                  profundidadeModulo - 50, espessura))
                fundo_duas_gavetas = (
                    '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50,
                                                          espessuraFundo))
                print(lateral_duas_gavetas)
                print(lateral_menor_duas_gavetas)
                print(fundo_duas_gavetas)
                arquivo.write(lateral_duas_gavetas + lateral_menor_duas_gavetas + fundo_duas_gavetas)
            frente_verso = largura - 87
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
                gaveta_menor = math.floor(gaveta_aux)
                gaveta_maior = math.ceil(gaveta_aux * 2)
                larguraAux = largura - 10
                total = (2 * gaveta_menor) + gaveta_maior + 105
                if total < sub_altura:  # pega o resto e coloca na medida da gaveta maior
                    rest = sub_altura - total
                    gaveta_maior = gaveta_maior + rest
                frente_gav_menor_3 = (
                    '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, larguraAux, espessura))
                frente_gav_3 = (
                    '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior + 1, larguraAux, espessura))
                print(frente_gav_menor_3)
                print(frente_gav_3)

                if profundidadeModulo >= 470:
                    lateral_tres_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                    lateral_menor_tres_gavetas = (
                        '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                    fundo_tres_gavetas = (
                        '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                    print(lateral_tres_gavetas)
                    print(lateral_menor_tres_gavetas)
                    print(fundo_tres_gavetas)

                else:
                    lateral_tres_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                      profundidadeModulo - 50, espessura))
                    lateral_menor_tres_gavetas = (
                        '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                      profundidadeModulo - 50, espessura))
                    fundo_tres_gavetas = (
                        '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50,
                                                              espessuraFundo))
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
                gaveta_menor = math.floor(gaveta_aux - 35)
                gaveta_maior = math.ceil(gaveta_aux) - 35
                larguraAux = largura - 10
                rest = sub_altura
                total = gaveta_menor + rest
                rest2 = sub_altura - total

                lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidadeModulo, espessura)
                print(lateral)

                base_com_batente = '1x {}*{}*{} (1+) base\n'.format(larguraBase, profundidadeModulo,
                                                                    espessura)
                print(base_com_batente)
                batente_2 = '1x {}*{}*{} (2+) batente\n'.format(larguraBase, 60, espessura)
                print(batente_2)

                if total < sub_altura:  # pega o resto e coloca na medida da gaveta maior
                    rest = sub_altura - total
                    gaveta_maior = gaveta_maior + rest
                frente_gav_menor_3 = (
                    '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, larguraAux, espessura))
                frente_gav_maior_3 = (
                    '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, larguraAux, espessura))
                print(frente_gav_menor_3)
                print(frente_gav_maior_3)

                if profundidadeModulo >= 470:
                    lateral_gav_maior_tres_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                    lateral_gav_menor_tres_gavetas = (
                        '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                    fundo_tres_gavetas = ('3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                    print(lateral_gav_maior_tres_gavetas)
                    print(lateral_gav_menor_tres_gavetas)
                    print(fundo_tres_gavetas)

                else:
                    lateral_maior_tres_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, profundidadeModulo - 50,
                                                                      espessura))
                    lateral_menor_tres_gavetas = (
                        '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, profundidadeModulo - 50,
                                                                      espessura))
                    fundo_tres_gavetas = (
                        '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50, espessuraFundo))
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
            larguraAux = largura - 10
            total = gaveta_aux - 35
            fundo_gav = largura - 57
            if total > sub_altura:  # pega o resto e coloca na medida da gaveta maior
                rest = sub_altura - total
                gaveta_maior = gaveta_maior + rest
            frente_gav_menor_quatro_gavetas = (
                '3x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, larguraAux, espessura))
            frente_gav_quatro_gavetas = (
                '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, larguraAux, espessura))
            print(frente_gav_menor_quatro_gavetas)
            print(frente_gav_quatro_gavetas)
            arquivo.write(frente_gav_menor_quatro_gavetas + frente_gav_quatro_gavetas)
            if profundidadeModulo >= 470:
                lateral_quatro_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                lateral_menor_quatro_gavetas = (
                    '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                fundo_quatro_gavetas = (
                    '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                print(lateral_quatro_gavetas)
                print(lateral_menor_quatro_gavetas)
                print(fundo_quatro_gavetas)
                arquivo.write(lateral_quatro_gavetas + lateral_menor_quatro_gavetas + fundo_quatro_gavetas)
            else:
                lateral_quatro_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                  profundidadeModulo - 50, espessura))
                lateral_menor_quatro_gavetas = (
                    '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                  profundidadeModulo - 50, espessura))
                fundo_quatro_gavetas = (
                    '4x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50,
                                                          espessuraFundo))
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

    elif tipo == '8':
        quantidade_gavetas = int(input('Quantas gavetas? '))
        altura = int(input('Qual é a altura? '))
        largura = int(input('Qual é a largura? '))
        larguraBase = largura - 30
        larguraAux = largura - 10
        espessura = 15
        espessuraFundo = 6
        profundidadeModulo = int(input('Qual é a profundidade? '))

        lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidadeModulo, espessura)
        print(lateral)
        arquivo.write(lateral)

        base_com_batente = '1x {}*{}*{} (1+) base\n'.format(larguraBase, profundidadeModulo, espessura)
        print(base_com_batente)
        batente = '1x {}*{}*{} (2+) batente\n'.format(larguraBase, 60, espessura)
        print(batente)
        arquivo.write(base_com_batente + batente)

        if quantidade_gavetas == 1:
            sub_altura = altura - 10 - 80
            fundo_gav = largura - 57
            gaveta = sub_altura - 35

            frente_uma_gaveta = ('1x {}*{}*{} (4L) frente gav\n'.format(gaveta, larguraAux, espessura))
            arquivo.write(frente_uma_gaveta)

            if profundidadeModulo >= 470:
                lateral_uma_gaveta = ('2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, '420', espessura))
                fundo_uma_gaveta = ('1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                print(lateral_uma_gaveta)
                print(fundo_uma_gaveta)
                arquivo.write(lateral_uma_gaveta)
                arquivo.write(fundo_uma_gaveta)
            else:
                lateral_uma_gaveta = (
                        '2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, profundidadeModulo - 50,
                                                                espessura))
                fundo_uma_gaveta = (
                        '1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50,
                                                              espessuraFundo))
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
                if total > sub_altura:  # pega o resto e coloca na medida da gaveta maior
                    rest = sub_altura - total
                    gaveta_maior = gaveta_maior + rest
                    frente_gav_2 = (
                        "1x {}*{}*{} (4L) frente gav menor\n".format(gaveta_menor, larguraAux, espessura))
                    frente_gav_maior_2 = (
                        "1x {}*{}*{} (4L) frente gav maior\n".format(gaveta_maior, larguraAux, espessura))
                    print(frente_gav_2)
                    print(frente_gav_maior_2)
                    arquivo.write(frente_gav_2 + frente_gav_maior_2)

                if total == sub_altura:
                    frente_gav2 = ('2x {}*{}*{} frente gav\n '.format(gaveta_aux - 35, larguraAux, espessura, ))
                    print(frente_gav2)
                    arquivo.write(frente_gav2)
                if profundidadeModulo >= 470:
                    lateral_duas_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                    lateral_menor_duas_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                    fundo_duas_gavetas = (
                        '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                    print(lateral_duas_gavetas)
                    print(lateral_menor_duas_gavetas)
                    print(fundo_duas_gavetas)
                    arquivo.write(lateral_duas_gavetas + lateral_menor_duas_gavetas + fundo_duas_gavetas)
                else:
                    lateral_duas_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                      profundidadeModulo - 50, espessura))
                    lateral_menor_duas_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                      profundidadeModulo - 50, espessura))
                    fundo_duas_gavetas = (
                        '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50,
                                                              espessuraFundo))
                    print(lateral_duas_gavetas)
                    print(lateral_menor_duas_gavetas)
                    print(fundo_duas_gavetas)
                    arquivo.write(lateral_duas_gavetas + lateral_menor_duas_gavetas + fundo_duas_gavetas)
                frente_verso = largura - 87
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
                    gaveta_menor = math.floor(gaveta_aux - 35)
                    gaveta_maior = math.ceil(gaveta_aux * 2) - 35
                    larguraAux = largura - 10
                    total = (2 * gaveta_menor) + gaveta_maior + 105
                    if total < sub_altura:  # pega o resto e coloca na medida da gaveta maior
                        rest = sub_altura - total
                        gaveta_maior = gaveta_maior + rest
                        frenteGavMenor3 = (
                            '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, larguraAux, espessura))
                        frenteGavMaior3 = (
                            '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, larguraAux, espessura))
                        print(frenteGavMenor3)
                        print(frenteGavMaior3)
                        arquivo.write(frenteGavMenor3 + frenteGavMaior3)

                        if profundidadeModulo >= 470:
                            lateralMaiorTresGavetas = (
                                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                            lateralMenorTresGavetas = (
                                '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                            fundoTresGavetas = (
                                '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                            print(lateralMaiorTresGavetas)
                            print(lateralMenorTresGavetas)
                            print(fundoTresGavetas)
                            arquivo.write(lateralMaiorTresGavetas + lateralMenorTresGavetas + fundoTresGavetas)

                        else:
                            lateralMaiorTresGavetas = (
                                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                              profundidadeModulo - 50, espessura))
                            lateralMenorTresGavetas = (
                                '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                              profundidadeModulo - 50, espessura))
                            fundoTresGavetas = (
                                '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50,
                                                                      espessuraFundo))
                            print(lateralMaiorTresGavetas)
                            print(lateralMenorTresGavetas)
                            print(fundoTresGavetas)
                            arquivo.write(lateralMaiorTresGavetas + lateralMenorTresGavetas + fundoTresGavetas)

                        frenteVerso = largura - 87
                        frenteVersoMenorTresGav = (
                            '4x {}*{}*{} (1+) frente/verso gav menor\n'.format(frenteVerso, gaveta_menor - 35,
                                                                               espessura))
                        frenteVersoMaiorTresGav = (
                            '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(frenteVerso, gaveta_maior - 35,
                                                                               espessura))
                        print(frenteVersoMenorTresGav)
                        print(frenteVersoMaiorTresGav)
                        arquivo.write(frenteVersoMenorTresGav + frenteVersoMaiorTresGav)

                else:
                    sub_altura = altura - 20 - 80
                    fundo_gav = largura - 57
                    gaveta_aux = sub_altura / 3
                    gaveta_menor = math.floor(gaveta_aux - 35)
                    gaveta_maior = math.ceil(gaveta_aux) - 35
                    larguraAux = largura - 10
                    total = gaveta_menor + gaveta_maior + 105
                    if total < sub_altura:  # pega o resto e coloca na medida da gaveta maior
                        rest = sub_altura - total
                        gaveta_maior = gaveta_maior + rest - gaveta_menor
                        frenteGavMenor3 = (
                            '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, larguraAux, espessura))
                        frenteGavMaior3 = (
                            '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, larguraAux, espessura))
                        print(frenteGavMenor3)
                        print(frenteGavMaior3)
                        arquivo.write(frenteGavMenor3 + frenteGavMaior3)

                        if profundidadeModulo >= 470:
                            lateral_tres_gavetas = (
                                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                            lateral_menor_tres_gavetas = (
                                '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                            fundo_tres_gavetas = (
                                '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                            print(lateral_tres_gavetas)
                            print(lateral_menor_tres_gavetas)
                            print(fundo_tres_gavetas)
                            arquivo.write(lateral_tres_gavetas + lateral_menor_tres_gavetas + fundo_tres_gavetas)

                        else:
                            lateral_tres_gavetas = (
                                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                              profundidadeModulo - 50, espessura))
                            lateral_menor_tres_gavetas = (
                                '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                              profundidadeModulo - 50, espessura))
                            fundo_tres_gavetas = (
                                '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50,
                                                                      espessuraFundo))
                            print(lateral_tres_gavetas)
                            print(lateral_menor_tres_gavetas)
                            print(fundo_tres_gavetas)
                            arquivo.write(lateral_tres_gavetas + lateral_menor_tres_gavetas + fundo_tres_gavetas)

                        frente_verso = largura - 87
                        frente_verso_menor_tres_gavetas = (
                            '4x {}*{}*{} (1+) frente/verso gav menor\n'.format(frente_verso, gaveta_menor - 35,
                                                                               espessura))
                        frente_verso_tres_gavetas = (
                            '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(frente_verso, gaveta_maior - 35,
                                                                               espessura))
                        print(frente_verso_menor_tres_gavetas)
                        print(frente_verso_tres_gavetas)
                        arquivo.write(frente_verso_menor_tres_gavetas + frente_verso_tres_gavetas)

            if quantidade_gavetas == 4:
                sub_altura = altura - 25 - 80
                gaveta_aux = (sub_altura / 4)
                gaveta_menor = math.floor(gaveta_aux - 35)
                gaveta_aux2 = gaveta_aux % 1
                gaveta_maior = math.ceil(gaveta_aux + gaveta_aux2 - 35)
                larguraAux = largura - 10
                total = gaveta_aux - 35
                fundo_gav = largura - 57
                if total > sub_altura:  # pega o resto e coloca na medida da gaveta maior
                    rest = sub_altura - total
                    gaveta_maior = gaveta_maior + rest
                frente_gav_menor_quatro_gavetas = (
                    '3x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, larguraAux, espessura))
                frente_gav_quatro_gavetas = (
                    '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, larguraAux, espessura))
                print(frente_gav_menor_quatro_gavetas)
                print(frente_gav_quatro_gavetas)
                arquivo.write(frente_gav_menor_quatro_gavetas + frente_gav_quatro_gavetas)
                if profundidadeModulo >= 470:
                    lateral_quatro_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                    lateral_menor_quatro_gavetas = (
                        '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                    fundo_quatro_gavetas = (
                        '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                    print(lateral_quatro_gavetas)
                    print(lateral_menor_quatro_gavetas)
                    print(fundo_quatro_gavetas)
                    arquivo.write(lateral_quatro_gavetas + lateral_menor_quatro_gavetas + fundo_quatro_gavetas)
                else:
                    lateral_quatro_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                      profundidadeModulo - 50, espessura))
                    lateral_menor_quatro_gavetas = (
                        '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                      profundidadeModulo - 50, espessura))
                    fundo_quatro_gavetas = (
                        '4x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50,
                                                              espessuraFundo))
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

    elif tipo == '9':
        quantidade_gavetas = int(input('Quantas gavetas? '))
        altura = int(input('Qual é a altura? '))
        largura = int(input('Qual é a largura? '))
        larguraBase = largura - 30
        larguraAux = largura - 10
        espessura = 15
        espessuraFundo = 6
        profundidadeModulo = int(input('Qual é a profundidade? '))

        lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidadeModulo, espessura)
        print(lateral)
        arquivo.write(lateral)

        base_com_batente = '1x {}*{}*{} (1+) base\n'.format(larguraBase, profundidadeModulo, espessura)
        print(base_com_batente)
        batente = '1x {}*{}*{} (2+) batente\n'.format(larguraBase, 60, espessura)
        print(batente)
        arquivo.write(base_com_batente + batente)

        if quantidade_gavetas == 1:
            sub_altura = altura - 10 - 80
            fundo_gav = largura - 57
            gaveta = sub_altura

            frente_uma_gaveta = ('1x {}*{}*{} (4L) frente gav\n'.format(gaveta, larguraAux, espessura))
            arquivo.write(frente_uma_gaveta)

            if profundidadeModulo >= 470:
                lateral_uma_gaveta = ('2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, '420', espessura))
                fundo_uma_gaveta = ('1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                print(lateral_uma_gaveta)
                print(fundo_uma_gaveta)
                arquivo.write(lateral_uma_gaveta)
                arquivo.write(fundo_uma_gaveta)
            else:
                lateral_uma_gaveta = (
                    '2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, profundidadeModulo - 50,
                                                            espessura))
                fundo_uma_gaveta = (
                    '1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50,
                                                          espessuraFundo))
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
            if total > sub_altura:  # pega o resto e coloca na medida da gaveta maior
                rest = sub_altura - total
                gaveta_maior = gaveta_maior + rest
                frente_gav_2 = (
                    "1x {}*{}*{} (4L) frente gav menor\n".format(gaveta_menor, larguraAux, espessura))
                frente_gav_maior_2 = (
                    "1x {}*{}*{} (4L) frente gav maior\n".format(gaveta_maior, larguraAux, espessura))
                print(frente_gav_2)
                print(frente_gav_maior_2)
                arquivo.write(frente_gav_2 + frente_gav_maior_2)

            if total == sub_altura:
                frente_gav_2 = ('2x {}*{}*{} frente gav\n '.format(gaveta_aux - 35, larguraAux, espessura, ))
                print(frente_gav_2)
                arquivo.write(frente_gav_2)
            if profundidadeModulo >= 470:
                lateral_duas_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                lateral_menor_duas_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                fundo_duas_gavetas = (
                    '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                print(lateral_duas_gavetas)
                print(lateral_menor_duas_gavetas)
                print(fundo_duas_gavetas)
                arquivo.write(lateral_duas_gavetas + lateral_menor_duas_gavetas + fundo_duas_gavetas)
            else:
                lateral_duas_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                  profundidadeModulo - 50, espessura))
                lateral_menor_duas_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                  profundidadeModulo - 50, espessura))
                fundo_duas_gavetas = (
                    '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50,
                                                          espessuraFundo))
                print(lateral_duas_gavetas)
                print(lateral_menor_duas_gavetas)
                print(fundo_duas_gavetas)
                arquivo.write(lateral_duas_gavetas + lateral_menor_duas_gavetas + fundo_duas_gavetas)
            frenteVerso = largura-87
            frente_verso_duas_gavetas = (
                '2x {}*{}*{} (1+) frente/verso gav menor\n'.format(gaveta_menor - 35, frenteVerso, espessura))
            frente_verso_menor_duas_gavetas = (
                '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(gaveta_maior - 35, frenteVerso, espessura))
            print(frente_verso_duas_gavetas)
            print(frente_verso_menor_duas_gavetas)
            arquivo.write(frente_verso_duas_gavetas + frente_verso_menor_duas_gavetas)

        if quantidade_gavetas == 3:
            tamanho = str(input('São do mesmo tamanho? '))

            if tamanho == 'não':
                sub_altura = altura - 20 - 80
                fundo_gav = largura - 57
                gaveta_aux = sub_altura / 4
                gaveta_menor = math.floor(gaveta_aux)
                gaveta_maior = math.ceil(gaveta_aux * 2)
                larguraAux = largura - 10
                total = (2 * gaveta_menor) + gaveta_maior + 105
                if total < sub_altura:  # pega o resto e coloca na medida da gaveta maior
                    rest = sub_altura - total
                    gaveta_maior = gaveta_maior + rest
                frente_gav_menor_3 = (
                    '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, larguraAux, espessura))
                frente_gav_3 = (
                    '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior + 1, larguraAux, espessura))
                print(frente_gav_menor_3)
                print(frente_gav_3)
                arquivo.write(frente_gav_menor_3 + frente_gav_3)

                if profundidadeModulo >= 470:
                    lateral_tres_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                    lateral_menor_tres_gavetas = (
                        '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                    fundo_tres_gavetas = (
                        '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                    print(lateral_tres_gavetas)
                    print(lateral_menor_tres_gavetas)
                    print(fundo_tres_gavetas)
                    arquivo.write(lateral_tres_gavetas + lateral_menor_tres_gavetas + fundo_tres_gavetas)

                else:
                    lateral_tres_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                      profundidadeModulo - 50, espessura))
                    lateral_menor_tres_gavetas = (
                        '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                      profundidadeModulo - 50, espessura))
                    fundo_tres_gavetas = (
                        '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50,
                                                              espessuraFundo))
                    print(lateral_tres_gavetas)
                    print(lateral_menor_tres_gavetas)
                    print(fundo_tres_gavetas)
                    arquivo.write(lateral_tres_gavetas + lateral_menor_tres_gavetas + fundo_tres_gavetas)

                frente_verso = largura - 87
                frente_verso_menor_tres_gavetas = (
                    '4x {}*{}*{} (1+) frente/verso gav menor\n'.format(frente_verso, gaveta_menor - 35, espessura))
                frente_verso_tres_gavetas = (
                    '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(frente_verso, gaveta_maior - 35, espessura))
                print(frente_verso_menor_tres_gavetas)
                print(frente_verso_tres_gavetas)
                arquivo.write(frente_verso_menor_tres_gavetas + frente_verso_tres_gavetas)

            if tamanho == 'sim':
                sub_altura = altura - 20 - 80
                fundo_gav = largura - 57
                gaveta_aux = sub_altura / 3
                gaveta_menor = math.floor(gaveta_aux)
                gaveta_maior = math.ceil(gaveta_aux)
                larguraAux = largura - 10
                total = gaveta_menor + gaveta_maior + 105
                if total > sub_altura:  # pega o resto e coloca na medida da gaveta maior
                    rest = sub_altura - total
                    gaveta_maior = gaveta_maior + rest - gaveta_menor
                frente_gav_menor_3 = (
                    '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, larguraAux, espessura))
                frente_gav_3 = (
                    '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, larguraAux, espessura))
                print(frente_gav_menor_3)
                print(frente_gav_3)
                arquivo.write(frente_gav_menor_3 + frente_gav_3)

                if profundidadeModulo >= 470:
                    lateral_tres_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                    lateral_menor_tres_gavetas = (
                        '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                    fundo_tres_gavetas = (
                        '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                    print(lateral_tres_gavetas)
                    print(lateral_menor_tres_gavetas)
                    print(fundo_tres_gavetas)
                    arquivo.write(lateral_tres_gavetas + lateral_menor_tres_gavetas + fundo_tres_gavetas)

                else:
                    lateral_tres_gavetas = (
                        '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                      profundidadeModulo - 50, espessura))
                    lateral_menor_tres_gavetas = (
                        '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                      profundidadeModulo - 50, espessura))
                    fundo_tres_gavetas = (
                        '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50,
                                                              espessuraFundo))
                    print(lateral_tres_gavetas)
                    print(lateral_menor_tres_gavetas)
                    print(fundo_tres_gavetas)
                    arquivo.write(lateral_tres_gavetas + lateral_menor_tres_gavetas + fundo_tres_gavetas)

                frente_verso = largura - 87
                frente_verso_menor_tres_gavetas = (
                    '4x {}*{}*{} (1+) frente/verso gav menor\n'.format(frente_verso, gaveta_menor - 35, espessura))
                frente_verso_tres_gavetas = (
                    '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(frente_verso, gaveta_maior - 35, espessura))
                print(frente_verso_menor_tres_gavetas)
                print(frente_verso_tres_gavetas)
                arquivo.write(frente_verso_menor_tres_gavetas + frente_verso_tres_gavetas)
        if quantidade_gavetas == 4:
            sub_altura = altura - 25 - 80
            gaveta_aux = (sub_altura / 4)
            gaveta_menor = math.floor(gaveta_aux)
            gaveta_aux2 = gaveta_aux % 1
            gaveta_maior = math.ceil(gaveta_aux + gaveta_aux2)
            larguraAux = largura - 10
            total = gaveta_aux - 35
            fundo_gav = largura - 57
            if total > sub_altura:  # pega o resto e coloca na medida da gaveta maior
                rest = sub_altura - total
                gaveta_maior = gaveta_maior + rest
            frente_gav_menor_quatro_gavetas = (
                '3x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, larguraAux, espessura))
            frente_gav_quatro_gavetas = (
                '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, larguraAux, espessura))
            print(frente_gav_menor_quatro_gavetas)
            print(frente_gav_quatro_gavetas)
            arquivo.write(frente_gav_menor_quatro_gavetas + frente_gav_quatro_gavetas)
            if profundidadeModulo >= 470:
                lateral_quatro_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                lateral_menor_quatro_gavetas = (
                    '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                fundo_quatro_gavetas = (
                    '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessuraFundo))
                print(lateral_quatro_gavetas)
                print(lateral_menor_quatro_gavetas)
                print(fundo_quatro_gavetas)
                arquivo.write(lateral_quatro_gavetas + lateral_menor_quatro_gavetas + fundo_quatro_gavetas)
            else:
                lateral_quatro_gavetas = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                  profundidadeModulo - 50, espessura))
                lateral_menor_quatro_gavetas = (
                    '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                  profundidadeModulo - 50, espessura))
                fundo_quatro_gavetas = (
                    '4x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidadeModulo - 50,
                                                          espessuraFundo))
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
    else:
        print('Apenas opções sugeridas são aceitas, saindo.')

    arquivo.write('--------------------------------------------- \n'
                  )
    arquivo.close()
