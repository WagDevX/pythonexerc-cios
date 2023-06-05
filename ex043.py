print('+'*37)
print(' Cálculo de Índice de Massa Corporal')
print('+'*37)
altura = float(input('Digite a sua altura (m): '))
peso = float(input('Digite o seu peso (Kg): '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu IMC é: {:.1f} \nVocê está abaixo do peso!'.format(imc))
elif 25 > imc > 18.5:
    print('Seu IMC é: {:.1f} \nVocê está no peso ideal!'.format(imc))
elif 30 < imc > 25:
    print('Seu IMC é: {:.1f} \nVocê está com sobrepeso!'.format(imc))
elif 40 < imc > 30:
    print('Seu IMC é: {:.1f} \nVocê está com obesidade!'.format(imc))
elif imc >= 40:
    print('Seu IMC é: {:.1f} \nVocê está com obesidade mórbida!'.format(imc))
else:
    print('Valor inválido!')
