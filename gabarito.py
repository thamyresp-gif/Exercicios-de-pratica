
#Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.

gabarito = ["D", "A", "C", "B", "A", "D", "C", "C", "A", "B"]

respostas = []

for i in range(10):
    input_resposta = (input(f"Digite a resposta da questão {i + 1}: ").upper())
    respostas.append(input_resposta)

notas = 0

for i in range (len(gabarito)):
    if respostas[i] == gabarito[i]:
        notas = notas + 1

print(f"Você acertou {notas} de 10 questões.")

