from operacoes import *

def menu():
    print('CALCULADORA PYTHON - por IvensAr7')
    while True:
        try:
            n1 = int(input('Digite o primeiro número: '))
            n2 = int(input('Digite o segundo número: '))
            break
        except ValueError:
            print('Erro: Número inválido')

    print('''
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
    return op, n1, n2


def opcs(op, n1, n2):
    if op == '1':
        resultado = soma(n1, n2)
    elif op == '2':
        resultado = sub(n1, n2)
    elif op == '3':
        resultado = mult(n1, n2)
    elif op == '4':
        resultado = div(n1, n2)
    return resultado

def main():
    op, a, b = menu()
    
    if op == '0':
        return print('FINALIZANDO PROGRAMA')
    else:
        result = opcs(op, a, b)
        print(f'Resultado: {result}')
    
    
if __name__ == '__main__':
    main()