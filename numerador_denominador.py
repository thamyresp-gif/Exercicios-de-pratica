
#Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

numerador_numero1 = float(input("Digite um numerador: "))
denominador_numero2 = float(input("Digite denominador: "))

if denominador_numero2 == 0:
    print ("Erro: Não pode ser 0 (Zero)")

else:
    divisao = numerador_numero1 // denominador_numero2
    print (f"A divisão entre {numerador_numero1} e {denominador_numero2} é {divisao}")

