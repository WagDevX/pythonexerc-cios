lista = []
while True:
    numeros = int(input('Digite um número: '))
    lista.append(numeros)
    continuar = ''
    while 'N' != continuar != 'S':
        continuar = input('Quer continuar?[S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
    else:
        continue
print('=-'*30)
print(f'Foram digitados {len(lista)} números!')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 not in lista:
    print(f'O valor 5 não foi encontrado na lista')
else:
    print(f'O valor 5 está na lista!')