def exercicio_30():
    while True:
        try:
            preco_pao = float(input("Preço do pão: R$ "))
            if preco_pao > 0:
                break
            else:
                print("O preço do pão deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    print(f"\nPanificadora Pão de Ontem - Tabela de preços")
    for i in range(1, 51):
        valor_total = i * preco_pao
        print(f"{i} - R$ {valor_total:.2f}")

     