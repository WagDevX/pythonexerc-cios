from ex115 import menu
from time import sleep
from ex115 import arquivo

arq = 'cursoemvideo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = menu.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        #Opção de lsitar o conteúdo de um arquivo
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        menu.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = menu.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        menu.cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)
