from tabulate import *


def carregar():
    lst = [{"ID": 1, "Nome": "Hamburguer", "Preço (R$)": 12.50},
           {"ID": 2, "Nome": "Pizza", "Preço (R$)": 30},
           {"ID": 3, "Nome": "Refrigerante", "Preço (R$)": 5}]
    return lst


def exibir(lst):
    print(tabulate(lst, headers='keys', tablefmt='fancy_grid'))


def add(lst, pedidos):
    while True:
        try:    
            id = int(input('Digite o ID o seu pedido: ')).strip()
            if 0 < id <= len(lst):
                break
            print('Valor inválido')
        except ValueError:
            print('Valor inválido')

    while True:
        try:    
            quant = int(input('Quantidade: ')).strip()
            total = lst[id]['Preço (R$)'] * quant
            break
        except ValueError:
            print('Valor inválido')
    
    pedido = {
        'Item'       : lst[id]['Nome'],
        'Quantidade' : quant,
        'Total'      : total
    }

    pedidos.append(pedido)


def exibirPedidos(pedidos):
    total = sum( [ item['Total'] for item in pedidos ] )
    exibir(pedidos)
    print('Preço Total: R${total:.2f}')


def remover(lst, pedidos):
    while True:
        id = input('Digite o nome ou ID: ')
        if id.isnumeric():
            verf = False
            nomes = [ pedido['Item'] for pedido in pedidos ]
            nome  = lst[id]['Nome'].lower()
            for n in nomes:
                if n == nome:
                    verf = True
                    pos = nomes.index(n)
                    pedidos.pop(pos)
            if verf:
                break
            else:
                print('Valor inválido')
                continue

        elif id.isalpha():
            verf = False
            nomes = [ pedido['Item'] for pedido in pedidos ]
            for n in nomes:
                if id == n:
                    verf = True
                    pos = nomes.index(n)
                    pedidos.pop(pos)
            if verf:
                break
            else:
                print('Valor inválido')
                continue

        else:
            print('Valor inválido')


