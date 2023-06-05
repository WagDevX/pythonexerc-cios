s = input('Qual o seu sexo? [M/F]: ').strip().upper()[0]
while s != 'M' and s != 'F':
    s = input('Dados inválidos. Por favor, informe seu sexo: ').strip().upper()[0]
if s == 'M':
    print('Sexo masculino registrado com sucesso!')
elif s == 'F':
    print('Sexo feminino registrado com sucesso!!')
