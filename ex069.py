mulheres = 0
cont = 0
homens = 0
while True:
    print('=='*15)
    print('CADASTRE UMA PESSOA')
    print('==' * 15)
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        cont += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if sexo == 'M':
        homens += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar [S/N]').upper().strip()[0]
    if continuar == 'N':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {homens} homens cadastrados.')
print('E temos {} mulheres com menos de 20 anos.'.format(mulheres))













