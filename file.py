import keyboard
import os
from datetime import datetime

print('Bem-vindo Lucas, ótimo dia de trabalho para você :)')

def main():
    """
    essa funcao faz isssoso...
    """
    erro = False
    #tentativas = 0
    valor_maximo_permitido = 3
    while True:   
        ## trecho pra pegar largura
        for i in range(0, valor_maximo_permitido + 1):
            if i == valor_maximo_permitido:
                break  
            try:
                largura = int(input('Qual é a largura? ' ))
            except:
                print('Apenas valores inteiros são permitidos')  
                continue
            break
        if i == valor_maximo_permitido:
            print('errou largura muitas vezes.....saindo')
            erro = True
            break
            
        ## trecho pra pegar altura   
        for i in range(0, valor_maximo_permitido +  1):
            
            if i == valor_maximo_permitido:
                break
                
            try:
                altura=int(input('Qual é a altura? '))
            except:
                print('Apenas valores inteiros são permitidos')
                continue    
            break
        if i == valor_maximo_permitido:
            print('errou altura muitas vezes.....saindo')
            erro = True
            break
            
        for i in range(0, valor_maximo_permitido +  1):
            if i == valor_maximo_permitido:
                break   
            try:
                profundidade_modulo=int(input('Qual é a profundidade? '))
            except:
                print('Apenas valores inteiros são permitidos')
                continue    
            break
        if i == valor_maximo_permitido:
            print('errou profundidade muitas vezes.....saindo')
            erro = True
            break
            
        for i in range(0, valor_maximo_permitido +  1):
            if i == valor_maximo_permitido:
                break   
            try:
                numero_portas=int(input('Quantas portas? '))
            except:
                print('Apenas valores inteiros são permitidos')
                continue    
            break
        if i == valor_maximo_permitido:
            print('errou profundidade muitas vezes.....saindo')
            erro = True
            break
            
        for i in range(0, valor_maximo_permitido +  1):
            if i == valor_maximo_permitido:
                break   
            try:
                batente= str(input('O módulo possui batente?'))
            except:
                print('Apenas strings (sim/nao) são permitidos')
                continue    
            break
        if i == valor_maximo_permitido:
            print('errou batente muitas vezes.....saindo')
            erro = True
            break
            
        for i in range(0, valor_maximo_permitido +  1):
            if i == valor_maximo_permitido:
                break   
            try:
                prat_int=str(input('O módulo possui prateleira interna? '))
            except:
                print('Apenas strings (sim/nao) são permitidos')
                continue    
            break
        if i == valor_maximo_permitido:
            print('errou prat_int muitas vezes.....saindo')
            erro = True
            break    
            
        for i in range(0, valor_maximo_permitido +  1):
            if i == valor_maximo_permitido:
                break   
            try:
                porta=str(input('Porta com puxador? '))
            except:
                print('Apenas strings (sim/nao) são permitidos')
                continue    
            break
        if i == valor_maximo_permitido:
            print('errou porta muitas vezes.....saindo')
            erro = True
            break    
                    
        break
        
    if erro:
        return 'None', 'None', 'None', 'None', 'None', 'None', 'None'
    else:
        return largura, altura, profundidade_modulo,numero_portas, batente, prat_int, porta
        


def write_file(largura, altura, profundidade_modulo, numero_portas, batente, prat_int, porta):
    lista_write = []
    var_0 = f'2x {altura}*{profundidade_modulo}*{espessura} lateral'
    lista_write.append(var_0)
    if batente=='sim':
        var_1 = f'1x {subtracao_largura}*{profundidade_modulo}*{espessura} base'
        var_2 = f'1x {subtracao_largura}*{profundidade_bat}*{espessura} batente'
        lista_write.append(var_1)
        lista_write.append(var_2)

    else:
        var_1 = f'2x {subtracao_largura}*{profundidade_modulo}*{espessura} base/superior'
        lista_write.append(var_1)

    if prat_int=='sim':
        var_3 = f'1x {subtracao_largura}*{subtracao2}*{espessura} prat interna'
        lista_write.append(var_3)

    if porta =='sim':
        if numero_portas == 1:
           var_4 =  f'1x {porta_puxador}*{porta_largura}*{espessura} porta'
           lista_write.append(var_4)
        else:
           var_4  = f'2x {porta_puxador}*{porta_largura / 2},{espessura} porta'
           lista_write.append(var_4)

    else:
        if numero_portas == 1:
            var_4 =  f'1x {porta_sem_puxador}*{porta_largura}*{espessura} porta'
            lista_write.append(var_4)
        else:
            var_4  = f'2x {porta_sem_puxador}*{porta_largura / 2},{espessura} porta'
            lista_write.append(var_4)

    var_5 = f'1x {largura}*{altura}*{espessura_fundo} fundo'
    lista_write.append(var_5)
    return lista_write

