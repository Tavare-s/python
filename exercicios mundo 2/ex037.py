#tranformar decimal em binario octal ou hexadecimal
num  = int( input('digite um numero: '))
print('''Escolha uma das bases para a converção:
[ 1 ] BINARIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'O valor convertido para BINARIO é igual a {bin (num)[2:]}')
elif opcao == 2:
    print(f'O valor convertido para OCTAL é igual a {oct (num)[2:]}')
else:
    opcao == 3
    print(f'O valor convertido para HEXADECIMAL é igual a {hex (num)[2:]}')
