from datetime import date
hoje = date.today().year
s = 0
for i in range(1, 8):
    ano = int(input('Qual é o ano de nascimento da pessoa {}: '.format(i)))
    idade = hoje - ano
    if idade >= 18:
        s += 1
print(s, 'pessoas já atingiram a maioridade, {} ainda não'.format(7-s))