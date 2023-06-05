from random import randint
from time import sleep
print('\33[33:107m|-|\33[m'*12)
print(f"{'GERADOR MEGA-SENA':^35}")
print('\33[33:107m|-|\33[m'*12)
sorteios = list()
sorteio = list()
qtdsorteio = int(input('Quantas vezes gostaria de sortear?: '))
print(f'{f"SORTEANDO {qtdsorteio} JOGOS":^35}')
print('\33[33:107m|-|\33[m'*12)
for q in range(0, qtdsorteio):
    cont = 0
    while True:
        sort = randint(1, 60)
        if sort not in sorteio:
            sorteio.append(sort)
            cont += 1
        if cont >= 6:
            break
    sorteios.append(sorteio[:])
    sorteio.clear()
for n, s in enumerate(sorteios):
    print(f'Jogo {n+1}: {sorteios[n]}')
    print('\33[33:107m*\33[m'*36)
    sleep(0.5)






