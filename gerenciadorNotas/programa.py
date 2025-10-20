from funcoes import *


while True:
    print('''
[ 1 ] Cadastrar aluno e notas
[ 2 ] Exibir relatório
[ 0 ] Sair
''')
    
    while True:
        op = input('Escolha uma opção: ')
        if op not in ['0', '1', '2']:
            print('erro: opção inválida')
            continue
        break
    
    if op == '0':
        break
    elif op == '1':
        listas = notas = []
        nome = input('Digite um nome: ')
        for i in range(3):
            while True:
                try:
                    notas.append(int(input('Digite a {i+1}ª nota: ')))
                    break
                except ValueError:
                    print('Erro: valor inválido')
        