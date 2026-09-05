
#Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.

lista = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    lista.append(numero)

print(f"A lista de números inteiros é: {lista}")

lista_invertida = []

for i in range(4, -1, -1):
    lista_invertida.append(lista[i])

print(f"A lista invertida é: {lista_invertida}")