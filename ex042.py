import sys
print('\033[32m-=\033[m'*13)
print('\033[31m Analisador de Triângulos\033[m')
print('\033[32m-=\033[m'*13)

a = int(input('Digite o comprimento da primeira reta(centímetros): '))
b = int(input('Digite o comprimento da segunda reta(centímetros): '))
c = int(input('Digite o comprimento da terceira reta(centímetros): '))

if a < b + c and b < a + c and c < a + b:
    print('Triângulo formado! Segue tipo abaixo:')
    if a == b == c:
        print('Triângulo Equilátero!')
    elif a != b != c != a:
        print('Triângulo Escaleno!')
    else:
        print('Triângulo Isósceles!')
else:
    print('Não é possível formar um triângulo!')


