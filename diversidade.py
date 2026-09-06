
#Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta. A equipe fez a coleta de informações sobre o número de espécies de plantas e animais em cada área dessa floresta e armazenou essas informações em um dicionário. Nele, a chave descreve a área dos dados e os valores nas listas correspondem às espécies de plantas e animais nas áreas, respectivamente.

areas = {
    'Área Norte': [2819, 7236],
    'Área Leste': [1440, 9492],
    'Área Sul': [5969, 7496],
    'Área Oeste': [14446, 49688],
    'Área Centro': [22558, 45148]
}

diversidade = {}

for area, especies in areas.items():
    diversidade[area] = sum(especies) / len(especies)

maior_diversidade = max(diversidade.values())

for area, media in diversidade.items():
    if media == maior_diversidade:
        area_maior_diversidade = area

print(f"Médias de espécies por área: {diversidade}")
print(f"Área com maior diversidade biológica: {area_maior_diversidade} ({maior_diversidade:.2f} espécies em média)")
