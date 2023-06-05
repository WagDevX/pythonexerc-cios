print('>>SEQUÊNCIA DE FIBONACCI>>')
num = int(input('Digite a quantidade de sequências desejada: '))
n1, n2 = 0, 1
count = 0
while count < num:
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
    print(n1,'→ ', end='')
seq = int(input('Digite um número da sequência para saber sua posição: '))
print('FIM')

