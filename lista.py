
#Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.

inputs = []
for i in range(10):
    id_produto = int(input("Digite o ID do produto (número inteiro): "))
    inputs.append(id_produto)

doces = 0
amargos = 0

for id_produtos in inputs:
    if id_produtos % 2 == 0: 
        doces = doces + 1
    else:
        amargos = amargos + 1

print(f"Quantidade de produtos doces: {doces}")
print(f"Quantidade de produtos amargos: {amargos}")

