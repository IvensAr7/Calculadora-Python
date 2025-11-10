from funcoes import *

lista = []
while True:
    print('''
[ 1 ] REGISTRAR NOVA VIAGEM
[ 2 ] EXIBIR TODAS AS VIAGENS
[ 3 ] BUSCAR VIAGEM POR MOTORISTA
[ 4 ] EXIBIR VIAGEM MAIS CARA
[ 5 ] MOSTRAR MÉDIA GERAL DE CONSUMO 
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