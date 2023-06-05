import sys
num = int(input('Escolha um número qualquer: '))
print('-'*20)
print('[1]Para binário')
print('[2]Para octal')
print('[3]Para hexadecimal')
print('[x]Para sair')
conv = input('Escolha a opção para converter: ')
bin = format(num, "b")
oct = format(num, "o")
hexa = format(num, "x")
if conv == 'x' or conv == 'X':
    sys.exit()
elif conv == '1':
    print('O número {} em binário é {}'.format(num, bin))
# ou print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num[2:]))
elif conv == '2':
    print('O número {} em octal é {}'.format(num, oct))
elif conv == '3':
    print('O número {} em hexadecimal é {}'.format(num, hexa))
else:
    print('Opção inválida!')

