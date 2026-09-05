
#Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:

numero = int(input("Insira um valor de 1 a 10: "))

if numero >= 11:
    print("Erro! Digite um numero de 1 a 10.")

else:
    for i in range (1, 10 + 1):
        numero * i         

        print(f"Valor da tabuada desse número é: {numero} x {i} = {numero * i}")




