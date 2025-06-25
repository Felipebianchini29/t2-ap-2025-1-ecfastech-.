def exercicio_29():
    print("Lojas Quase Dois - Tabela de preços")
    preco_por_item = 1.99
    for i in range(1, 51):
        valor_total = i * preco_por_item
        print(f"{i} - R$ {valor_total:.2f}")
