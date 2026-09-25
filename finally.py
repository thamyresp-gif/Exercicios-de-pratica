
def converter_lista(lista):
    lista_convertida = []
    try:
        for item in lista:
            lista_convertida.append(float(item))
    except ValueError as erro:
        print(f"Erro de valor (ValueError): não foi possível converter '{item}' para float. Detalhes: {erro}")
    except TypeError as erro:
        print(f"Erro de tipo (TypeError): tipo de dado inválido. Detalhes: {erro}")
    else:
        return lista_convertida
    finally:
        print("Fim da execução da função")

