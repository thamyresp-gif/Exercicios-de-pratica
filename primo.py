
#Os números primos possuem várias aplicações dentro da Ciência de Dados, por exemplo, na criptografia e segurança. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

numero = int(input("Digite um número inteiro: "))

for i in range (2, numero):
    if numero % i == 0:
        print(f"Número não é primo!")
        break

else:
    print(f"Número digitado é primo")





