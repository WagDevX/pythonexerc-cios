frase = str(input('Digite uma frase: ')).strip().upper()
frases = frase.split()
fraseju = ''.join(frases)
inverso = fraseju[::-1]
'''for c in range(len(fraseju) -1, -1, -1):
    inverso += fraseju[c]'''
print('O inverso de {} é {}'.format(fraseju, inverso))
if inverso == fraseju:
    print('É UM PALÍNDROMO')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO')

