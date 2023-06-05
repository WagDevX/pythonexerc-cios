palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for c, p in enumerate(palavras):
    print(f'\nNa palavra \33[0:30:41m{p.upper()}\33[m temos: ', end = ' ')
    for char in palavras[c]:
        if char in 'aeiou':
            print(f'\33[30:42m{char}\33[m', end='\33[30:42m \33[m')


