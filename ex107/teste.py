from ex107 import moeda

p = float(input('Digite o preçõ: R$ '))
print(f'A metade de R$ {p} é R${moeda.metade(p)}')
print(f'O dobro de R$ {p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(p, 10)}')
print(f'Diminuindo 15%, temos R$ {moeda.diminuir(p, 15)}')
