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

alt_roupeiro = int(input('Qual é a altura? '))
vista_roupeiro = int(input('Qual o tamanho da vista? '))
largura_roupeiro = int(input('Qual é a largura do roupeiro? '))
profundidade_roupeiro = int(input('Qual é a profundidade? '))
espessura = 15
espessura_fundo = 6
conta_vista = alt_roupeiro - vista_roupeiro - 80
conta_divisoria_central = alt_roupeiro - vista_roupeiro - 15 - 15 - 80
prateleiras =

print_vista_roupeiro = '1x {}*{}*{} vista roupeiro'.format(vista_roupeiro, largura_roupeiro -30, espessura )
print(print_vista_roupeiro)
print_lateral_roupeiro = '2x {}*{}*{} (1+) lateral roupeiro'.format(alt_roupeiro, profundidade_roupeiro, espessura)
print(print_lateral_roupeiro)
print_larg_aux_roupeiro = '2x {}*{}*{} (1+) base/superior roupeiro'.format(largura_roupeiro - 30, profundidade_roupeiro, espessura)
print(print_larg_aux_roupeiro)
print_rodape_roupeiro = '1x {}*{}*{} rodapé roupeiro'.format(print_larg_aux_roupeiro, 80, espessura)
print(print_rodape_roupeiro)
print_divisoria_central = '1x {}*{}*{} divisória central roupeiro'.format(conta_divisoria_central, profundidade_roupeiro - 80, espessura)
print(print_divisoria_central)
print_fundo_roupeiro = '1x {}*{}*{} fundo roupeiro'.format(alt_roupeiro - conta_vista, espessura_fundo)
print(print_fundo_roupeiro)
print_acabamento_roupeiro = '1x {}*{}*{} acabamento lateral roupeiro'.format(alt_roupeiro, 20, espessura)
print(print_acabamento_roupeiro)