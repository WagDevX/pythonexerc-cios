termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        contador += 1
        termo += razao
        print(termo - razao, end=' → ')
    print('Pausa!')
    mais = int(input('Quantos termos mais você quer mostrar? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
