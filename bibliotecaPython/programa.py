from funcoes import *


biblioteca = []

while True:
    while True :
        print('''
[ 1 ] ADICIONAR LIVRO
[ 2 ] EXIBIR LIVROS
[ 3 ] EMPRESTAR LIVRO
[ 4 ] DEVOLVER LIVRO
[ 0 ] SAIR
''')
        op = input('Escolha sua opção: ').strip()
        if op not in ['0', '1', '2', '3', '4']:
            print('opção inválida')
            continue
        break

    if op == '0':
        break
    if op == '1':
        biblioteca = addLivro(biblioteca)
    if op == '2':
        exibirLivros(biblioteca)
    if op == '3':
        biblioteca = emprestarLivro(biblioteca)
    if op == '4':
        bilioteca = devolverLivro(biblioteca)