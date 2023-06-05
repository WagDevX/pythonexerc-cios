pessoas = {'nome': 'Wagner', 'sexo': 'M', 'idade': 28}
pessoas['peso'] = 65.5
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
for k, v in pessoas.items():
    print(f'{k} = {v}')