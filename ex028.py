from random import randint
computador = randint(0, 5) #faz computador pensar
print('-=-'*20)
print('vou pensar em um numero entre 0 e 5. tente adivinhar')

jogador = int(input('Em que numero eu pensei? '))#jogador tenta adivinhar
if jogador == computador:
    print('Voce ganhou.')
else:
    print(f'eu pensei em {computador} e nao em {jogador}') 
    print('-=-'*20)