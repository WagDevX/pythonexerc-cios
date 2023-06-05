def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('\n\033[0:31mO usuário optou por não digitar o número.\033[m')
            return 0
        except:
            print('\n\033[0:31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except KeyboardInterrupt:
            print('\n\033[0:31mO usuário optou por não digitar o número.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\n\033[0:31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return n

n = leiaInt('Digite um número Inteiro: ')
n2 = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {n2}')