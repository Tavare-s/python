from random import randint
jog = int(input('''
pedra [ 0 ]
papel [ 1 ]
tesoura [ 2 ]
escolha: '''))
itens = ('pedra', 'papel', 'tesoura')
computador = randint (0,2)
print('=-'*15)
print(f'computador jogou {itens [computador]}')
print(f'jogador jogou {itens[jog]}')
print('=-'*15)
if computador == 0:   #computador jogou PEDRA
    if jog == 0:
        print('EMPATE')
    elif jog == 1:
        print('PERDEU')
    elif jog == 2:
        print('GANHOU')
    else:
        print('jogada invalida')
elif computador == 1: #computador jogou PAPEL
    if jog == 0:
        print('PERDEU')
    elif jog == 1:
        print('EMPATOU')
    elif jog == 2:
        print('GANHOU')
    else :
        print('jogada invalida')

elif computador == 2: #computador jogou TESOURA
    if jog == 0:
        print('GANHOU')
    elif jog == 1:
        print('PERDEU')
    elif jog == 2:
        print('EMPATOU2')
    else:
        print('jogada invalida')