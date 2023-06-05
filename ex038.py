print('=-='*8)
print(' ANALISADOR DE NÚMEROS')
print('=-='*8)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O \033[32mprimeiro número\033[m é maior!')
elif n2 > n1:
    print('O \033[32msegundo número\033[m é maior!')
else:
    print('\033[32mNão existe\033[m valor maior, os dois são iguais!')

