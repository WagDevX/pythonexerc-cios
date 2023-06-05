from datetime import date
ano = int(input('Qual ano quer analisar? Coloque 0 para analisar o ano atual: '))
bi = ano % 4
if ano == 0:
    ano = date.today().year
if bi == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
