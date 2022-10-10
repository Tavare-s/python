velocidade = float(input('Qual a velocidade do veiculo? '))
if velocidade > 80 :
    print('voce foi multado.')
    multa = (velocidade-80)*7
    print(f'voce deve pagar R${multa}')
else:
    print('tenha um bom dia ! dirija com cuidado.')