from random import randint
lista = ()
print('Os valores sorteados foram: ',end='')
for c in range(0, 4):
    sorteio = randint(0, 10)
    lista += (sorteio, )
    print(sorteio, end = ' ')
print(f'\nO maior valor sorteado foi {max(lista)}')
print(f'O menor valor sorteado foi {min(lista)}')
