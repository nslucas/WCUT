import math

nome_cliente = str(input('Qual o nome do(a) cliente? '))

tipo = str(input('O que você deseja criar? \n Opções: \n 1 - Armário comum \n 2 - Armário comum inferior de cozinha \n 3 - Microondas \n 4 - Nicho \n 5 - Porta-tempeiro \n 6 - Gaveteiro com puxador sem rodapé \n 7 - Gaveteiro sem puxador e sem rodapé  \n 8 - Gaveteiro com puxador e com rodapé \n 9 - Gaveteiro sem puxador e com rodapé \n Selecione uma opção: '  ))

arquivo = open(r"C:\Users\Positivo i5\Desktop\PLANOS DE CORTE\Plano de corte " + nome_cliente + '.txt', "a")

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
        one_prat = ('1x {}*{}*{} (1+) prat interna\n'.format(subtracao_largura, subtracao2, espessura))
        print(one_prat)
        arquivo.write(one_prat)
    if prat_int == 2:
        two_prat = ('2x {}*{}*{} (1+) prat interna\n'.format(subtracao_largura, subtracao2, espessura))
        print(two_prat)
        arquivo.write(two_prat)
    if numero_portas > 0:
        porta_puxador = altura - 45
        porta_sem_puxador = altura - 10
        porta_largura = largura - 10
        porta_largura_two = math.floor(porta_largura / 2)

        if porta == 'sim':
            if numero_portas == 1:
                one_door_handle = ('1x {}*{}*{} (4L) porta\n'.format(porta_puxador, porta_largura, espessura))
                print(one_door_handle)
                arquivo.write(one_door_handle)
            if numero_portas == 2:
                two_door_handle = ('2x {}*{}*{} (4L) porta\n'.format(porta_puxador, porta_largura_two, espessura))
                print(two_door_handle)
                arquivo.write(two_door_handle)

        if porta == 'não':
            if numero_portas == 1:
                one_door_no_handle = (
                    '1x {}*{}*{} (4L) porta\n'.format(porta_sem_puxador, porta_largura, espessura))
                print(one_door_no_handle)
                arquivo.write(one_door_no_handle)
            if numero_portas == 2:
                two_door_no_handle = (
                    '2x {}*{}*{} (4L) porta\n'.format(porta_sem_puxador, porta_largura_two, espessura, ))
                print(two_door_no_handle)
                arquivo.write(two_door_no_handle)

        back = ('1x {}*{}*{} fundo\n'.format(largura, altura, espessura_fundo))
        print(back)
        arquivo.write(back)

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

    with_batente = '1x {}*{}*{} (1+) base\n'.format(subtracao_largura, profundidade_modulo, espessura)
    print(with_batente)
    with_batente_2 = '1x {}*{}*{} (2+) batente\n'.format(subtracao_largura, 60, espessura)
    print(with_batente_2)
    arquivo.write(with_batente + with_batente_2)

    if prat_int == 1:
        one_prat = ('1x {}*{}*{} (1+) prat interna\n'.format(subtracao_largura, subtracao2, espessura))
        print(one_prat)
        arquivo.write(one_prat)
    if prat_int == 2:
        two_prat = ('2x {}*{}*{} (1+) prat interna\n'.format(subtracao_largura, subtracao2, espessura))
        print(two_prat)
        arquivo.write(two_prat)
    if numero_portas > 0:
        porta_puxador = altura - 45
        porta_sem_puxador = altura - 10
        porta_largura = largura - 10
        porta_largura_two = math.floor(porta_largura / 2)

        if porta == 'sim':
            if numero_portas == 1:
                one_door_handle = ('1x {}*{}*{} (4L) porta\n'.format(porta_puxador, porta_largura, espessura))
                print(one_door_handle)
                arquivo.write(one_door_handle)
            if numero_portas == 2:
                two_door_handle = (
                    '2x {}*{}*{} (4L) porta\n'.format(porta_puxador, porta_largura_two, espessura))
                print(two_door_handle)
                arquivo.write(two_door_handle)

        if porta == 'não':
            if numero_portas == 1:
                one_door_no_handle = (
                    '1x {}*{}*{} (4L) porta\n'.format(porta_sem_puxador, porta_largura, espessura))
                print(one_door_no_handle)
                arquivo.write(one_door_no_handle)
            if numero_portas == 2:
                two_door_no_handle = (
                    '2x {}*{}*{} (4L) porta\n'.format(porta_sem_puxador, porta_largura_two, espessura, ))
                print(two_door_no_handle)
                arquivo.write(two_door_no_handle)

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
        lat_micro = (
            '2x {}*{}*{} (1+/1-) lateral mod micro'.format(altura, profundidade_fundo_encaixado, espessura))
        print(lat_micro)
        arquivo.write(lat_micro)

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
    printBaseSuperior = '2x {}*{}*{} (1+) base/superior\n'.format(subtracao_largura, profundidade_modulo, espessura)
    print(printBaseSuperior)
    arquivo.write(printBaseSuperior)
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
    fren_vers = 85
    largura_aux_2 = largura - 89
    fundo = fren_vers + 15
    altura_int = 85

    lateral_caixa = (
        '2x {}*{}*{} (1+/1-) lateral mod porta tempero\n'.format(altura, profundidade_modulo, espessura, ))
    base_caixa = ('1x {}*{}*{} (1+) base mod porta tempero\n'.format(subtracao_largura, profundidade_modulo,
                                                                     espessura))
    batente_caixa = ('1x {}*{}*{} (2+) batente\n'.format(subtracao_largura, 60, espessura))
    frente_caixa = (
        '1x {}*{}*{} (4L) frente mod porta tempero\n'.format(porta_puxador, largura_aux, espessura))
    lateral_maior_int = ('1x {}*{}*{} (1+/1-) lateral maior mod porta tempero\n'.format(lateral_int,
                                                                                        profundidade_modulo - 50,
                                                                                        espessura))
    lateral_menor_int = (
        '2x {}*{}*{} (1+/1-) lateral menor mod porta tempero\n'.format(altura_int, profundidade_modulo - 50,
                                                                       espessura))
    fren_vers_int = (
        '4x {}*{}*{} (1+) frente/verso mod porta tempero\n'.format(fren_vers, largura_aux_2, espessura))
    fundo_tempero = (
        '2x {}*{}*{} (2+) fundo porta tempero\n'.format(profundidade_modulo - 50, largura_aux_2 + 15,
                                                        espessura_fundo))
    print(lateral_caixa)
    print(base_caixa)
    print(batente_caixa)
    print(frente_caixa)
    print(lateral_maior_int)
    print(lateral_menor_int)
    print(fren_vers_int)
    print(fundo_tempero)
    arquivo.write(
        lateral_caixa + base_caixa + batente_caixa + frente_caixa + lateral_maior_int + lateral_menor_int + fren_vers_int + fundo_tempero)


