from tabulate import *


def carregar():
    lst = [{"id": 1, "nome": "Hambúrguer", "Preço (R$)": 12.50},
           {"id": 2, "nome": "Pizza", "Preço (R$)": 30},
           {"id": 3, "nome": "Refrigerante", "Preço (R$)": 5}]
    return lst


def exibir(lst):
    print(tabulate(lst, headers='keys', tablefmt='fancy_grid'))


def add(lst, pedido):
    id = int(input('Digite o ID o seu pedido: '))