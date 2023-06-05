alt = int(input('Qual é a altura da parede? '))
lar = int(input('Qual é a largura da parede? '))
rend = int(input('Qual o rendimento da tinta?(m2 por litro) '))
ar = alt * lar
tint = ar / rend
print('Você irá precisar de {:.2f} litros de tinta para pintar essa parede.'.format(tint))
