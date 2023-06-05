termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = 1
while contador <= 10:
    contador += 1
    termo = termo + razao
    print(termo - razao, end=' → ')
print('Acabou!')