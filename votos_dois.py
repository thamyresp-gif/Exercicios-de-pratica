
#Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. A pesquisa foi feita e o votos computados podem ser observados abaixo:


votos = {
    "Design 1": 1334,
    "Design 2": 982,
    "Design 3": 1751,
    "Design 4": 210,
    "Design 5": 1811
}


total_votos = sum(votos.values())
max_values = max(votos.values())

for design, qtd_votos in votos.items():
    if qtd_votos == max_values:
        design_mais_votado = design

votos_percentual = (100 * max_values / total_votos)

print(f"Total de votos: {total_votos}")
print(f"Design mais votado: {design_mais_votado} com {max_values} votos.")
print(f"Percentual de votos do design mais votado: {votos_percentual:.2f}%")