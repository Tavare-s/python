nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2 )/2
if media >= 70:
    print('\033[42mAPROVADO\033[m')
    print(f'sua media foi {media}')
elif media < 50:
    print('\033[41mREPROVADO\033[m')
    print(f'sua media foi {media}')
else:
    media >= 50 and (nota1 + nota2) / 2 <6.9
    print('\033[43mRECUPERAÇÃO\033[m')
    print(f'sua media foi {media}')