jogadores = list()
dados = dict()
gols = list()
while True:
    dados['Nome'] = str(input(('Nome do Jogador: ')))
    qtdpartidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    for c in range(0, qtdpartidas):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    dados['Gols'] = gols[:]
    dados['Total'] = sum(gols)
    jogadores.append(dados.copy())
    gols.clear()
    continuar = input('Quer continuar? [S/N] ')
    if continuar in 'Nn':
        break
print('-=' * 28)

print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('=' * 40)
for n, j in enumerate(jogadores):
    print(f'{n:>3} ', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    jogador = int(input('Mostrar dados de qual jogador? '))
    if jogador == 999:
        print('>>> VOLTE SEMPRE <<<')
        break
    if jogador >= len(jogadores):
        print(f'ERRO! Não Existe jogador com o código {jogador}!')
    else:
        print(f'== LEVANTAMENTO DO JOGADOR {jogadores[jogador]["Nome"]:}')
        for j, g in enumerate(jogadores[jogador]['Gols']):
            print(f'{"No jogo {} fez {} gols.":>28}'.format(j + 1, g))

