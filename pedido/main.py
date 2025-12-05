from cardapio import *
from pedidos  import *

pedido = []

while True:
    print('''
[ 1 ] EXIBIR CARDÁPIO
[ 2 ] FAZER PEDIDO
[ 3 ] EXIBIR PEDIDO
[ 0 ] SAIR
''')
    
    pedidos = []
    cardapio = carregar()
    op       = input('Digite a sua opção: ').strip()
    
    match op:
        case '1':
            exibir(cardapio)
        case '2':
            pedido = novoPedido(cardapio)
        case '3':
            exibirPedido(pedido)
        case '0':
            break
        case _:
            print('Opção inválida.')