di = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
td = di * 60 + 0.15 * km
print('O total a pagar é de R${:.2f}'.format(td))