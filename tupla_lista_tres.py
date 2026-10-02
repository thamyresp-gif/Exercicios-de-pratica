

def agrupar_listas(lista1, lista2):
    try:
        if len(lista1) != len(lista2):
            raise IndexError("A quantidade de elementos em cada lista é diferente")

        resultado  = [] 
        for i in range(len(lista1)):
            resultado.append((lista1[i], lista2[i], lista1[i] + lista2[i]))

        return resultado

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