if tipo == '6':
        arquivo = open(r"C:\Users\Positivo i5\Desktop\PLANOS DE CORTE\Plano de corte " + nome_cliente + '.txt', "a")
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

            with_batente = '1x {}*{}*{} (1+) base\n'.format(subtracao_largura, profundidade_modulo, espessura)
            print(with_batente)
            with_batente_2 = '1x {}*{}*{} (2+) batente\n'.format(subtracao_largura, 60, espessura)
            print(with_batente_2)
            arquivo.write(with_batente + with_batente_2)

            one_drawer = ('1x {}*{}*{} (4L) frente gav\n'.format(gaveta, largura_aux, espessura))
            arquivo.write(one_drawer)

            if profundidade_modulo >= 470:
                lat_one_drawer = ('2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, '420', espessura))
                back_one_drawer = ('1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                print(lat_one_drawer)
                print(back_one_drawer)
                arquivo.write(lat_one_drawer)
                arquivo.write(back_one_drawer)
            else:
                lat_one_drawer = (
                    '2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, profundidade_modulo - 50, espessura))
                back_one_drawer = (
                    '1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50, espessura_fundo))
                print(lat_one_drawer)
                print(back_one_drawer)
                arquivo.write(lat_one_drawer + back_one_drawer)
                fren_vers = largura - 87
                front_back_one_drawer = (
                    '2x {}*{}*{} (1+) frente/verso gav\n'.format(gaveta - 35, fren_vers, espessura))
                print(front_back_one_drawer)
                arquivo.write(front_back_one_drawer)

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

            with_batente = '1x {}*{}*{} (1+) base\n'.format(subtracao_largura, profundidade_modulo, espessura)
            print(with_batente)
            with_batente_2 = '1x {}*{}*{} (2+) batente\n'.format(subtracao_largura, 60, espessura)
            print(with_batente_2)
            arquivo.write(with_batente + with_batente_2)
            if total > sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                rest = sub_altura - total
                gaveta_maior = gaveta_maior + rest
            front_gav_2 = ("1x {}*{}*{} (4L) frente gav menor\n".format(gaveta_menor, largura_aux, espessura))
            print(front_gav_2)
            arquivo.write(front_gav_2)
            front_gav_bigger_2 = ("1x {}*{}*{} (4L) frente gav maior\n".format(gaveta_maior, largura_aux, espessura))
            print(front_gav_bigger_2)
            arquivo.write(front_gav_bigger_2)

            if total == sub_altura:
                front_gav_2 = ('2x {}*{}*{} frente gav\n '.format(gaveta_aux - 35, largura_aux, espessura, ))
                print(front_gav_2)
                arquivo.write(front_gav_2)
            if profundidade_modulo >= 470:
                lat_two_drawers = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                lat_smaller_two_drawers = (
                    '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                back_two_drawers = ('2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                print(lat_two_drawers)
                print(lat_smaller_two_drawers)
                print(back_two_drawers)
                arquivo.write(lat_two_drawers + lat_smaller_two_drawers + back_two_drawers)
            else:
                lat_two_drawers = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, profundidade_modulo - 50,
                                                                  espessura))
                lat_smaller_two_drawers = (
                    '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, profundidade_modulo - 50,
                                                                  espessura))
                back_two_drawers = (
                    '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50, espessura_fundo))
                print(lat_two_drawers)
                print(lat_smaller_two_drawers)
                print(back_two_drawers)
                arquivo.write(lat_two_drawers + lat_smaller_two_drawers + back_two_drawers)
            fren_vers = largura - 87
            front_back_two_drawer = (
                '2x {}*{}*{} (1+) frente/verso gav menor\n'.format(gaveta_menor - 35, fren_vers, espessura))
            front_back_smaller_two_drawer = (
                '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(gaveta_maior - 35, fren_vers, espessura))
            print(front_back_two_drawer)
            print(front_back_smaller_two_drawer)
            arquivo.write(front_back_two_drawer + front_back_smaller_two_drawer)

        if quantidadeGavetas == 3:
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

            with_batente = '1x {}*{}*{} (1+) base\n'.format(subtracao_largura, profundidade_modulo, espessura)
            print(with_batente)
            with_batente_2 = '1x {}*{}*{} (2+) batente\n'.format(subtracao_largura, 60, espessura)
            print(with_batente_2)
            arquivo.write(with_batente + with_batente_2)
            if total < sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                rest = sub_altura - total
                gaveta_maior = gaveta_maior + rest
            front_gav_smaller_3 = (
                '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
            front_gav_3 = ('1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, largura_aux, espessura))
            print(front_gav_smaller_3)
            print(front_gav_3)
            arquivo.write(front_gav_smaller_3 + front_gav_3)
            if profundidade_modulo >= 470:
                lat_three_drawers = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                lat_smaller_three_drawers = (
                    '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                back_three_drawers = ('3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                print(lat_three_drawers)
                print(lat_smaller_three_drawers)
                print(back_three_drawers)
                arquivo.write(lat_three_drawers + lat_smaller_three_drawers + back_three_drawers)
            else:
                lat_three_drawers = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, profundidade_modulo - 50,
                                                                  espessura))
                lat_smaller_three_drawers = (
                    '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, profundidade_modulo - 50,
                                                                  espessura))
                back_three_drawers = (
                    '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50, espessura_fundo))
                print(lat_three_drawers)
                print(lat_smaller_three_drawers)
                print(back_three_drawers)
                arquivo.write(lat_three_drawers + lat_smaller_three_drawers + back_three_drawers)
            fren_vers = largura - 87
            front_back_smaller_three_drawers = (
                '4x {}*{}*{} (1+) frente/verso gav menor\n'.format(fren_vers, gaveta_menor - 35, espessura))
            front_back_three_drawers = (
                '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(fren_vers, gaveta_maior - 35, espessura))
            print(front_back_smaller_three_drawers)
            print(front_back_three_drawers)
            arquivo.write(front_back_smaller_three_drawers + front_back_three_drawers)

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

            with_batente = '1x {}*{}*{} (1+) base\n'.format(subtracao_largura, profundidade_modulo, espessura)
            print(with_batente)
            with_batente_2 = '1x {}*{}*{} (2+) batente\n'.format(subtracao_largura, 60, espessura)
            print(with_batente_2)
            arquivo.write(with_batente + with_batente_2)
            if total > sub_altura:  ## pega o resto e coloca na medida da gaveta maior
                rest = sub_altura - total
                gaveta_maior = gaveta_maior + rest
            front_gav_smaller_four = (
                '3x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
            front_gav_four = ('1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, largura_aux, espessura))
            print(front_gav_smaller_four)
            print(front_gav_four)
            arquivo.write(front_gav_smaller_four + front_gav_four)
            if profundidade_modulo >= 470:
                lat_four_drawers = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                lat_four_smaller_drawers = (
                    '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                back_four_drawers = ('3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                print(lat_four_drawers)
                print(lat_four_smaller_drawers)
                print(back_four_drawers)
                arquivo.write(lat_four_drawers + lat_four_smaller_drawers + back_four_drawers)
            else:
                lat_four_drawers = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, profundidade_modulo - 50,
                                                                  espessura))
                lat_four_smaller_drawers = (
                    '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, profundidade_modulo - 50,
                                                                  espessura))
                back_four_drawers = (
                    '4x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50, espessura_fundo))
                print(lat_four_drawers)
                print(lat_four_smaller_drawers)
                print(back_four_drawers)
                arquivo.write(lat_four_drawers + lat_four_smaller_drawers + back_four_drawers)
            fren_vers = largura - 87
            front_back_four_smaller_drawers = (
                '6x {}*{}*{} (1+) frente/verso gav menor\n'.format(fren_vers, gaveta_menor - 35, espessura))
            front_back_four_drawers = (
                '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(fren_vers, gaveta_maior - 35, espessura))
            print(front_back_four_smaller_drawers)
            print(front_back_four_drawers)
            arquivo.write(front_back_four_smaller_drawers + front_back_four_drawers)
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
            lat_one_drawer = ('2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, '420', espessura))
            back_one_drawer = ('1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
            print(lat_one_drawer)
            print(back_one_drawer)
            arquivo.write(lat_one_drawer)
            arquivo.write(back_one_drawer)
        else:
            lat_one_drawer = (
                '2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, profundidade_modulo - 50,
                                                        espessura))
            back_one_drawer = (
                '1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                      espessura_fundo))
            print(lat_one_drawer)
            print(back_one_drawer)
            arquivo.write(lat_one_drawer + back_one_drawer)
        fren_vers = largura - 87
        front_back_one_drawer = (
            '2x {}*{}*{} (1+) frente/verso gav\n'.format(gaveta - 35, fren_vers, espessura))
        print(front_back_one_drawer)
        arquivo.write(front_back_one_drawer)

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
            front_gav_2 = (
                "1x {}*{}*{} (4L) frente gav menor\n".format(gaveta_menor, largura_aux, espessura))
            front_gav_bigger_2 = (
                "1x {}*{}*{} (4L) frente gav maior\n".format(gaveta_maior, largura_aux, espessura))
            print(front_gav_2)
            print(front_gav_bigger_2)
            arquivo.write(front_gav_2 + front_gav_bigger_2)

        if total == sub_altura:
            front_gav2 = ('2x {}*{}*{} frente gav\n '.format(gaveta_aux - 35, largura_aux, espessura, ))
            print(front_gav_2)
            arquivo.write(front_gav2)
        if profundidade_modulo >= 470:
            lat_two_drawers = (
                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
            lat_smaller_two_drawers = (
                '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
            back_two_drawers = (
                '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
            print(lat_two_drawers)
            print(lat_smaller_two_drawers)
            print(back_two_drawers)
            arquivo.write(lat_two_drawers + lat_smaller_two_drawers + back_two_drawers)
        else:
            lat_two_drawers = (
                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                              profundidade_modulo - 50, espessura))
            lat_smaller_two_drawers = (
                '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                              profundidade_modulo - 50, espessura))
            back_two_drawers = (
                '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                      espessura_fundo))
            print(lat_two_drawers)
            print(lat_smaller_two_drawers)
            print(back_two_drawers)
            arquivo.write(lat_two_drawers + lat_smaller_two_drawers + back_two_drawers)

        front_back_two_drawer = (
            '2x {}*{}*{} (1+) frente/verso gav menor\n'.format(gaveta_menor - 35, fren_vers, espessura))
        front_back_smaller_two_drawer = (
            '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(gaveta_maior - 35, fren_vers, espessura))
        print(front_back_two_drawer)
        print(front_back_smaller_two_drawer)
        arquivo.write(front_back_two_drawer + front_back_smaller_two_drawer)

    if quantidade_gavetas == 3:
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
        front_gav_smaller_3 = (
            '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
        front_gav_3 = (
            '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, largura_aux, espessura))
        print(front_gav_smaller_3)
        print(front_gav_3)
        arquivo.write(front_gav_smaller_3 + front_gav_3)
        if profundidade_modulo >= 470:
            lat_three_drawers = (
                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
            lat_smaller_three_drawers = (
                '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
            back_three_drawers = (
                '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
            print(lat_three_drawers)
            print(lat_smaller_three_drawers)
            print(back_three_drawers)
            arquivo.write(lat_three_drawers + lat_smaller_three_drawers + back_three_drawers)
        else:
            lat_three_drawers = (
                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                              profundidade_modulo - 50, espessura))
            lat_smaller_three_drawers = (
                '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                              profundidade_modulo - 50, espessura))
            back_three_drawers = (
                '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                      espessura_fundo))
            print(lat_three_drawers)
            print(lat_smaller_three_drawers)
            print(back_three_drawers)
            arquivo.write(lat_three_drawers + lat_smaller_three_drawers + back_three_drawers)
        fren_vers = largura - 87
        front_back_smaller_three_drawers = (
            '4x {}*{}*{} (1+) frente/verso gav menor\n'.format(fren_vers, gaveta_menor - 35, espessura))
        front_back_three_drawers = (
            '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(fren_vers, gaveta_maior - 35, espessura))
        print(front_back_smaller_three_drawers)
        print(front_back_three_drawers)
        arquivo.write(front_back_smaller_three_drawers + front_back_three_drawers)

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
        front_gav_smaller_four = (
            '3x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
        front_gav_four = (
            '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, largura_aux, espessura))
        print(front_gav_smaller_four)
        print(front_gav_four)
        arquivo.write(front_gav_smaller_four + front_gav_four)
        if profundidade_modulo >= 470:
            lat_four_drawers = (
                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
            lat_four_smaller_drawers = (
                '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
            back_four_drawers = (
                '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
            print(lat_four_drawers)
            print(lat_four_smaller_drawers)
            print(back_four_drawers)
            arquivo.write(lat_four_drawers + lat_four_smaller_drawers + back_four_drawers)
        else:
            lat_four_drawers = (
                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                              profundidade_modulo - 50, espessura))
            lat_four_smaller_drawers = (
                '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                              profundidade_modulo - 50, espessura))
            back_four_drawers = (
                '4x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                      espessura_fundo))
            print(lat_four_drawers)
            print(lat_four_smaller_drawers)
            print(back_four_drawers)
            arquivo.write(lat_four_drawers + lat_four_smaller_drawers + back_four_drawers)
        fren_vers = largura - 87
        front_back_four_smaller_drawers = (
            '6x {}*{}*{} (1+) frente/verso gav menor\n'.format(fren_vers, gaveta_menor - 35, espessura))
        front_back_four_drawers = (
            '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(fren_vers, gaveta_maior - 35, espessura))
        print(front_back_four_smaller_drawers)
        print(front_back_four_drawers)
        arquivo.write(front_back_four_smaller_drawers + front_back_four_drawers)


if tipo == '8':

        quantidade_gavetas = int(input('Quantas gavetas? '))
        altura = int(input('Qual é a altura? '))
        largura = int(input('Qual é a largura? '))
        subtracao_largura = largura - 30
        largura_aux = largura - 10
        espessura = 15
        espessura_fundo = 6
        profundidade_modulo = int(input('Qual é a profundidade? '))
        arquivo = open(
            r"C:\Users\Positivo i5\Desktop\PLANOS DE CORTE\Plano de corte " + nome_cliente + '.txt', "a")

        lateral = '2x {}*{}*{} (1+/1-) lateral\n'.format(altura, profundidade_modulo, espessura)
        print(lateral)
        arquivo.write(lateral)

        with_batente = '1x {}*{}*{} (1+) base\n'.format(subtracao_largura, profundidade_modulo, espessura)
        print(with_batente)
        with_batente_2 = '1x {}*{}*{} (2+) batente\n'.format(subtracao_largura, 60, espessura)
        print(with_batente_2)
        arquivo.write(with_batente + with_batente_2)

        if quantidade_gavetas == 1:
            sub_altura = altura - 10 - 80
            fundo_gav = largura - 57
            gaveta = sub_altura - 35

            one_drawer = ('1x {}*{}*{} (4L) frente gav\n'.format(gaveta, largura_aux, espessura))
            arquivo.write(one_drawer)

            if profundidade_modulo >= 470:
                lat_one_drawer = ('2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, '420', espessura))
                back_one_drawer = ('1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                print(lat_one_drawer)
                print(back_one_drawer)
                arquivo.write(lat_one_drawer)
                arquivo.write(back_one_drawer)
            else:
                lat_one_drawer = (
                    '2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, profundidade_modulo - 50,
                                                            espessura))
                back_one_drawer = (
                    '1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                          espessura_fundo))
                print(lat_one_drawer)
                print(back_one_drawer)
                arquivo.write(lat_one_drawer + back_one_drawer)
            fren_vers = largura - 87
            front_back_one_drawer = (
                '2x {}*{}*{} (1+) frente/verso gav\n'.format(gaveta - 35, fren_vers, espessura))
            print(front_back_one_drawer)
            arquivo.write(front_back_one_drawer)

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
                front_gav_2 = (
                    "1x {}*{}*{} (4L) frente gav menor\n".format(gaveta_menor, largura_aux, espessura))
                front_gav_bigger_2 = (
                    "1x {}*{}*{} (4L) frente gav maior\n".format(gaveta_maior, largura_aux, espessura))
                print(front_gav_2)
                print(front_gav_bigger_2)
                arquivo.write(front_gav_2 + front_gav_bigger_2)

            if total == sub_altura:
                front_gav2 = ('2x {}*{}*{} frente gav\n '.format(gaveta_aux - 35, largura_aux, espessura, ))
                print(front_gav_2)
                arquivo.write(front_gav2)
            if profundidade_modulo >= 470:
                lat_two_drawers = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                lat_smaller_two_drawers = (
                    '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                back_two_drawers = (
                    '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                print(lat_two_drawers)
                print(lat_smaller_two_drawers)
                print(back_two_drawers)
                arquivo.write(lat_two_drawers + lat_smaller_two_drawers + back_two_drawers)
            else:
                lat_two_drawers = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                  profundidade_modulo - 50, espessura))
                lat_smaller_two_drawers = (
                    '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                  profundidade_modulo - 50, espessura))
                back_two_drawers = (
                    '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                          espessura_fundo))
                print(lat_two_drawers)
                print(lat_smaller_two_drawers)
                print(back_two_drawers)
                arquivo.write(lat_two_drawers + lat_smaller_two_drawers + back_two_drawers)

            front_back_two_drawer = (
                '2x {}*{}*{} (1+) frente/verso gav menor\n'.format(gaveta_menor - 35, fren_vers, espessura))
            front_back_smaller_two_drawer = (
                '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(gaveta_maior - 35, fren_vers, espessura))
            print(front_back_two_drawer)
            print(front_back_smaller_two_drawer)
            arquivo.write(front_back_two_drawer + front_back_smaller_two_drawer)

        if quantidade_gavetas == 3:
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
            front_gav_smaller_3 = (
                '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
            front_gav_3 = (
                '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, largura_aux, espessura))
            print(front_gav_smaller_3)
            print(front_gav_3)
            arquivo.write(front_gav_smaller_3 + front_gav_3)
            if profundidade_modulo >= 470:
                lat_three_drawers = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                lat_smaller_three_drawers = (
                    '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                back_three_drawers = (
                    '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                print(lat_three_drawers)
                print(lat_smaller_three_drawers)
                print(back_three_drawers)
                arquivo.write(lat_three_drawers + lat_smaller_three_drawers + back_three_drawers)
            else:
                lat_three_drawers = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                  profundidade_modulo - 50, espessura))
                lat_smaller_three_drawers = (
                    '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                  profundidade_modulo - 50, espessura))
                back_three_drawers = (
                    '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                          espessura_fundo))
                print(lat_three_drawers)
                print(lat_smaller_three_drawers)
                print(back_three_drawers)
                arquivo.write(lat_three_drawers + lat_smaller_three_drawers + back_three_drawers)
            fren_vers = largura - 87
            front_back_smaller_three_drawers = (
                '4x {}*{}*{} (1+) frente/verso gav menor\n'.format(fren_vers, gaveta_menor - 35, espessura))
            front_back_three_drawers = (
                '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(fren_vers, gaveta_maior - 35, espessura))
            print(front_back_smaller_three_drawers)
            print(front_back_three_drawers)
            arquivo.write(front_back_smaller_three_drawers + front_back_three_drawers)

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
            front_gav_smaller_four = (
                '3x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
            front_gav_four = (
                '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, largura_aux, espessura))
            print(front_gav_smaller_four)
            print(front_gav_four)
            arquivo.write(front_gav_smaller_four + front_gav_four)
            if profundidade_modulo >= 470:
                lat_four_drawers = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
                lat_four_smaller_drawers = (
                    '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
                back_four_drawers = (
                    '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
                print(lat_four_drawers)
                print(lat_four_smaller_drawers)
                print(back_four_drawers)
                arquivo.write(lat_four_drawers + lat_four_smaller_drawers + back_four_drawers)
            else:
                lat_four_drawers = (
                    '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                                  profundidade_modulo - 50, espessura))
                lat_four_smaller_drawers = (
                    '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                                  profundidade_modulo - 50, espessura))
                back_four_drawers = (
                    '4x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                          espessura_fundo))
                print(lat_four_drawers)
                print(lat_four_smaller_drawers)
                print(back_four_drawers)
                arquivo.write(lat_four_drawers + lat_four_smaller_drawers + back_four_drawers)
            fren_vers = largura - 87
            front_back_four_smaller_drawers = (
                '6x {}*{}*{} (1+) frente/verso gav menor\n'.format(fren_vers, gaveta_menor - 35, espessura))
            front_back_four_drawers = (
                '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(fren_vers, gaveta_maior - 35, espessura))
            print(front_back_four_smaller_drawers)
            print(front_back_four_drawers)
            arquivo.write(front_back_four_smaller_drawers + front_back_four_drawers)

if tipo == '9':
    quantidade_gavetas = int(input('Quantas gavetas? '))
    altura = int(input('Qual é a altura? '))
    largura = int(input('Qual é a largura? '))
    subtracao_largura = largura - 30
    largura_aux = largura - 10
    espessura = 15
    espessura_fundo = 6
    profundidade_modulo = int(input('Qual é a profundidade? '))

    if quantidade_gavetas == 1:
        sub_altura = altura - 10 - 80
        fundo_gav = largura - 57
        gaveta = sub_altura

        one_drawer = ('1x {}*{}*{} (4L) frente gav\n'.format(gaveta, largura_aux, espessura))
        arquivo.write(one_drawer)

        if profundidade_modulo >= 470:
            lat_one_drawer = ('2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, '420', espessura))
            back_one_drawer = ('1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
            print(lat_one_drawer)
            print(back_one_drawer)
            arquivo.write(lat_one_drawer)
            arquivo.write(back_one_drawer)
        else:
            lat_one_drawer = (
                '2x {}*{}*{} (1+) lateral gav\n'.format(gaveta - 35, profundidade_modulo - 50,
                                                        espessura))
            back_one_drawer = (
                '1x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                      espessura_fundo))
            print(lat_one_drawer)
            print(back_one_drawer)
            arquivo.write(lat_one_drawer + back_one_drawer)
        fren_vers = largura - 87
        front_back_one_drawer = (
            '2x {}*{}*{} (1+) frente/verso gav\n'.format(gaveta - 35, fren_vers, espessura))
        print(front_back_one_drawer)
        arquivo.write(front_back_one_drawer)

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
            front_gav_2 = (
                "1x {}*{}*{} (4L) frente gav menor\n".format(gaveta_menor, largura_aux, espessura))
            front_gav_bigger_2 = (
                "1x {}*{}*{} (4L) frente gav maior\n".format(gaveta_maior, largura_aux, espessura))
            print(front_gav_2)
            print(front_gav_bigger_2)
            arquivo.write(front_gav_2 + front_gav_bigger_2)

        if total == sub_altura:
            front_gav2 = ('2x {}*{}*{} frente gav\n '.format(gaveta_aux - 35, largura_aux, espessura, ))
            print(front_gav_2)
            arquivo.write(front_gav2)
        if profundidade_modulo >= 470:
            lat_two_drawers = (
                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
            lat_smaller_two_drawers = (
                '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
            back_two_drawers = (
                '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
            print(lat_two_drawers)
            print(lat_smaller_two_drawers)
            print(back_two_drawers)
            arquivo.write(lat_two_drawers + lat_smaller_two_drawers + back_two_drawers)
        else:
            lat_two_drawers = (
                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                              profundidade_modulo - 50, espessura))
            lat_smaller_two_drawers = (
                '2x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                              profundidade_modulo - 50, espessura))
            back_two_drawers = (
                '2x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                      espessura_fundo))
            print(lat_two_drawers)
            print(lat_smaller_two_drawers)
            print(back_two_drawers)
            arquivo.write(lat_two_drawers + lat_smaller_two_drawers + back_two_drawers)

        front_back_two_drawer = (
            '2x {}*{}*{} (1+) frente/verso gav menor\n'.format(gaveta_menor - 35, fren_vers, espessura))
        front_back_smaller_two_drawer = (
            '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(gaveta_maior - 35, fren_vers, espessura))
        print(front_back_two_drawer)
        print(front_back_smaller_two_drawer)
        arquivo.write(front_back_two_drawer + front_back_smaller_two_drawer)

    if quantidade_gavetas == 3:
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
        front_gav_smaller_3 = (
            '2x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
        front_gav_3 = (
            '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, largura_aux, espessura))
        print(front_gav_smaller_3)
        print(front_gav_3)
        arquivo.write(front_gav_smaller_3 + front_gav_3)
        if profundidade_modulo >= 470:
            lat_three_drawers = (
                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
            lat_smaller_three_drawers = (
                '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
            back_three_drawers = (
                '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
            print(lat_three_drawers)
            print(lat_smaller_three_drawers)
            print(back_three_drawers)
            arquivo.write(lat_three_drawers + lat_smaller_three_drawers + back_three_drawers)
        else:
            lat_three_drawers = (
                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                              profundidade_modulo - 50, espessura))
            lat_smaller_three_drawers = (
                '4x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                              profundidade_modulo - 50, espessura))
            back_three_drawers = (
                '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                      espessura_fundo))
            print(lat_three_drawers)
            print(lat_smaller_three_drawers)
            print(back_three_drawers)
            arquivo.write(lat_three_drawers + lat_smaller_three_drawers + back_three_drawers)
        fren_vers = largura - 87
        front_back_smaller_three_drawers = (
            '4x {}*{}*{} (1+) frente/verso gav menor\n'.format(fren_vers, gaveta_menor - 35, espessura))
        front_back_three_drawers = (
            '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(fren_vers, gaveta_maior - 35, espessura))
        print(front_back_smaller_three_drawers)
        print(front_back_three_drawers)
        arquivo.write(front_back_smaller_three_drawers + front_back_three_drawers)

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
        front_gav_smaller_four = (
            '3x {}*{}*{} (4L) frente gav menor\n'.format(gaveta_menor, largura_aux, espessura))
        front_gav_four = (
            '1x {}*{}*{} (4L) frente gav maior\n'.format(gaveta_maior, largura_aux, espessura))
        print(front_gav_smaller_four)
        print(front_gav_four)
        arquivo.write(front_gav_smaller_four + front_gav_four)
        if profundidade_modulo >= 470:
            lat_four_drawers = (
                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35, '420', espessura))
            lat_four_smaller_drawers = (
                '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35, '420', espessura))
            back_four_drawers = (
                '3x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, '420', espessura_fundo))
            print(lat_four_drawers)
            print(lat_four_smaller_drawers)
            print(back_four_drawers)
            arquivo.write(lat_four_drawers + lat_four_smaller_drawers + back_four_drawers)
        else:
            lat_four_drawers = (
                '2x {}*{}*{} (1+) lateral gav maior\n'.format(gaveta_maior - 35,
                                                              profundidade_modulo - 50, espessura))
            lat_four_smaller_drawers = (
                '6x {}*{}*{} (1+) lateral gav menor\n'.format(gaveta_menor - 35,
                                                              profundidade_modulo - 50, espessura))
            back_four_drawers = (
                '4x {}*{}*{} (2+) fundo gav\n'.format(fundo_gav, profundidade_modulo - 50,
                                                      espessura_fundo))
            print(lat_four_drawers)
            print(lat_four_smaller_drawers)
            print(back_four_drawers)
            arquivo.write(lat_four_drawers + lat_four_smaller_drawers + back_four_drawers)
        fren_vers = largura - 87
        front_back_four_smaller_drawers = (
            '6x {}*{}*{} (1+) frente/verso gav menor\n'.format(fren_vers, gaveta_menor - 35, espessura))
        front_back_four_drawers = (
            '2x {}*{}*{} (1+) frente/verso gav maior\n'.format(fren_vers, gaveta_maior - 35, espessura))
        print(front_back_four_smaller_drawers)
        print(front_back_four_drawers)
        arquivo.write(front_back_four_smaller_drawers + front_back_four_drawers)


