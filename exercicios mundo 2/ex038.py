n1 = float(input('digite um numero: '))
n2 = float(input('Digite outro numero: '))

if n1 > n2:
    print(f'O numero {n2:.0f} é o menor!')
elif n1 < n2:
    print(f'O numero {n2:.0f} é o maior')
else:
    n1 == n2
    print(f'Os dois valores {n1:.0f} e {n2:.0f} são iguais')