from time import sleep
import numpy as np
students = list()
student = list()
notes = list()

while True:
    student.append(str(input('Nome: ')))
    notes.append(float(input('Nota 1: ')))
    notes.append(float(input('Nota 2: ')))
    student.append(notes[:])
    students.append(student[:])
    student.clear()
    notes.clear()
    continuar = ''
    while 'S' != continuar != 'N':
        continuar = input('Deseja continuar?[S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break
    else:
        continue
print('No. NOME              MÉDIA')
print('=' * 30)
for n, s in enumerate(students):
    print(f'{n:<4}{s[0]:<18}{np.mean(s[1]):<15}')
print('=' * 30)
while True:
    nota = int(input('Mostrar notas de qual aluno?(999 Sai): '))
    if nota == 999:
        break
    print(f'Notas de {students[nota][0]} são {students[nota][1]}')
    print('=' * 30)
print('FINALIZANDO...')
sleep(0.5)
print('<<< VOLTE SEMPRE >>>')


