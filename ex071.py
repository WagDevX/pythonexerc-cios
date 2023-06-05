print('==' * 15)
print('         BANCO CEV')
print('==' * 15)
valor = int(input('Que valor você quer sacar? R$'))
cont2 = cont3 = cont4 = cont5 = cont50 = cont20 = cont10 = cont1 = 0
sob50 = valor % 50
sob20 = sob50 % 20
sob10 = sob20 % 10
while cont50 < valor:
    cont50 += 50
    if cont50 <= valor:
        cont2 += 1
while cont20 < sob50:
    cont20 += 20
    if cont20 <= sob50:
        cont3 += 1
while cont10 < sob20:
    cont10 += 10
    if cont10 <= sob20:
        cont4 += 1
while cont1 < sob10:
    cont1 += 1
if cont2 > 0:
    print(f'Total de {cont2} cédulas de R$50')
if cont3 > 0:
    print(f'Total de {cont3} cédulas de R$20')
if cont4 > 0:
    print(f'Total de {cont4} cédulas de R$10')
if cont1 > 0:
    print(f'Total de {cont1} cédulas de R$1')
print('==' * 15)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')