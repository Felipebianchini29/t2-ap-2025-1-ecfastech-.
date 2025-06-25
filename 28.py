def exercicio_28():
    while True:
        try:
            quantidade_cds = int(input("Digite a quantidade de CDs na coleção: "))
            if quantidade_cds >= 0:
                break
            else:
                print("A quantidade de CDs não pode ser negativa.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    valor_total_investido = 0
    if quantidade_cds > 0:
        for i in range(quantidade_cds):
            while True:
                try:
                    valor_cd = float(input(f"Digite o valor do CD {i+1}: R$ "))
                    if valor_cd >= 0:
                        valor_total_investido += valor_cd
                        break
                    else:
                        print("O valor do CD não pode ser negativo.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
        media_gasta = valor_total_investido / quantidade_cds
        print(f"Valor total investido na coleção de CDs: R$ {valor_total_investido:.2f}.")
        print(f"Valor médio gasto em cada CD: R$ {media_gasta:.2f}.")
    else:
        print("Nenhum CD foi inserido, portanto não há investimento para calcular.")
