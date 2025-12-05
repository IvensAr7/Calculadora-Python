from tabulate import *


def carregar():
    lst = [{"ID": 0, "Nome": "Hamburguer", "Preço (R$)": 12.50},
           {"ID": 1, "Nome": "Pizza", "Preço (R$)": 30},
           {"ID": 2, "Nome": "Refrigerante", "Preço (R$)": 5}]
    return lst


def exibir(lst):
    print(tabulate(lst, headers='keys', tablefmt='fancy_grid'))


def busca(id, lst):
    for p in lst:
        if p['id'] == id:
            return p
    return None