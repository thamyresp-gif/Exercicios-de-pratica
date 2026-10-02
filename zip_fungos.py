#dados sem exceção
pressoes = [100, 120, 140, 160, 180]
temperaturas = [20, 25, 30, 35, 40]

#dados com exceção
pressoes = [60, 120, 140, 160, 180]
temperaturas = [0, 25, 30, 35, 40]

#dados de ValueError
pressoes = [100, 120, 140, 160]
temperaturas = [20, 25, 30, 35, 40]


def divide_colunas(pressoes, temperaturas):
    if len(pressoes) != len(temperaturas):
        raise ValueError(f" As listas tem tamanho diferente")

    resultado = []  

    for p, t in zip(pressoes, temperaturas):
            resultado.append(p / t)
    return resultado


# Dados sem exceção
pressoes = [100, 120, 140, 160, 180]
temperaturas = [20, 25, 30, 35, 40]

try:
    print(divide_colunas(pressoes, temperaturas))
except (ValueError, ZeroDivisionError) as e:
    print(f"{type(e).__name__}: {e}")


# Exceção de ZeroDivisionError
pressoes = [60, 120, 140, 160, 180]
temperaturas = [0, 25, 30, 35, 40]

try:
    print(divide_colunas(pressoes, temperaturas))
except (ValueError, ZeroDivisionError) as e:
    print(f"{type(e).__name__}: {e}")


# Exceção de ValueError
pressoes = [100, 120, 140, 160]
temperaturas = [20, 25, 30, 35, 40]

try:
    print(divide_colunas(pressoes, temperaturas))
except (ValueError, ZeroDivisionError) as e:
    print(f"{type(e).__name__}: {e}")