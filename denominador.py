
#Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

n_numero1 = float (input("Digite um numero: ").replace(",", ".")) 
n_numero2 = float(input("Digite o denominador: ").replace(",", "."))

if n_numero2 == 0:
    print("Erro: o denominador não pode ser 0.")
else:
    divisao = n_numero1 / n_numero2
    print(f"A divisão entre {n_numero1} e {n_numero2} é: {divisao}")

    