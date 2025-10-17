from operacoes import *

def menu():
    while True:
        try:
            n1 = int(input('Digite o primeiro número: '))
            n2 = int(input('Digite o segundo número: '))
            break
        except ValueError:
            print('Erro: Número inválido')

    print('''
CALCULADORA PYTHON - Por Ivens    

OPÇÕES:
    [ 1 ]   ADIÇÃO
    [ 2 ]   SUBTRAÇÃO
    [ 3 ]   MULTIPLICAÇÃO
    [ 4 ]   DIVISÃO
    [ 0 ]   SAIR
''')
    while True:
        op = input('Escolha uma opção: ')
        if op not in ['0', '1', '2', '3', '4'] :
            print('Erro: Opção inexistente')
            continue
        break
    return op


def opcs(op):
    if op == '1':
        resultado = soma(n1, n2)
    elif op == '2':
        resultado = soma(n1, n2)
    elif op == '3':
        resultado = soma(n1, n2)
    elif op == '4':
        resultado = soma(n1, n2)
    else:
        return True
    return 
    