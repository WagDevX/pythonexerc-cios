def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)

def soma(* num):
    s = 0
    for val in num:
        s += val
    print(f'Somando os valores {num} temos {s}.')

soma(5, 2)
soma(2, 9, 4)