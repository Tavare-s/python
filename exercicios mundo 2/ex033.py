n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
n3 = float(input('Digite mais um  numero: '))
#verifica quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor é \033[41m{menor}\033[m')
print(f'O maior é \033[42m{maior}\033[m')
