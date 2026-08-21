
#Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:

#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

lado_a = float(input("Digite o lado A do triângulo: ").replace(",","."))
lado_b = float(input("Digite o lado B do triângulo: ").replace(",","."))
lado_c = float(input("Digite o lado C do triângulo: ").replace(",","."))


if (lado_a + lado_b) > lado_c and (lado_a + lado_c) > lado_b and (lado_b + lado_c) > lado_a:

    if lado_a == lado_b and lado_b == lado_c:
        print(f"O triângulo é: EQUILÁTERO")

    elif lado_b == lado_c or lado_a == lado_b or lado_a == lado_c:
        print(f"O triângulo é: ISÓSCELES")

    else: 
        print(f" O triângulo é: ESCALENO")

else: 
    print("Os valores informados NÃO formam um triângulo.")
