nom = input('Digite seu nome completo: ').strip().lower()
sil = 'silva' in nom
if sil is True:
    print('Você tem Silva no nome.')
else:
    print('Você não tem Silva no nome.')

# nome = str(input(Qual é seu nome completo? ')).strip()
# print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
