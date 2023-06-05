from datetime import date
nome = input('Qual é o seu nome?: ')
ano = int(input('Que ano você nasceu?: '))
peso = input('Qual é o seu peso?: ')
idade = date.today().year - ano
print('Olá {}, você tem {} anos e você pesa {}. Parabéns, você é linda!'.format(nome, idade, peso))