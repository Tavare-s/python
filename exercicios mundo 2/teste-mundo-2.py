# i = int(input('inicio: '))
# f = int(input('fim: '))
# p = int(input('passo: '))
# for c in range (i, f, p):
#     print(c)
# print('FIM')

# for c in range (0,10): #vai pedir 10 valores
#     n = int(input('valor: '))
# print('fim')

# s = 0
# for c in range(0,5):
#     n = int(input('Digite um valor: '))
#     s = s + n #ou s += n
# print(f'a soma deu {s}')
'''while '''
n = 1 
par = impar = 0
while n != 0:
    n = int(input('digite um valor: '))
    if n != 0:
        if n % 2 == 0 :
            par = par + 1
        else:
            impar = impar + 1
print(f'Voce digitou {par} numeros pares e {impar} numeros impares')