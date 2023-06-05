lst1 = []
lst2 = []
lst3 = []
lst4 = []
for l in range(1, 5):
    print('--{}ª PESSOA--'.format(l))
    nome = input('NOME: ')
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).lower()
    lst1.append(idade)
    lst2.append(nome)
    lst3.append(sexo)
    if sexo == 'f' and idade < 20:
        lst4.extend('f')
    if sexo == 'm':
        homemv = lst1.index(max(lst1))
if 'm' in lst3:
    hm = lst3.index('m')
    print('O nome do homem mais velho é: ', lst2[homemv])
else:
    hm = 10
    print('Não há homens no grupo.')
print('Há {} mulheres com menos de 20 anos.'.format(lst4.count('f')))

print('A média de idade do grupo é de', sum(lst1) / 4, 'anos.')


