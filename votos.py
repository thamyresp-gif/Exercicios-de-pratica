
#Em uma eleição para gerência em uma empresa com 20 funcionários, existem quatro candidatos. Escreva um programa que calcule o vencedor da eleição. A votação ocorreu da seguinte maneira:
#Cada funcionário votou em um dos quatro candidatos (representados pelos números 1, 2, 3 e 4).
#Também foram contabilizados os votos nulos (representado pelo número 5) e os votos em branco (representado pelo número 6).
#Ao final da votação, o programa deve exibir o total de votos para cada candidato, o número de votos nulos e o número de votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.


contagem_1 = 0
contagem_2 = 0
contagem_3 = 0  
contagem_4 = 0
contagem_nulos = 0
contagem_brancos = 0

for i in range (20):
    voto = int(input("Digite o número do candidato (1, 2, 3, 4), ou 5 para nulo, ou 6 para branco: "))

    if voto == 1:
        contagem_1 += 1
    elif voto == 2:
        contagem_2 += 1 
    elif voto == 3:
        contagem_3 += 1 
    elif voto == 4:
        contagem_4 += 1
    elif voto == 5:
        contagem_nulos += 1
    elif voto == 6:
        contagem_brancos += 1

porcentagem_nulos = (contagem_nulos / 20) *100

porcentagem_brancos = (contagem_brancos / 20) *100

print("Total de votos para o canditado 1: ", contagem_1)
print("Total de votos para o canditado 2: ", contagem_2)
print("Total de votos para o canditado 3: ", contagem_3)
print("Total de votos para o canditado 4: ", contagem_4)
print("Total de votos nulos: ", contagem_nulos)
print("Total de votos em branco: ", contagem_brancos)
print("Porcentagem de votos nulos: ", porcentagem_nulos)
print("Porcentagem de votos em branco: ", porcentagem_brancos)

maior_votos = max(contagem_1, contagem_2, contagem_3, contagem_4)

if maior_votos == contagem_1:
    print("O candidato vencedor é o candidato 1!")
elif maior_votos == contagem_2:
    print("O candidato vencedor é o candidato 2!")
elif maior_votos == contagem_3:
    print("O candidato vencedor é o candidato 3!")
elif maior_votos == contagem_4:
    print("O candidato vencedor é o candidato 4!")