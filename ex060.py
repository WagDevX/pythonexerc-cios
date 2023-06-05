from time import sleep
num2 = int(input('Digite um número qualquer: '))
print('Calculando {}! = '.format(num2), end='')
sleep(2)
num = num2
f = 1
while num > 0:
    print('{}'.format(num), end='')
    print(' x ' if num > 1 else ' = ', end='')
    f *= num
    num -= 1
print(f)

