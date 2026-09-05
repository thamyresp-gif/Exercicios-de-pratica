
#Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).

temperaturas = []

for i in range(12):
    temp = float(input(f"Digite a temperatura média do mês {i + 1}: ").replace(",","."))
    temperaturas.append(temp)

media_anual = sum(temperaturas) / len(temperaturas)

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

print(f"A média anual das temperaturas é: {media_anual:.2f}°C")

print("Temperaturas acima da média anual:")
for i in range(12):
    if temperaturas[i] > media_anual:
        print(f"{meses[i]}: {temperaturas[i]:.2f}°C")