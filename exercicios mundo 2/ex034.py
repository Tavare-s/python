'''Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''
sal = float(input('Qual é seu salario? '))
if sal > 1250:
    aumento = (sal * 0.10) + sal
    print(f'O seu salario era {sal}. seu salario com aumento é R$ {aumento}')
else:
    sal <= 1250
    aumento2 = (sal * 0.15) + sal
    print(f'O seu salario era R$ {sal} seu salario com aumento é R$ {aumento2}')