from time import sleep
from random import randint
escolhas = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogada = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*12)
print('Computador jogou {}'.format(escolhas[computador]))
print('Jogador jogou {}'.format(escolhas[jogada]))
print('-='*12)
if computador == jogada:
    print('EMPATE!')
elif computador == 0 and jogada == 1 or computador == 1 and jogada == 2 or computador == 2 and jogada == 0:
    print('JOGADOR VENCE')
else:
    print('COMPUTADOR VENCE')