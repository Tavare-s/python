'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
somaidade = 0
mediaidade = 0
maioridadehomen = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print(f'----- PESSOA {p} -----')
    nome = str(input(f'Nome : ')).strip()
    idade = int(input(f'Idade : '))
    sexo = str(input('M/F : ')).strip() .upper()
    somaidade += idade
    if p == 1 and sexo == 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print(f'a media de idade é {mediaidade}')
print(f'O homen mais velho tem {maioridadehomen} anos e se chama {nomevelho}')
print(f'ao todos sao {totmulher20} mulheres com menos de 20 anos')