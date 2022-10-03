ano = float(input('Qual o ano de nascimento: '))
idade = 2022 - ano
if idade > 20:
    print('MASTER')
elif idade == 20:
    print('SENIOR')
elif idade == 14 or idade > 9:
    print('INFANTIL')
else:
    idade <= 9 
    print('MIRIM')