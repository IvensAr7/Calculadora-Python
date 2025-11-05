def calcular_media(lst):
    return sum(lst)/len(lst)


def verificar_situacao(media):
    if media >= 7:
        return 'APROVADO'
    elif media < 5:
        return 'REPROVADO'
    else:
        return 'RECUPERAÇÃO'
    

           