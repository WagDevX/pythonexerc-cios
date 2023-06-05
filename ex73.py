brasileirao = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians',
               'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'Botafogo', 'Santos',
               'São Paulo', 'Bragantino', 'Goiás', 'Coritiba', 'Ceará SC',
               'Cuiabá', 'Atlético-GO', 'Avaí', 'Juventude')
print('-='*15)
print(f'Lista de times do Brasileirão: {brasileirao}')
print('-='*15)
print(f'Os 5 primeiros são: {brasileirao[0:5]}')
print('-='*15)
print(f'Os 4 últimos são {brasileirao[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('-='*15)
time = input('Digite o nome do time para saber a posição: ').strip()
while time not in brasileirao:
    time = input(f'{time} não está na lista. Tente novamente: ').strip()
print(f'O {time} está na {brasileirao.index(time)+1}ª posição')
