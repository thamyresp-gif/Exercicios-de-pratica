
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

resultado = []


for valor in glicemia:

    if valor <= 70:
        situacao = "Hipoglicemia"

    elif valor <= 99:
        situacao = "Normal"

    elif valor <= 125:
        situacao = "Alterada"

    else:
        situacao = "Diabetes"

    resultado.append((situacao, valor))

print(resultado)