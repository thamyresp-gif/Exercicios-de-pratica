
id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

dados = [(id_item, qtd_item, preco_item, qtd_item * preco_item) for id_item, qtd_item, preco_item in zip(id, quantidade, preco)]

tabela = [('id', 'quantidade', 'preco', 'total')] + dados

print(tabela)


