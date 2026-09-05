
# Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.

numero = int(input("Digite um número inteiro: "))
primos = []

for i in range (2, numero + 1):
    primo = True
    for j in range (2, i):
        if i % j == 0:
            primo = False
            break
    if primo:
        primos.append(i)

print(f"Os números primos entre 1 e {numero} são: {primos}")    

