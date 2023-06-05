from datetime import date
print('~-'*17)
print(' CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('~-'*17)
categoria = int(input('Digite seu ano de nascimento para saber sua categoria: '))
idade = date.today().year - categoria
print('Você tem {} anos.'.format(idade))
if idade <= 9:
    print('Você está na categoria: MIRIM!')
elif 9 < idade <= 14:
    print('Você está na categoria: INFANTIL!')
elif 14 < idade <= 19:
    print('Você está na categoria: JUNIOR!')
elif 25 >= idade >= 20:
    print('Você está na categoria: SENIOR!')
elif idade > 25:
    print('Você está na categoria: MASTER!')
else:
    print('Idade inválida!')

