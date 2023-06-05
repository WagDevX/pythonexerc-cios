from random import randint
print('=-' * 15)
print('  VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
cont = 0
while True:
    computador = randint(1, 11)
    jogador = int(input('Digite um valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = input('Par ou ímpar? [P/I]').upper().strip()[0]
    soma = computador + jogador
    print('Você VENCEU!')
    print('Vamos jogar novamente...')
    print('=-' * 15)
    if soma % 2 == 1:
        resultado = 'I'
    else:
        resultado = 'P'
    if pi == 'I' and resultado == 'P':
        break
    elif pi == 'P' and resultado == 'I':
        break
    else:
        cont += 1
    if resultado == 'I':
        print('--' * 15)
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU ÌMPAR!')
        print('--' * 15)
    else:
        print('--' * 15)
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR!')
        print('--' * 15)
if resultado == 'I':
    print('--' * 15)
    print(f'Você jogou {jogador} e o computador {computador}. Total deu {soma} DEU ÌMPAR!')
    print('--' * 15)
else:
    print('--' * 15)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR!')
    print('--' * 15)
print('Você PERDEU!')
print('=-' * 15)
print(f'GAME OVER! Você venceu {cont} vezes!')

