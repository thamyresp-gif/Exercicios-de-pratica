
#Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.


precos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]


contador = 0

for preco in precos:
    if preco > 3000:
        contador += 1

total_compras = len(precos)
porcentagem = (contador / total_compras) * 100

print(f"Quantidade de compras acima de 3000 reais: {contador}")
print(f"Total de compras: {total_compras}")
print(f"Porcentagem de compras acima de 3000 reais: {porcentagem:.2f}%")


