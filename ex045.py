from random import choice
print('#-#'*5)
print(' JOKENPÔ GAME')
print('#-#'*5)
computador = ['Pedra', 'Papel', 'Tesoura']
jogada1 = choice(computador)
jogada2 = choice(computador)
jogada3 = choice(computador)
jogador1 = input('Pedra, papel ou tesoura? ').strip().lower()
jogador2 = input('Pedra, papel ou tesoura? ').strip().lower()
jogador3 = input('Pedra, papel ou tesoura? ').strip().lower()
if jogada1 == 'Pedra' and jogador1 == 'pedra' or jogada1 == 'Papel' and jogador1 == 'papel' or jogada1 == 'Tesoura' and jogador1 == 'tesoura':
    print('Computador escolheu {} e você {}. Empate!'.format(jogada1, jogador1))
elif jogada1 == 'Pedra' and jogador1 == 'tesoura' or jogada1 == 'Papel' and jogador1 == 'pedra' or jogada1 == 'Tesoura' and jogador1 == 'papel':
    print('Computador escolheu {} e você {}. Computador ganhou!'.format(jogada1, jogador1))
else:
    print('Computador escolheu {} e você {}. Você ganhou!'.format(jogada1, jogador1))
if jogada2 == 'Pedra' and jogador2 == 'pedra' or jogada2 == 'Papel' and jogador2 == 'papel' or jogada2 == 'Tesoura' and jogador2 == 'tesoura':
    print('Computador escolheu {} e você {}. Empate!'.format(jogada2, jogador2))
elif jogada2 == 'Pedra' and jogador2 == 'tesoura' or jogada2 == 'Papel' and jogador2 == 'pedra' or jogada2 == 'Tesoura' and jogador2 == 'papel':
    print('Computador escolheu {} e você {}. Computador ganhou!'.format(jogada2, jogador2))
else:
    print('Computador escolheu {} e você {}. Você ganhou!'.format(jogada2, jogador2))
if jogada3 == 'Pedra' and jogador3 == 'pedra' or jogada3 == 'Papel' and jogador3 == 'papel' or jogada3 == 'Tesoura' and jogador3 == 'tesoura':
    print('Computador escolheu {} e você {}. Empate'.format(jogada3, jogador3))
elif jogada3 == 'Pedra' and jogador3 == 'tesoura' or jogada3 == 'Papel' and jogador3 == 'pedra' or jogada3 == 'Tesoura' and jogador3 == 'papel':
    print('Computador escolheu {} e você {}. Computador ganhou!'.format(jogada3, jogador3))
else:
    print('Computador escolheu {} e você {}. Você ganhou!'.format(jogada3, jogador3))

