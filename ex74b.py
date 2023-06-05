from random import randint
print('\33[33:107m|-|\33[m'*9)
print('     GERADOR MEGA-SENA')
print('\33[33:107m|-|\33[m'*9)
numsort = ()
for c in range(0, 6):
    sorteio = randint(0, 60)
    numsort += (sorteio, )
    print(f'{sorteio:<4}', end = ' ')
print('\n\33[33:107m|-||-||-||-||-||-||-||-||-|\33[m')
print('         BOA SORTE!')