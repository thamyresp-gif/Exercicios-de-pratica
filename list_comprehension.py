
aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

valores_apartamento = [item[1] for item in aluguel if item[0] == "Apartamento"]

print(valores_apartamento)

  