def fatorial(n, show=False):
  """
  -> Calcula o Fatorial de um número.
  :param n: O número a ser calculado.
  :param show: (opicional) Mostrar ou não a conta.
  :return: O valor do Fatorial de um número n.
  """
  f = 1
  cont = 0
  for c in range(n, 0, -1):
    f *= c
    cont += 1
    if show:
      print(f'{c} ', end='')
      if cont < n:
        print('x ', end='')
  if show:
    print('=', end=' ')
  return f

help(fatorial)
print(fatorial(5, show=True))

