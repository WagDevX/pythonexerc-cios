termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
progressao = (termo + (razao * 9))
while termo <= progressao:
    termo = termo + razao
    print(termo - razao, end=' → ')
    if termo == progressao:
        mais = int(input('Quantos termos mais?: '))
        if mais == 0:
            print('Até mais!')
            break
        else:
            progressao = (termo + (razao * mais))


