from time import sleep
from random import randint
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'{"O {} tirou {} no dado.":>25}'.format(k, v))
    sleep(0.5)
jogadas_ordenadas = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)
print('Ranking dos jogadores: ')
for v, i in enumerate(jogadas_ordenadas):
    print(f'{"{}º Lugar: {} com {}":>23}'.format(v+1, i[0], i[1]))
    sleep(0.5)
