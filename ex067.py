while True:
    print('==' * 16)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('==' * 16)
    if num < 0:
        break
    for c in range(1, 11):
        tabuada = num * c
        print(f'{num} X {c} = {tabuada}')
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')