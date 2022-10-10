'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
if frase [::-1] == frase :
    print(f'O contrario de {junto} é {junto[::-1]}. ')
    print('É um palindromo')
else:
    print(f'a frase {frase} nao é um palindromo, e ao contrario fica {junto[::-1]}.')