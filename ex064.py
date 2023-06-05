num = 0
count = -1
soma = 0
while num != 999:
    count += 1
    soma += num
    num = int(input('Digite um número [999 para sair]: '))
print('Foram digitados',count,'números e a soma deles é {}.'.format(soma))