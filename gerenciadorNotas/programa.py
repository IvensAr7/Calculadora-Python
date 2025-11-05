from funcoes import *
import pandas as pd


lista = []
while True:
    dicio = {
        'nome'  : '',
        'notas' : [],
        'media' : 0
    }
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
        print('Finalizando programa')
        break
    elif op == '1':
        notas = []
        nome = input('Digite um nome: ')
        for i in range(3):
            while True:
                try:
                    notas.append(int(input(f'Digite a {i+1}ª nota: ')))
                    break
                except ValueError:
                    print('Erro: valor inválido')
        dicio['nome'] = nome
        dicio['notas'] = notas
        dicio['media'] = calcular_media(notas)
        lista.append(dicio)
    elif op == '2':
        df = pd.DataFrame(lista)
        print(df)
        