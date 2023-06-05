import math
ang = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('Seno é igual a {:.2f}, e o coseno é {:.2f} e o tangente é {:.2f}'.format(sen, cos, tan))