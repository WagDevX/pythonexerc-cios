print('Calculando média e valores maiores e menores')
parar = 0
count = 0
list = []
soma = 0
while parar != 'N':
    exe = int(input('Digite um número: '))
    parar = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    count += 1
    soma += exe
    list.append(exe)
print('Você digitou {} números e a média foi {:.2f}'.format(count, soma / count))
print('O maior valor foi', max(list))
print('O menor valor foi', min(list))


