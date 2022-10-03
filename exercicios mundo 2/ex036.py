preco = float(input('Qual o valor do imovel? R$ '))
sal = float(input('Qual é o seu salario? R$ '))
anos = float(input('Em quantos anos voce quer pagar o imovel? '))
print('=-'*40)
msg ='A PRESTAÇÃO NÃO PODERA EXCEDER 30% DO SEU SALARIO!!'
print(msg)
prestacao = anos *12
val = preco /prestacao
if sal *0.30 > val:
    print(f'Seu emprestimo tera {prestacao:.0f} parcelas')
    print(f'E a parcela sera de R$ {val:.2f}')
else:
    print('Emprestimo \033[41mnegado\033[m')
