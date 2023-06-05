num = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

for c in range(num, num+(razao * 10), razao):
    print(c, end=' → ')
print('Acabou')
