ano = int(input('Ano de nascimento: '))
idade = 2022 - ano
falta = 18 - idade
falta2 = idade - 18  
alistamento = 2022 - falta 
deveria = 2022 - falta2
print(f'Quem nasceu em {ano} tem {idade} anos 2022.')
if idade == 18:
    print('Voce deve se alistar IMEDIATAMENTE.')
elif idade > 18:
    print(f'Voce ja deveria ter se alistado há {falta2} anos.')
    print(f'seu alistamento foi em {deveria}')
else:
    idade < 18
    print(f'ainda falta {falta} anos para voce se alistar.')
    print(f'seu alistamento sera em: {alistamento}')
