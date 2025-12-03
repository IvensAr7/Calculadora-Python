from cardapio import *
from pedidos  import *


while True:
    print('''
[ 1 ] EXIBIR CARDÁPIO
[ 2 ] FAZER PEDIDO
[ 3 ] EXIBIR PEDIDO
[ 0 ] SAIR
''')
    
    op = input('Digite a sua opção: ').strip()
    
    match op:
        case '1':
            registrar(lista)
        case '2':
            exibir(lista)
        case '3':
            buscar(lista)
        case '4':
            mais_cara(lista)
        case '5':
            med = media(lista)
            print(f'Média de consumo: {med}')
        case '0':
            break
        case _:
            print('Opção inválida.')