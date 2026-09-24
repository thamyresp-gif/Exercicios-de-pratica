
estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']

estados_unicos = set(estados)
print(estados_unicos)

contagem = {estado: estados.count(estado) for estado in set(estados)}

print(contagem)


