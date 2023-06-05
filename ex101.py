from datetime import datetime


def voto(n):
    global idade
    idade = datetime.today().year - n
    if 16 < idade < 18:
        n = 'OPCIONAL'
    elif  64 >= idade >= 18:
        n = 'OBRIGATÓRIO'
    elif idade >= 65:
        n = 'OPCIONAL'
    else:
        n = 'NEGADO'
    return n


print('=' * 28)
ano = int(input('Em que ano você nasceu? '))
voto(ano)
print(f'Com {idade} anos: VOTO {voto(ano)}')

