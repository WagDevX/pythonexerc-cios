city = str(input('Digite o nome da cidade: ')).strip()
cityl = city.lower()
tem = 'santo' in cityl
print('Analisando o nome da cidade...')
if tem is True:
   print('Essa cidade tem Santo no nome.')
else:
   print('Essa cidade não tem Santo no nome.')

# cid = str(input('Em que cidade você nasceu? ')).strip()
# print(cid[:5].upper == 'SANTO')
