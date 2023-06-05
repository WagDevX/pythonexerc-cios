'''import math
cato = float(input('Digite o cateto oposto: '))
cata = float(input('Digite o cateto adjacente: '))
hip = math.hypot(cato, cata)
print('A hipotenusa é {:.2f}'.format(hip))'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
