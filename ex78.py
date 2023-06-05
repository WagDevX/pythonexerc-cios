lista = []
for n in range(0, 5):
    lista.append(int(input(f'Digite um número para a posição {n}: ')))
print('=-'*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições', end=' ')
for p, v in enumerate(lista):
    if max(lista) == v:
        print(f'{p}...', end='')
print(f'\nO menor valor digitado foi {min(lista)} nas posições', end=' ')
for p, v in enumerate(lista):
    if min(lista) == v:
        print(f'{p}...', end='')
