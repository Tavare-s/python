preco = float(input('Qual o preço das compras? R$ '))
print('=-' * 40)
print('DINHEIRO: [ 1 ]')
print('DEBITO:   [ 2 ]')
print('CREDITO:  [ 3 ]')
print('=-' * 40)
pag = input('Qual a forma de pagamento: ')
dinheiro = preco - (preco * 0.10) 
debito = preco - (preco * 0.05)
credito = preco
if pag == '3':
    n2 = int(input('Quantas vezes? '))
    if n2 <= 2 :
        print(f'Sua compra deu R$ {preco}')
    if n2 > 2 :
        juros = preco + (preco * 0.20)
        parc = juros / n2
        print(f'A sua compra deu R$ {preco} com pagamento em {n2}X vezes de R$ {parc} ficou em R$ {juros}')
elif pag == '1' :
    print(f'Sua compra de R$ {preco} com 10% de desconto ficou R$ {dinheiro}')
elif pag == '2' :
    print(f'Sua compra de R$ {preco} com 5% de desconto ficou R$ {debito} ')