



numero = int(input("Digite um número de 1 a 10: "))


def tabuada(numero):
    print(f"Tabuada do {numero}: ")
    for i in range (0, 10 + 1):
        print(f"{numero} x {i} = {numero * i}")


tabuada(numero)