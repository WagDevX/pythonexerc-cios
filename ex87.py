lista = [[], [], []]
somapares = maiorvalor = 0
for c in range(0, 3):
    lista[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0, 3):
    lista[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0, 3):
    lista[2].append(int(input(f'Digite um valor para [2, {c}]: ')))
print('-=' * 30)
for p in lista:
    print(f'[ {p[0]:^3} ][ {p[1]:^3} ][ {p[2]:^3} ]')
print('-=' * 30)
for e, p in enumerate(lista):
    for p in p:
        if p % 2 == 0:
            somapares += p
print(f'A soma dos valores pares é {somapares}.')
print(f'A soma dos valores da terceira coluna é {lista[0][2] + lista [1][2] + lista[2][2]}.')
print(f'O maior valor da segunda linha é {max(lista[1])}.')
