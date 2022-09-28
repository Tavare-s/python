'''Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''
distancia = float(input('Qual a distancia da sua viagem? '))

'''if viagem <= 200:
    preco1 = viagem * 0.50
    print(f'A sua viagem vai custar: \033[42mR$ {preco1:.2f}\033[m')
else:
    preco2 = viagem *0.45
    print(f'A sua viagem vau custar: \033[42mR$ R$ {preco2:.2f}\033[m')'''
preco = distancia *0.50 if distancia <=200 else distancia * 0.45
print(f'o preco da sua passagem sera {preco}')