#importa biblioteca re
import re
def leiaint(txt):
    #Lê um argumento dado pelo usuário
    n = input(f'{txt}')
    #Checa se o dado que o usuário colocou é um número inteiro
    match = re.search("\D", n)
    #Enquanto o dado que o usuário não for um número inteiro, aparecerá uma tela de erro e será perguntado novamente.
    while match:
        print('ERRO! Digite um número inteiro válido.')
        n = input(f'{txt}')
        match = re.search("\D", n)
    #Se o usuário digitar um número inteiro, retorna o valor digitado como n.
    if not match:
        return n


#Programa Principal
#Utiliza a função leiaint como input para registrar dado do usuário
n = leiaint('Digite um número: ')
#Mostra na tela o número que o usuário digitou
print(f'Você acabou de digitar o número {n}')