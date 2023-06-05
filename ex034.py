salario = float(input('Digite seu salário: '))
aumento1 = salario * 0.15
aumento2 = salario * 0.10
if salario <= 1250:
    print('Você terá um aumento de R${:.2f}!'.format(aumento1))
else:
    print('Você terá um aumento de R${:.2f}!'.format(aumento2))