print('--'*13)
print(' Digite abaixo a sua nota')
print('--'*13)
n1 = input('Sua primeira nota foi: ')
n2 = input('Sua segunda nota foi: ')
nota1 = float(n1)
nota2 = float(n2)
not1 = n1.find('.')
not2 = n2.find('.')
if not1 == -1 or not2 == -1:
    print('Você precisa colocar o ponto!')
elif (nota1 + nota2) / 2 <= 5:
    print('Você foi REPROVADO!')
elif (nota1 + nota2) / 2 <= 6.9 and (nota1 + nota2) / 2 >= 5.0:
    print('Você está de RECUPERAÇÃO!')
elif (nota1 + nota2) / 2 >= 7:
    print('PARABÉNS, você foi APROVADO! E sua média foi {}'.format((nota1 + nota2) / 2))
else:
    print('Nota inválida!')

