lst = []
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    lst.append(peso)
print('O maior peso da lista é {:.1f}Kg'.format(max(lst)))
print('O menor peso da lista é {:.1f}Kg'.format(min(lst)))
