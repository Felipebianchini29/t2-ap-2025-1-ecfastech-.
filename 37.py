def exercicio_37():
    dados_clientes = []
    print("Digite os dados dos clientes (código, altura, peso). Digite 0 para o código para finalizar.")

    while True:
        try:
            codigo = int(input("Digite o código do cliente (0 para finalizar): "))
            if codigo == 0:
                break
            altura = float(input("Digite a altura do cliente (em metros): "))
            peso = float(input("Digite o peso do cliente (em kg): "))

            if altura <= 0 or peso <= 0:
                print("Altura e peso devem ser valores positivos. Por favor, redigite para este cliente.")
                continue

            dados_clientes.append({'codigo': codigo, 'altura': altura, 'peso': peso})
        except ValueError:
            print("Entrada inválida. Por favor, digite números para código, altura e peso.")

    if not dados_clientes:
        print("Nenhum dado de cliente foi inserido.")
        return

    cliente_mais_alto = None
    cliente_mais_baixo = None
    cliente_mais_gordo = None
    cliente_mais_magro = None

    soma_alturas = 0
    soma_pesos = 0

    for cliente in dados_clientes:
        if cliente_mais_alto is None or cliente['altura'] > cliente_mais_alto['altura']:
            cliente_mais_alto = cliente
        if cliente_mais_baixo is None or cliente['altura'] < cliente_mais_baixo['altura']:
            cliente_mais_baixo = cliente
        if cliente_mais_gordo is None or cliente['peso'] > cliente_mais_gordo['peso']:
            cliente_mais_gordo = cliente
        if cliente_mais_magro is None or cliente['peso'] < cliente_mais_magro['peso']:
            cliente_mais_magro = cliente

        soma_alturas += cliente['altura']
        soma_pesos += cliente['peso']

    media_alturas = soma_alturas / len(dados_clientes)
    media_pesos = soma_pesos / len(dados_clientes)

    print("\n--- Resultados do Censo ---")
    print(f"Cliente mais alto: Código {cliente_mais_alto['codigo']}, Altura {cliente_mais_alto['altura']:.2f} m.")
    print(f"Cliente mais baixo: Código {cliente_mais_baixo['codigo']}, Altura {cliente_mais_baixo['altura']:.2f} m.")
    print(f"Cliente mais gordo: Código {cliente_mais_gordo['codigo']}, Peso {cliente_mais_gordo['peso']:.2f} kg.")
    print(f"Cliente mais magro: Código {cliente_mais_magro['codigo']}, Peso {cliente_mais_magro['peso']:.2f} kg.")
    print(f"Média das alturas dos clientes: {media_alturas:.2f} m.")
    print(f"Média dos pesos dos clientes: {media_pesos:.2f} kg.")
