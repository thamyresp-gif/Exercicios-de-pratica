
idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}

try:
    nome = input("Digite o nome do estudante: ")
    resultado = idades[nome]
    print(f"{resultado}")
except KeyError:
    print("Nome não encontrado")

