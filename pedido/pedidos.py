from cardapio import *
from tabulate import *

def novoPedido(lst):
    pedido = []

    print('Adicione itens ao seu pedido')
    
    while True:
        exibir(lst)
        
        while True:
            try:    
                id = int(input('Digite o ID o seu pedido: '))
                if 0 <= id < len(lst):
                    break
                print('Valor inválido')
            except ValueError:
                print('Valor inválido')

        while True:
            try:    
                quant = int(input('Quantidade: '))
                total = lst[id]['Preço (R$)'] * quant
                break
            except ValueError:
                print('Valor inválido')
        
        item = {
            'Item'       : lst[id]['Nome'],
            'Quantidade' : quant,
            'Total'      : total
        }

        pedido.append(item)

        while True:
            op = input('Deseja adicionar mais um item? [S/N] \n : ').strip().upper()
            match op:
                case 'S':
                    break
                case 'N':
                    return pedido
                case _:
                    print('Inválido')


def calcular(lst):
    total = 0
    for i in lst:
        total += i['Total']
    if total > 50:
        total *= 0.9
    return total


def exibirPedido(pedido):
    tot = calcular(pedido)
    exibir(pedido)
    print(f'Total: R${tot:.2f}')






