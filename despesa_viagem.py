
def gasto_hotel(dias):
    valor = 150 * dias
    return valor

dias = int(input("Digite quantos dias deseja ficar: "))
gasto_total_hotel = gasto_hotel(dias)

def gasto_gasolina(distancia):
    distancia_total = distancia * 2
    litros_gastos = distancia_total / 14
    custo = litros_gastos * 5
    return custo

def gasto_passeio(valor_diario, dias):
    valor = valor_diario * dias
    return valor

dias = 3
distancia_salvador = 850
valor_diario_salvador = 200


total = gasto_hotel(dias) + gasto_gasolina(distancia_salvador) + gasto_passeio(valor_diario_salvador, dias)

print(f"Com base nos gastos definidos, uma viagem de {dias} dias para Salvador saindo de Recife custaria {round(total, 2)} reais")