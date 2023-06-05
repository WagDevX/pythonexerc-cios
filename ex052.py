print('-----NÚMERO PRIMO----')
num = int(input('Digite aqui o número: '))
if num > 1:
    for c in range(2, num):
        if (num % c) == 0:
            print(num, 'não é primo pois é divisível por mais de 2 números.')
            break
    else:
        print(num, 'é primo pois só é divisível por 1 e por ele mesmo.')
else:
    print(num, 'não é primo.')
