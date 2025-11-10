from tabulate import *


def registrar(lista):
    viagem = {
        'motorista' : '',
        'destino'   : '',
        'distancia' : 0,
        'gasto'     : 0,
        'consumo'   : 0
    }

    viagem['motorista']  = input('Digite o nome do motorista: ').strip().lower()
    viagem['destino']    = input('Destino: ').strip().lower()
    while True:
        try:
            viagem['distancia'] = int(input('Distância (km): '))
            if viagem['distancia'] != 0:
                break
            else:
                print('Valor inválido')
        except ValueError:
            print('erro: valor inválido')
    while True:   
        try:
            viagem['gasto'] = round(float(input('Valor: R$')), 2)
            break
        except ValueError:
            print('erro: valor inválido')
    viagem['consumo'] = round(viagem['gasto'] / viagem['distancia'], 2)

    lista.append(viagem)
         
        
def exibir(lista):
    print(tabulate(lista, headers='keys', tablefmt='fancy_gate'))


def buscar(lista):
    nome    = input('Digite o nome o motorista: ').strip().lower()
    viagens = [viagem for viagem in lista if viagem['motorista'] == nome]
    if len(viagens) == 0:
        print('Motorista não encontrado')
    else:
        exibir(viagens)


def mais_cara(lista):
    maiores = []
    gastos  = [viagem['gasto'] for viagem in lista]
    maior   = max(gastos)
    for viagem in lista:
        if viagem['gasto'] == maior:
            maiores.append(viagem)
    exibir(maiores)


def media(lista):
    return round(sum([viagem['consumo'] for viagem in lista]) / len(lista), 2)