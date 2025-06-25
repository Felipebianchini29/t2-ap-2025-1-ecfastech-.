def exercicio_31():
    print("Lojas Tabajara")
    while True:
        valor_total_compra = 0
        item_numero = 1
        print("\n--- Nova Compra ---")
        while True:
            try:
                preco = float(input(f"Produto {item_numero}: R$ "))
                if preco == 0:
                    break
                elif preco < 0:
                    print("O preço não pode ser negativo. Por favor, digite um valor positivo ou 0 para finalizar.")
                else:
                    valor_total_compra += preco
                    item_numero += 1
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        print(f"Total: R$ {valor_total_compra:.2f}")

        while True:
            try:
                dinheiro_recebido = float(input("Dinheiro: R$ "))
                if dinheiro_recebido >= valor_total_compra:
                    troco = dinheiro_recebido - valor_total_compra
                    print(f"Troco: R$ {troco:.2f}")
                    break
                else:
                    print("Dinheiro insuficiente. Por favor, forneça o valor total.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        continuar_comprando = input("Deseja iniciar uma nova compra? (sim/não): ").lower()
        if continuar_comprando != 'sim':
            break
