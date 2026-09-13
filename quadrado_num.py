
lista_notas = []

for i in range(5):
    notas = float(input("Digite a nota: "))
    lista_notas.append(notas)


maior = max(lista_notas)
menor = min(lista_notas)

lista_notas.remove(maior)
lista_notas.remove(menor)


def media(lista_notas):
    calculo = sum(lista_notas) / 3
    return calculo


resultado = media(lista_notas)
print(f"Nota da manobra: {resultado}")