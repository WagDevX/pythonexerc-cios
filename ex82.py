lista = []
listapares = []
listaimpares = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    continuar = ' '
    while 'S' != continuar != 'N':
        continuar = input('Deseja continuar?[S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
    else:
        continue
for c in lista:
    if c % 2 == 0:
        listapares.append(c)
    else:
        listaimpares.append(c)
print('=-'*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listapares}')
print(f'A lista de ímpares é {listaimpares}')