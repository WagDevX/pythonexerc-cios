def aumentar(preco=0, taxa=0, format=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: o preço que se quer reajustar
    :param taxa: qual é a porcentagem de aumento
    :param format: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    res = preco + (preco * taxa/100)
    return res if format is False else moeda(res)


def diminuir(preco=0, taxa=0, format=False):
    res = preco - (preco * taxa/100)
    return res if format is False else moeda(res)


def metade(preco=0, format=False):
    res = preco / 2
    return res if not format else moeda(res)


def dobro(preco=0, format=False):
    res = preco * 2
    return res if not format else moeda(res)


def moeda(preco=0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taum=10, tdim=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taum}% de aumento: \t{aumentar(preco, taum, True)}')
    print(f'{tdim}% de redução: \t{diminuir(preco, tdim, True)}')
    print('-' * 30)

