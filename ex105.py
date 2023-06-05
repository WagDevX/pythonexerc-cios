def media(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    cont = 0
    soma = 0
    maior = 0
    menor = 10
    for c in num:
        cont += 1
        soma += c
        if c > maior:
            maior = c
        if c < menor:
            menor = c

    di = dict()
    di['Total'] = cont
    di['Média'] = soma / cont
    di['Maior'] = maior
    di['Menor'] = menor
    if di['Média'] >= 7:
        situ = 'BOA'
    if 7 > di['Média'] >= 4:
        situ = 'RAZOÁVEL'
    if di['Média'] < 4:
        situ = 'RUIM'
    if sit == True:
        di['Situação'] = situ
    return di


resp = media(5.5, 8.5, 7.8, sit=True)
print(resp)
