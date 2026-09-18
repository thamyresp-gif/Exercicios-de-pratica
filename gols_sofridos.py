
gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

pontos = 0

for marcado, sofrido in zip(gols_marcados, gols_sofridos):
    print(marcado, sofrido)

    if marcado > sofrido:
        pontos = pontos + 3
    elif marcado == sofrido:
        pontos = pontos + 1
    else:
        pontos = pontos + 0

qtd_jogos = len(gols_marcados)

pontuacao_maxima = (qtd_jogos * 3)

aproveitamento = (pontos/pontuacao_maxima) * 100

print(f"A pontuação do time foi de {pontos} e seu aproveitamento foi de {aproveitamento}%")
