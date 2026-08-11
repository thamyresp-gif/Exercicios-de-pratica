
#Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

n_numerador = float(input("Digite numerador: ").replace(",","."))
n_denominador = float(input("Digite denominador: ").replace(",","."))


if n_denominador == 0:
    print("Erro: Não pode ser 0 (Zero)")


else:
    resto = n_numerador % n_denominador 
    print(f"O resto da divisão entre {n_numerador} e {n_denominador} é {resto}")



