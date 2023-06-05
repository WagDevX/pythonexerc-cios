dados = dict()
listadedados = list()
pessoas = somaidade = 0
while True:
    dados['Nome'] = str(input('Nome: '))
    while True:
        dados['Sexo'] = str(input('Sexo [M/F]: '))
        if dados['Sexo'] in 'MmFf':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')
    dados['Idade'] = int(input('Idade: '))
    pessoas += 1
    listadedados.append(dados.copy())
    while True:
        continuar = input('Quer continuar [S/N]')
        if continuar in 'NnSs':
            break
        else:
            print('ERRO! Por favor digite apenas S ou N')
    if continuar in 'Nn':
        break

print('-=' * 30)
print(f'A) O grupo tem {pessoas} pessoas.')
for c in listadedados:
    somaidade += c['Idade']
media = somaidade / pessoas
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for c in listadedados:
    if c['Sexo'] in 'Ff':
        print(c['Nome'], end=' ')
print()
print('D) Lista de pessoas que estão acima da média:')
for c in listadedados:
    if c['Idade'] > media:
        print('   ', end='')
        for k, v in c.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')

