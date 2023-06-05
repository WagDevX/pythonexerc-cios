from time import sleep
def manual():
    while True:
        print('\33[44m\33[30m~' * 30)
        print('SISTEMA DE AJUDA PyHELP')
        print('~' * 30)
        txt = input('\033[0mFunção ou Biblioteca > ')
        print('\33[42m\33[30m~' * 37)
        if 'FIM' in txt:
            break
        print(f"Acessando o manual do comando '{txt}'")
        print('~' * 37)
        sleep(0.5)
        print('\033[0m')
        print('\033[46m\33[30m')
        print(f'{help(txt)}')


manual()