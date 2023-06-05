dados = dict()
gols = list()
dados['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
dados['Gols'] = gols[:]
dados['Total'] = sum(gols)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'{k}: {v}')
print('-=' * 30)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')
for p, g in enumerate(gols):
    print(f'{f"   => Na partida {p}, fez {g} gols."}')
print(f'Foi um total de {dados["Total"]} gols.')
