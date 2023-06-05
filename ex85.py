listanum = [[], []]
for n in range(0, 7):
    valor = int(input(f'Digite o {n+1}º valor: '))
    if valor % 2 == 0:
        listanum[0].append(valor)
    else:
        listanum[1].append(valor)
print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(listanum[0])}')
print(f'Os valores ímpares digitados foram: {sorted(listanum[1])}')