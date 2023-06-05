print('--'*15)
print('      LOJA SUPER BARATÃO')
print('--'*15)
cont = 0
total = []
produtos = []
while True:
    produto = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))
    if preco > 1000:
        cont += 1
    produtos.append(produto)
    total.append(preco)
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar [S/N]').upper().strip()[0]
    if continuar == 'N':
        break
menor = total.index(min(total))
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${sum(total):.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O mais barato foi o produto com nome de {produtos[menor]} que custa R${total[menor]:.2f}')
