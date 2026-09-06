
#O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) de 4 setores da empresa. Para isso, foram fornecidos os seguintes dados:
#Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.


setores = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
}

media_por_setor = {}

for setor, idades in setores.items():
    media_por_setor[setor] = sum(idades) / len(idades)

idades_gerais = []
for setor, idades in setores.items():
    for idade in idades:
        idades_gerais.append(idade)

media_geral = sum(idades_gerais) / len(idades_gerais)

pessoas_acima_da_media = 0
for idade in idades_gerais:
    if idade > media_geral:
        pessoas_acima_da_media = pessoas_acima_da_media + 1

print(f"Médias de idade por setor: {media_por_setor}")
print(f"Idade média geral: {media_geral:.2f}")
print(f"Número de pessoas acima da idade média geral: {pessoas_acima_da_media}")

