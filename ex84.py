pessoas = list()
pessoa = list()
maiorp = menorp = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa[:])
    pessoa.clear()
    continuar = ' '
    while 'S'!= continuar != 'N':
        continuar  = input('Deseja continuar?[S/N]').strip().upper()[0]
    if continuar == 'N':
        break
for p, n in enumerate(pessoas):
    if p == 0:
        maiorp = n[1]
        menorp = n[1]
    if n[1] > maiorp:
        maiorp = n[1]
    elif n[1] < menorp:
        menorp = n[1]

print('=-' * 30)
print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maiorp:.1f}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == maiorp:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menorp:.1f}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == menorp:
        print(f'[{p[0]}]', end=' ')
