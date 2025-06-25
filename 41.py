def exercicio_41():
    while True:
        try:
            valor_divida = float(input("Digite o valor da dívida: R$ "))
            if valor_divida > 0:
                break
            else:
                print("O valor da dívida deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    dados_parcelas = [
        (1, 0),
        (3, 10),
        (6, 15),
        (9, 20),
        (12, 25)
    ]

    print("\nValor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela")
    print("-------------------------------------------------------------------------")

    for parcelas, percentual_juros in dados_parcelas:
        valor_juros = valor_divida * (percentual_juros / 100)
        valor_total = valor_divida + valor_juros
        if parcelas > 0:
            valor_parcela = valor_total / parcelas
        else:
            valor_parcela = valor_total

        print(f"R$ {valor_total:12.2f} | R$ {valor_juros:12.2f} | {parcelas:23} | R$ {valor_parcela:14.2f}")
