from time import sleep
def contador(i, f, p):
    print('-=' * 15)
    if p < 0:
        p = -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    if i > f:
        p = -abs(p)
        f -= 1
    if i < f:
        f +=1

    for k in range(i, f, p):
        print(k, end=' ')
        sleep(0.2)
    print('FIM!', end='')
contador(1, 10, 1)
print()
contador(10, 0, -2)
print()
print('-=' * 15)
print('Agora é sua vez de personalizar a contagem!')
p = int(input('Início: '))
s = int(input('Fim: '))
t = int(input('Passo: '))
contador(p, s, t)