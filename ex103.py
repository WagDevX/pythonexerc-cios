def ficha(n=0, g=0):
    if n == '':
        n = '<desconhecido>'
    if g == '':
        g = "0"
    print(f'O jogador {n} fez {g} gol(s) no campeonato!')


#Programa Principal
print('=' * 25)
jogador = input('Nome do jogador: ')
gols = input('Quantidade de gols marcados: ')
ficha(jogador, gols)
