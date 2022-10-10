numero = int(input('digite um numero: '))
resultado = numero % 2
if resultado == 0:
    print(f'O numero {numero} é \033[32mPAR\033[m')
else:
    print(f'O numero {numero} é \033[31mIMPAR\033[m')
