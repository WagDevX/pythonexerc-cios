import math
import emoji
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(emoji.emojize("Olá, mundo {}!:earth_americas:".format(raiz),language='alias'))
