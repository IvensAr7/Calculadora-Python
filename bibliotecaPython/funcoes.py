from tabulate import *

class C:
    R = '\033[91m'
    G = '\033[38;5;76m' 
    O = '\033[38;5;202m'
    Y = '\033[38;5;184m'
    RESET = '\033[0m' # RESET

def addLivro(biblioteca):
    livro = {
        'titulo' : '',
        'autor'  : '',
        'status' : f'{C.G}DISPONÍVEL{C.RESET}'
    }

    livro['titulo'] = input('Digite o título do livro: ').strip().lower()
    livro['autor']  = input('Digite o autor do livro: ').strip().lower()  

    biblioteca.append(livro)
    return biblioteca


def emprestarLivro(biblioteca):
    input("diz o livro ")
    





def exibirLivros(biblioteca):
    print(tabulate(biblioteca, headers="keys", tablefmt="outline"))