distancia = float(input('Qual a distância da viagem em Km?: '))
price = 0.5 * distancia
price2 = 0.45 * distancia
if distancia <= 200:
    print('O valor total é de R${:.2f}!'.format(price))
else:
    print('O valor toal é de R${:.2f}'.format(price2))
print('BOA VIAGEM!!!')

# preço = distancia * 0.50 if distancia <= 200 else distância * 0.45
