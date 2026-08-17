
#Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

numero1 = input("Digite um numero: ").replace(",",".")
numero2 = input("Digite outro numero: ").replace(",",".")


operação = input("Digite a operação  +,-,*,/: ")


if operação == "+":
    soma = float(numero1) + float(numero2)
    print (f"O resultado da soma é: {soma}")
    if soma % 2 == 0: 
        print("O número é par")
    else: 
        print("O numero é impar")
    if soma > 0: 
        print ("O numero é positivo")
    elif soma < 0:
        print ("O numero é negativo")
    else:
        print ("O número é zero")
    if soma % 1 == 0:
        print ("O numero é inteiro")
    else:
        print ("O número é decimal")
                        

elif operação == "-":
    subtracao = float(numero1) - float(numero2) 
    print (f"O resultado da subtração é: {subtracao}")
    if subtracao % 2 == 0:
        print("O numero é par")
    else:
        print("O numero é impar")
    if subtracao > 0:
        print ("O número é positivo")
    elif subtracao < 0:
        print("O número é negativo")
    else:
        print ("O número é ZERO")
    if subtracao % 1 == 0:
        print ("O número é inteiro")
    else: 
        print ("O número é decimal")


elif operação == "*":
    multiplicacao = float(numero1) * float(numero2)
    print (f"O resultado da multiplicação é: {multiplicacao}")
    if multiplicacao % 2 == 0:
        print("O numero é par")
    else:
        print("O numero é impar")
    if multiplicacao > 0:
        print ("O número é positivo")
    elif multiplicacao < 0:
        print("O número é negativo")
    else:
        print ("O número é ZERO")
    if multiplicacao % 1 == 0:
        print ("O número é inteiro")
    else: 
        print ("O número é decimal")


elif operação == "/":
    if float (numero2) == 0:
        print ("ERRO: numero 2 não pode ser 0 (ZERO)")
    else:
        divisao = float(numero1) / float(numero2)
        print (f"O resultado da divisão é: {divisao}")
    
        if divisao % 2 == 0:
            print("O numero é par")
        else:
            print("O numero é impar")
        if divisao > 0:
            print ("O número é positivo")
        elif divisao < 0:
            print("O número é negativo")
        else:
            print ("O número é ZERO")
        if divisao % 1 == 0:
            print ("O número é inteiro")
        else: 
            print ("O número é decimal")





