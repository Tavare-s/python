'''Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. '''

num = int(input('Digite um numero: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        tot = tot + 1
        print('\033[34m', end='')
    else:
        print('\033[32m', end='')
    print(f' {c} ', end='')
print(f'\n\033[mo numero {num} foi divisivel {tot} vezes.') #\n\ quebra de linha
if tot == 2:
    print('primo')
else:
    print('nao é primo')