num = int(input('Digite um número: '))
for c in range(1, 11):
    multi = num * c
    print('{} X {:2} = {}'.format(num, c, multi))