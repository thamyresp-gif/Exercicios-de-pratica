
n_numero1 = float(input("digite um numero: ").replace(",", "."))
n_numero2 = float(input("digite o numero: ").replace(",", "."))
n_numero3 = float(input("digite o terceiro numero: ").replace(",", "."))

soma = n_numero1 + n_numero2
subtracao = soma - n_numero3
print(f"A soma dos dois primeiros numeros é: {soma}")

print(f"A subtração do terceiro numero com a soma dos dois primeiros numeros é: {subtracao}")

