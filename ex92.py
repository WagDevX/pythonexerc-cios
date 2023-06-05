from datetime import date
aposentadoria = dict()
aposentadoria['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano da Nascimento: '))
aposentadoria['Idade'] = date.today().year - nascimento
aposentadoria['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if aposentadoria['CTPS'] != 0:
    aposentadoria['Contratação'] = int(input('Ano de contratação: '))
    aposentadoria['Salário'] = int(input('Salário: '))
    aposentadoria['Aposentadoria'] = (aposentadoria['Contratação'] + 35) - nascimento
print('-=' * 30)
for k, v in aposentadoria.items():
    print(f'{k}: {v}')