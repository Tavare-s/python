'''Exercício Python 54: Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nascimento = int(input(f'ano: '))
    idade = atual - nascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'{totmenor} pessoas menor de idade')
print(f'{totmaior} pessoas maior de idade')

