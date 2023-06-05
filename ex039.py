import sys
from datetime import date
print('\033[32m*-*\033[m'*8)
print(' SERVIÇO DE ALISTAMENTO')
print('\033[32m*-*\033[m'*8)
ano = int(input('Digite o ano do seu nascimento: '))
sexo = input('Qual o seu sexo? Digite M para masculino e F para feminino: ').upper()
anoele = date.today().year - ano
print('Você nasceu em {} e tem {} anos em {}.'.format(ano, anoele, date.today().year))
if sexo == 'F':
    print('Você não precisa se alistar, pois é uma mulher!')
    sys.exit()
elif anoele == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif anoele < 18:
    print('Ainda faltam {} ano(s) para você se alistar!'.format(18 - anoele))
    print('Seu alistamento será em {}.'.format(ano + (18 - anoele)))
elif anoele > 18:
    print('Você não pode mais se alistar! Já passou {} anos.'.format(anoele % 18))
    print('Você deveria ter se alistado em {}.'.format(ano + 18))



