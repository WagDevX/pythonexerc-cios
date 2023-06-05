import random
from time import sleep
print('Sou seu computador...')
print('Vou pensar em um número entre 0 e 10. Tente adivinhar!')
computador = random.randint(0, 10)
jogador = ''
contador = 0
while jogador != computador:
    jogador = int(input('Qual o seu palpite? '))
    contador += 1
    if 0 < jogador > 10:
        print('\033[31mNúmero inválido! Escolha de 0 a 10!\033[m')
    if jogador < computador:
        print('Mais... Tente novamente!')
    if jogador > computador:
        print('Menos... Tente novamente!')
if jogador == computador and contador == 1:
    print('\033[32mParabéns, você acertou de primeira!!!')
    print('O computador pensou {} e você digitou {}!'.format(computador, jogador))
elif jogador == computador and contador > 1:
    print('''\033[32mParabéns! Você tentou {} vezes e ganhou!
O computador pensou {} e você digitou {}. '''.format(contador, computador, jogador))
