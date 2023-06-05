import random
from time import sleep
num = random.randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
dig = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if dig == num:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(num, dig))
print('---FIM---')
