
#Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.

contagem_0_25 = 0

contagem_26_50 = 0

contagem_51_75 = 0

contagem_76_100 = 0

numero = int(input("Digite uma idade: "))

while numero >= 0:

    if numero >= 0 and numero <= 25:
        contagem_0_25 = contagem_0_25 + 1

    elif numero >= 26 and numero <= 50:
        contagem_26_50 = contagem_26_50 +1

    elif numero >= 51 and numero <= 75:
        contagem_51_75 = contagem_51_75 + 1

    elif numero >= 76 and numero <= 100:
        contagem_76_100 =  contagem_76_100 + 1

    numero = int(input("Digite uma idade: "))

print(f"A contagem de 0 á 25 é: {contagem_0_25}")
print(f"A contagem de 26 á 50 é: {contagem_26_50}")
print(f"A contagem de 51 á 75 é: {contagem_51_75}")
print(f"A contagem de 76 á 100 é: {contagem_76_100}")





