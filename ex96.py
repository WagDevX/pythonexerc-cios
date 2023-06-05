def area(l, c):
    print(f'A área do terreno {l}x{c} é de {l*c}m²')

print('  Controle de terrenos  ')
print(25 * '=')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)

