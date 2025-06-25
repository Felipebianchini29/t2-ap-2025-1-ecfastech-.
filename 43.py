def exercicio_43():
    menu = {
        100: {"item": "Cachorro Quente", "preco": 1.20},
        101: {"item": "Bauru Simples", "preco": 1.30},
        102: {"item": "Bauru com ovo", "preco": 1.50},
        103: {"item": "Hambúrguer", "preco": 1.20},
        104: {"item": "Cheeseburguer", "preco": 1.30},
        105: {"item": "Refrigerante", "preco": 1.00}
    }

    print("--- Cardápio da Lanchonete ---")
    print("Código | Especificação    | Preço")
    print("-----|------------------|-------")
    for codigo, info_item in menu.items():
        print(f"{codigo:<4} | {info_item['item']:<16} | R$ {info_item['preco']:.2f}")
    print("--------------------------------")
    print("Digite o código do item e a quantidade. Digite 0 para o código para finalizar o pedido.")

    itens_pedido = []
    valor_total_geral_pedido = 0

    while True:
        try:
            codigo_item = int(input("\nDigite o código do item (0 para finalizar): "))
            if codigo_item == 0:
                break

            if codigo_item not in menu:
                print("Código de item inválido. Por favor, digite um código do cardápio.")
                continue

            quantidade = int(input(f"Digite a quantidade para {menu[codigo_item]['item']}: "))
            if quantidade <= 0:
                print("A quantidade deve ser positiva.")
                continue

            preco_item = menu[codigo_item]['preco']
            total_item = preco_item * quantidade
            itens_pedido.append({'item': menu[codigo_item]['item'], 'quantidade': quantidade, 'preco_unitario': preco_item, 'total': total_item})
            valor_total_geral_pedido += total_item

            print(f"Adicionado: {quantidade} x {menu[codigo_item]['item']} = R$ {total_item:.2f}.")

        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros para código e quantidade.")

    print("\n--- Seu Pedido ---")
    if itens_pedido:
        for item in itens_pedido:
            print(f"{item['quantidade']}x {item['item']} (R$ {item['preco_unitario']:.2f} cada) - Total: R$ {item['total']:.2f}")
        print(f"\nTotal Geral do Pedido: R$ {valor_total_geral_pedido:.2f}.")
    else:
        print("Nenhum item foi pedido.")
