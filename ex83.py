lista = []
expressao = input('Digite a expressão: ')
lista.append(expressao)
contagem1 = 0
contagem2 = 0
for c in lista[0]:
    if c == '(':
        contagem1 += 1
    elif c == ')':
        contagem2 += 1
if contagem1 == contagem2:
    print('Expressão válida!')
else:
    print('Epxressão inválida!')
