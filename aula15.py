num = s = 0
while True:
    num = int(input('Digite um número? '))
    if num == 999:
        break
    s += num
print(f'A soma vale {s}')
