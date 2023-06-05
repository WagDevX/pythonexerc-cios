from time import sleep
print('\033[32m|\033[m'*33)
print(' Seja bem vindo ao \033[32mFinanciaZero!')
print('\033[32m|'*33)
casav = float(input('Qual é o valor da sua casa?: '))
sal = float(input('Qual é o seu salário?: '))
anos = int(input('Em quantos anos pretende pagar?: \033[m'))
prest = anos * 12
margem = sal * 0.30
vp = casav / prest
if vp <= margem:
    print('CALCULANDO...')
    sleep(2)
    print('Parabéns! Seu empréstimo foi aprovado!')
    print('O valor da prestação é de R${:.2f}.'.format(vp))
else:
    print('O seu empréstimo foi negado pois R${} excede o limite de 30% do seu salário!'.format(vp))
