from time import sleep
print('-=' * 20)


def maior(* lst):
    cont = maior = 0
    print('Analisando os valores passados...')
    if sum(lst) != 0:
        for i in lst:
            print(f'{i}', end=' ')
            sleep(0.3)
    if sum(lst) != 0:
        print(f'Foram informados {len(lst)} valores ao todo.')
    else:
        print('Foram informados 0 valores ao todo.')
    if sum(lst) != 0:
        print(f'O maior valor informado foi {max(lst)}.')
    else:
        print(f'O maior valor informado foi 0.')
    print('-=' * 20)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()
