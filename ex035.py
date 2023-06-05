print('\033[32m-=\033[m'*20)
print('\033[31mAnalisador de Triângulos\033[m')
print('\033[32m-=\033[m'*20)
a = int(input('Digite o comprimento da primeira reta: '))
b = int(input('Digite o comprimento da segunda reta: '))
c = int(input('Digite o comprimento da terceira reta: '))
#c1 = b + c
#c2 = a + c
#c3 = a + b
if a < b + c and b < a + c and c < a + b:
    print('É possível fazer um triângulo!')
else:
    print('Não é possível fazer um triângulo!')