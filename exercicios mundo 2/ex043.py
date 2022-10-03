alt = float(input('Qual é a sua altura? '))
kg = float(input('Qual é o seu peso? KG '))

imc = kg / (alt**2)

if imc > 40 :
    print('Obesidade mórbida.')
elif imc >= 30 and imc <= 40:
    print('Obesidade.')
elif imc >= 25 and imc <= 30:
    print('Sobrepeso.')
elif 18.5 <= imc <= 25: # outra forma de usar ELIF
    print('Peso ideal.')
else:
    imc < 18.5
    print('Abaixo do peso.')
print (f'Seu IMC é {imc:.1f}')