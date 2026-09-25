

try:
    num_1 = float(input("Digite um número: ").replace(",","."))
    num_2 = float(input("Digite um número: ").replace(",","."))
    
    divisao = num_1 / num_2
    print(f"Resultado: {divisao}")

except ValueError:
        print("Erro: você não digitou um número válido")
except ZeroDivisionError: 
    print("Erro: não é possível dividir por zero")



