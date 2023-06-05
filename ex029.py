print('ATENÇÂO!!!')
vel = float(input('Qual é a velocidade atual do carro?: '))
calc = vel % 80
multa = calc * 7
if calc < 1:
    print('Tenha um bom dia, dirija com segurança!')
else:
    print('\033[31mVocê foi multado em \033[m\033[33mR${:.2f}!\033[m \033[31mPois excedeu o limite de 80Km/h!'.format(multa))
    print('\033[32mTenha um bom dia, dirija com segurança!')

