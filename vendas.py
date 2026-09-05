
#Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:
#{'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
#'Produto D': 200, 'Produto E': 250, 'Produto F': 30}


vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

values = vendas.values()
total_vendas = sum(values)
max_value = max(values)

for produto, valor in vendas.items():
    if valor == max_value:
        produto_mais_vendido = produto
        
print(f"Total de vendas: {total_vendas}")
print(f"Venda mais alta: {max_value}")
print(f"Produto mais vendido: {produto_mais_vendido}")
