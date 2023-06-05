num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))
numeros = (num1, num2, num3, num4)
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não foi  digitado em nehuma posição')
for p in numeros:
    if p % 2 == 0:
        print('Os números pares digitados foram: ', end ='')
        break
else:
    print('Não foram digitados números pares.')
for p in numeros:
    if p % 2 == 0:
        print(p, end=' ')

