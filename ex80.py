lista = []
valor = int(input('Digite um valor: '))
lista.append(valor)
print('Adicionado ao final da lista...')
for c in range(0, 4):
    valor = int(input('Digite um valor: '))
    menor = min(lista)
    maior = max(lista)
    if valor >= maior:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    if valor <= menor:
        lista.insert(0, valor)
        print('Adicionado na posição 0 da lista...')
    if valor < maior and valor > menor:
        lista.insert(1, valor)
        print('Adicionado na posição 1 da lista...')

print('=-'*30)
print(f'Os valores digitados foram {lista}')