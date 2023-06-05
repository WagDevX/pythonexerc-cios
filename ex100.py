from time import sleep
from random import randint

def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end=' ')
    for i in range(0, 6):
        n = randint(0, 10)
        lista.append(n)
        print(n, end=' ')
        sleep(0.5)
    print()


def somaPar(lista):
    somapares = 0
    for c in lista:
        if c % 2 == 0:
            somapares += c
    print(f'A soma dos valores pares na lista {lista} é de {somapares}')


numeros = list()
sorteio(numeros)
somaPar(numeros)

