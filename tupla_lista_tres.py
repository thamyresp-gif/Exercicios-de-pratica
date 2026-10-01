
def agrupar(lista1, lista2):
    resultado = []

    for i in range(len(lista1)):
        resultado.append((lista1[i], lista2[i], lista1[i] + lista2[i]))
    return resultado   



