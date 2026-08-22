
#Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

#O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
#O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.


compra = float(input("Digite a quantidade de litros: ").replace(",","."))

operacao = input("Digite a OPÇÃO escolhida, E (ETANOL) OU D (DIESEL): ").upper()


if operacao == "E":
    preco_litro = 1.70
    if compra <=15:
        desconto = 0.02
    else:
        desconto = 0.04

elif operacao == "D":
    preco_litro = 2.00
    if compra <=15:
        desconto = 0.03
    else: 
        desconto = 0.05

else:
    print("Opção inválida! Digite E para etanol ou D para diesel.")
    exit()

valor_desconto = preco_litro * compra * desconto
valor_a_pagar = (preco_litro * compra) - valor_desconto

print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")





