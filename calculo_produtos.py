from Lista_Produtos import produtos 

# Inicializando variáveis
total_quantidade = 0
valor_total_vendas = 0

# Loop para calcular total de produtos vendidos e valor total de vendas
for produto in produtos:
    total_quantidade += produto["quantidade_vendida"]  # Soma a quantidade vendida
    valor_total_vendas += produto["preco_unitario"] * produto["quantidade_vendida"]  # Calcula o valor total de vendas

# Calculando a média de quantidade vendida
media_quantidade = total_quantidade / len(produtos)

# Exibindo os resultados
print(f'Total de produtos vendidos: {total_quantidade}')
print(f'Média de quantidade de produtos vendidos: {media_quantidade:.2f}')
print(f'Valor total de vendas: R$ {valor_total_vendas:.2f}')