def main_2():
    valor_maximo_permitido = 3
    erro = False
    #tentativas = 0
    for i in range(0, valor_maximo_permitido +  1):
            if i == valor_maximo_permitido:
                break   
            try:
                quantidade_gavetas=int(input('Quantas gavetas? '))
            except:
                print('Apenas inteiros são permitidos')
                continue    
            break

    if i == valor_maximo_permitido:
        print('errou qtd gavetas muitas vezes.....saindo')
        erro = True
           
            
    if erro:
        return 'None'
    else:
        return quantidade_gavetas


def write_file_2(altura, profundidade, espacamento, quantidade_gavetas):
    lista_write = []
    
    #pegando a altura da menor gaveta de acordo com a quantidade de gavetas:
    if quantidade_gavetas%2 == 0: #par
        altura_gaveta_menor = (altura - espacamento) / quantidade_gavetas
        #altura_gaveta_menor = int(str(altura_gaveta_menor).split('.')[0])
        altura_gaveta_maior = altura_gaveta_menor*2
        #altura_gaveta_maior = int(str(altura_gaveta_maior).split('.')[0]) + 1
        
    else: #impar
        altura_gaveta_menor = (altura - espacamento) / 4
        #altura_gaveta_menor = int(str(altura_gaveta_menor).split('.')[0])
        altura_gaveta_maior = altura_gaveta_menor*2
        #altura_gaveta_maior = int(str(altura_gaveta_maior).split('.')[0]) + 1
        
        
    if quantidade_gavetas%2 != 0: ##impar
        altura_gaveta_menor_inteiro = altura_gaveta_menor - altura_gaveta_menor%1
        
        if (altura_gaveta_menor%1 != 0): #se tiver sobra de tamanho
            excedente = (altura_gaveta_menor% 1) * quantidade_gavetas
            altura_gaveta_maior = altura_gaveta_menor_inteiro*2 + excedente
            #altura_gaveta_maior = int(str(altura_gaveta_maior).split('.')[0]) + 1

            if (altura_gaveta_maior% 1 != 0):  # se tiver sobra de tamanho
                #print('aqui_1')
                var_0 = f'{quantidade_gavetas - 1}x {altura_gaveta_menor_inteiro-35}  {largura2} {espessura} frente gav menor'
                altura_gaveta_maior_1 = int(str(altura_gaveta_maior).split('.')[0]) + 1
                var_1 = f'1x {altura_gaveta_maior_1-35} {largura2} {espessura} frente gav maior'
                lista_write.append(var_0)
                lista_write.append(var_1)
                #print(quantidade_gavetas - 1,'x', altura_gaveta_menor_inteiro-35, '', largura2, ' 15 frente gav menor' )
                #print('1x',altura_gaveta_maior-35, '', largura2, ' 15 frente gav maior')
        else:
            #print('aqui_2')
            var_2 = f'{quantidade_gavetas-1}x {altura_gaveta_menor_inteiro} {largura2} {espessura} frente gav menor'
            var_3 = f'1x {altura_gaveta_maior-35} {largura2} {espessura} frente gav maior'
            lista_write.append(var_2)
            lista_write.append(var_3)
            #print(quantidade_gavetas-1,'x', altura_gaveta_menor_inteiro, '', largura2, ' 15 frente gav menor')
            #print('1x',altura_gaveta_maior-35, '', largura2, ' 15 frente gav maior')

    elif quantidade_gavetas%2 == 0: #se a quantidade de gavetas for par
        altura_gaveta_menor_inteiro = altura_gaveta_menor - altura_gaveta_menor%1
        
        if (altura_gaveta_menor%1 != 0): #se tiver sobra de tamanho
            excedente = (altura_gaveta_menor % 1) * quantidade_gavetas
            altura_gaveta_maior = altura_gaveta_menor_inteiro + excedente
            altura_gaveta_maior = int(str(altura_gaveta_maior).split('.')[0]) + 1
            #print('aqui_3')
            var_4 = f'{quantidade_gavetas - 1}x {altura_gaveta_menor_inteiro}  {largura} {espessura} frente gav menor'
            var_5 = f'1x {altura_gaveta_maior-35} {largura} {espessura} frente gav maior'
            lista_write.append(var_4)
            lista_write.append(var_5)
            
            #print(quantidade_gavetas - 1,'x ',altura_gaveta_menor_inteiro,'', largura, ' 15 frente gav menor')
            #print('1x',altura_gaveta_maior-35, '', largura, ' 15 frente gav maior')
        else:
            #print('aqui_4')
            var_6 = f'{quantidade_gavetas-1}x {altura_gaveta_menor_inteiro} {largura} {espessura} frente gav menor'
            var_7 = f'1x {altura_gaveta_maior-35} {largura} {espessura} frente gav maior'
            lista_write.append(var_6)
            lista_write.append(var_7)
            #print(quantidade_gavetas - 1, 'x ',altura_gaveta_menor_inteiro, '', largura, ' 15 frente gav menor')
            #print('1x',altura_gaveta_maior-35, '', largura, ' 15 frente gav maior')

    if profundidade>=470:
        #print('aqui_5')
        var_7 = f'2x {altura_gaveta_menor-70} 420 {espessura} lateral gav menor'
        var_8 = f'3x {fundo} 420 {espessura} fundo gav'
        lista_write.append(var_7)
        lista_write.append(var_8)
        #print('2x',altura_gaveta_menor-70,'','420','',espessura,'lateral gav menor')
        #print('3x',fundo, '','420','',espessura, 'fundo gav')
    else:
        #print('aqui_6')
        altura_gaveta_menor_1 = int(str(altura_gaveta_menor).split('.')[0])
        var_9 = f'2x {altura_gaveta_menor_1-70} {profundidade-50}  {espessura} lateral gav menor'
        var_10 = f'3x {fundo} {profundidade} {espessura} fundo gav'
        lista_write.append(var_9)
        lista_write.append(var_10)
        #print('2x',altura_gaveta_menor-70,'',profundidade-50,'',espessura,'lateral gav menor')
        #print('3x',fundo, '',profundidade,'',espessura, 'fundo gav')

    fren_vers=largura-87
    #print('aqui_7')
    altura_gaveta_menor_1 = int(str(altura_gaveta_menor).split('.')[0])
    var_11 = f'4x {fren_vers} {altura_gaveta_menor_1-70} {espessura} frente/verso gav menor'
    var_12 = f'2x {fren_vers} {altura_gaveta_menor_1-70} {espessura} frente/verso gav maior'
    lista_write.append(var_11)
    lista_write.append(var_12)
    return lista_write
    #print('4x',fren_vers,'',altura_gaveta_menor-70,'',espessura,'frente/verso gav menor')
    #print('2x',fren_vers,'', altura_gaveta_maior-70,'',espessura,'frente/verso gav maior')   


def save_file(name_file, lista_write):
    f = open(name_file, "a")
    data = datetime.today().strftime('%d-%m-%Y')
    f.write(data + '\n')
    for _var in lista_write:
        f.write(_var + '\n')
    f.write('#################################################### \n')
    f.close()  



if __name__ == '__main__':
    largura, altura, profundidade_modulo, numero_portas, batente, prat_int, porta = main()
    espessura=15
    subtracao_largura=largura - 30
    profundidade_bat = 60
    subtracao2=profundidade_modulo-100
    porta_puxador=altura-45
    porta_sem_puxador=altura-10
    porta_largura=largura-10
    espessura_fundo = 6

    lista_write = write_file(largura, altura, profundidade_modulo, numero_portas, batente, prat_int, porta)
    save_file('primeiro.txt', lista_write)

    quantidade_gavetas = main_2()

    aux = largura
    largura2 = aux-10
    espacamento=(quantidade_gavetas+1)*5
    fundo=largura-57

    decisao = str(input('Deseja Continuar? '))
    if decisao == 'sim':
        lista_write = write_file_2(altura, profundidade_modulo, espacamento, quantidade_gavetas)
        save_file('primeiro.txt', lista_write)       









        
        


        

         
