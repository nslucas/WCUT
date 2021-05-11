'''Para fazermos o roupeiro padrão de 2 portas precisaremos de:

- 2 Laterais
- 2 base/superior
- Rodapé
- Divisória central
- Prateleiras maleiro
- Fundo 6mm
- Gavetas
- Montantes
- Vista
- Portas (podem ser ou não de correr)

Para o roupeiro de somente 1 porta:

- 2 Laterais
- 2 base/superior
- Rodapé
- Gaveteiro
- Prateleiras
- Porta
'''
import math

alt_roupeiro = int(input('Qual é a altura? '))
vista_roupeiro = int(input('Qual o tamanho da vista? '))
largura_roupeiro = int(input('Qual é a largura do roupeiro? '))
profundidade_roupeiro = int(input('Qual é a profundidade? '))
modulos = int(input('Quantos módulos o roupeiro tem?'))
espessura = 15
espessura_fundo = 6
largura_aux = largura_roupeiro - 30
largura_aux2 = largura_aux/2
conta_vista = alt_roupeiro - vista_roupeiro - 80
conta_divisoria_central = alt_roupeiro - vista_roupeiro - 15 - 15 - 80
conta_prateleira_aux = largura_aux - 15
conta_prateleira = math.floor(conta_prateleira_aux/2)
conta_prateleira2 = math.ceil(conta_prateleira_aux/2)
conta_fundo = math.floor(largura_aux / 2) + 15

#roupeiro comum de 2 portas e somente 1 divisória central#

print_vista_roupeiro = '1x {}*{}*{} vista roupeiro'.format(vista_roupeiro, largura_aux, espessura )
print(print_vista_roupeiro)
print_lateral_roupeiro = '2x {}*{}*{} (1+) lateral roupeiro'.format(alt_roupeiro, profundidade_roupeiro, espessura)
print(print_lateral_roupeiro)
print_larg_aux_roupeiro = '2x {}*{}*{} (1+) base/superior roupeiro'.format(largura_aux, profundidade_roupeiro, espessura)
print(print_larg_aux_roupeiro)
print_rodape_roupeiro = '1x {}*{}*{} (1+) rodapé roupeiro'.format(largura_aux, 80, espessura)
print(print_rodape_roupeiro)
print_divisoria_central = '1x {}*{}*{} (1+) divisória central roupeiro'.format(conta_divisoria_central, profundidade_roupeiro - 80, espessura)
print(print_divisoria_central)
print_prateleiras_maleiro = '2x {}*{}*{} (1+) prateleira maleiro lado esquerdo'.format(conta_prateleira, profundidade_roupeiro - 50, espessura)
print(print_prateleiras_maleiro)
print_prateleiras_maleiro2 = '2x {}*{}*{} (1+) prateleira maleiro lado direito'.format(conta_prateleira2, profundidade_roupeiro - 50, espessura)
print(print_prateleiras_maleiro2)
print_fundo_roupeiro = '1x {}*{}*{} (laminação??) fundo roupeiro'.format(conta_fundo, conta_vista, espessura_fundo)
print(print_fundo_roupeiro)
print_acabamento_roupeiro = '1x {}*{}*{} (1+) acabamento lateral roupeiro'.format(alt_roupeiro, 20, espessura)
print(print_acabamento_roupeiro)

#gaveteiro#
print_montante_roupeiro = '2x {}*{}*{} (2+) montante gaveteiro (FAZER 4 DE 30)'.format(644, 70, 15)
print(print_montante_roupeiro)
print_frente_gav = '4x {}*{}*{} (4L) frente gav'.format(136, conta_prateleira - 60 - 27, espessura )
print(print_frente_gav)
print_lateral_gav = '8x {}*{}*{} (1+/1-) lateral interna gav'.format(130, 420, espessura)
print(print_lateral_gav)
print_frente_verso_gav = '8x {}*{}*{} (1+) frente/verso gav'.format(130, conta_prateleira - 60 - 27 - 30, espessura)
print(print_frente_verso_gav)
print_fundo_gav = '4x {}*{}*{} (2-) fundo gav'.format(conta_prateleira - 60 - 27, 420, espessura_fundo)
print(print_fundo_gav)

if modulos == '3':
    conta_prateleira = math.ceil(conta_prateleira_aux / 2)
    print_vista_roupeiro = '1x {}*{}*{} vista roupeiro'.format(vista_roupeiro, largura_aux, espessura)
    print(print_vista_roupeiro)
    print_lateral_roupeiro = '2x {}*{}*{} (1+) lateral roupeiro'.format(alt_roupeiro, profundidade_roupeiro, espessura)
    print(print_lateral_roupeiro)
    print_larg_aux_roupeiro = '2x {}*{}*{} (1+) base/superior roupeiro'.format(largura_aux, profundidade_roupeiro, espessura)
    print(print_larg_aux_roupeiro)
    print_rodape_roupeiro = '1x {}*{}*{} rodapé roupeiro'.format(print_larg_aux_roupeiro, 80, espessura)
    print(print_rodape_roupeiro)
    print_divisoria_central = '1x {}*{}*{} (1+) divisória central roupeiro'.format(conta_divisoria_central, profundidade_roupeiro - 80, espessura)
    print(print_divisoria_central)
    print_prateleiras_maleiro = '2x {}*{}*{} (1+) prateleira maleiro'.format(conta_prateleira, profundidade_roupeiro - 50, espessura)
    print(print_prateleiras_maleiro)
    print_fundo_roupeiro = '1x {}*{}*{} (laminação??) fundo roupeiro'.format(alt_roupeiro, conta_vista, espessura_fundo)
    print(print_fundo_roupeiro)
    print_acabamento_roupeiro = '1x {}*{}*{} (1+) acabamento lateral roupeiro'.format(alt_roupeiro, 20, espessura)
    print(print_acabamento_roupeiro)
