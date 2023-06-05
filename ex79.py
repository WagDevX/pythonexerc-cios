lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    cont = lista.count(valor)
    if cont == 1:
        print('Valor adicionado com sucesso...')
    if cont > 1:
        lista.remove(valor)
        print('Valor duplicado! Não adicionado...')
    continuar = ''
    while 'S' != continuar != 'N':
        continuar = input('Quer continuar[S/N]? ').strip().upper()[0]
    if continuar == 'N':
        break
    else:
        continue
print('=-'*30)
print(f'Você adicionou os valores {sorted(lista)}')