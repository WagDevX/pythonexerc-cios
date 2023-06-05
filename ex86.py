lista = [[], [], []]
for c in range(0, 3):
    lista[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0, 3):
    lista[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0, 3):
    lista[2].append(int(input(f'Digite um valor para [2, {c}]: ')))
print('-=' * 30)
for p in lista:
    print(f'[ {p[0]:^5} ][ {p[1]:^5} ][ {p[2]:^5} ]')

