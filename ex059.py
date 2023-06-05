p = 0
maior = []
while p < 2:
    num = int(input('Digite um número: '))
    p += 1
    soma = num + num
    muti = num * num
    maior.append(num)
    if p == 2:
        menu = int(input('''[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Sair do programa
Escolha uma opção: '''))
        if menu == 3:
            print('O maior número é:', max(maior))
        if menu == 2:
            print('O resultado da multiplicação é:', muti)
        if menu == 1:
            print('O resultado da soma é:', soma)
        if menu == 4:
           p = 0
        if menu == 5:
            print('Até mais!')





