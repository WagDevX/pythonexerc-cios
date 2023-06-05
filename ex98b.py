from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    cont = 1
    if i < f:
        while cont <= f:
            print(f'{cont}', end='')
            sleep(0.5)
            cont += p
    print('FIM')
    else:
        cont = i
        while cont >- f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
            print('FIM!')

# programa principal
contador(1, 10 , 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)

