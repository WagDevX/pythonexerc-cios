z = 0
cont = 0
list = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto']
for c in range(0, 6):
    num = int(input('Digite o {} número: '.format(list[c])))
    if num % 2 == 0:
        cont += 1
        z += num
print('A soma dos {} números pares digitados é {}'.format(cont, z))
