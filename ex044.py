valorn = float(input('Digite o valor do produto: '))
print('[1] À vista no dinheiro/cheque.(10% de desconto)')
print('[2] À vista no cartão.(5% de desconto)')
print('[3] Até 2x no cartão.(preço normal)')
print('[4] 3x ou mais no cartão.(20% de JUROS.')
pagamento = input('Digite a condição de pagamento: ')
dinheiro = valorn - valorn * 0.10
cartao = valorn - valorn * 0.05
duasvezes = valorn
tresvezesmais = valorn + valorn * 0.2
if pagamento == '1':
    print('O valor total a pagar é de R${}.'.format(dinheiro))
elif pagamento == '2':
    print('O valor total a pagar é de R${}.'.format(cartao))
elif pagamento == '3':
    print('Sua compra será parcelada em 2x de R${}'.format(valorn / 2))
    print('O valor total a pagar é de R${}.'.format(duasvezes))
elif pagamento == '4':
    parcelamento = int(input('Quantas parcelas? '))
    if parcelamento < 3:
        print('Nessa opção, somente a partir de 3 vezes!')
    else:
        print('Sua compra será parcelada em {}x de R${} COM JUROS'.format(parcelamento, tresvezesmais / parcelamento))
        print('O valor total a pagar é de R${}.'.format(tresvezesmais))
else:
    print('Opção inválida!')
