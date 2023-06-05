z = 0
cont = 0
for c in range(0, 501, 3):
    if c % 2 == 1:
        cont = cont + 1
        z += c
print('A soma de todos os {} números é de {}.'.format(cont, z))
