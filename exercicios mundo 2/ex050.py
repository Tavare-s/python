'''Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''
soma = 0
cont = 0
for c in range (1,7): #vai pedir 6 valores
    num = int(input(f'valor {c} : '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(f'a soma dos {cont} numeros é: {soma}')
