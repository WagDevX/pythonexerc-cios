num = int(input('\033[35mDigite  um número qualquer: '))
resto = num % 2
if resto == 0:
    print('\033[mO número {} é \033[35mPAR!'.format(num))
else:
    print('\033[mO número {} é \033[35mÍMPAR!'.format(num))

