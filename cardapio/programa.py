from funcoes import *


while True:
    print('''
Menu:
[ 1 ] Ver cardápio
''')
    cardapio = carregar()
    op       = input('Escolha a opção: ').strip()

    match op:
        case '1':
            exibir(cardapio)