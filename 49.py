def exercicio_49():
    while True:
        try:
            n = int(input("Digite o número de termos (n) para a série: "))
            if n > 0:
                break
            else:
                print("Por favor, digite um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    soma_serie = 0
    termos = []
    for i in range(1, n + 1):
        numerador = i
        denominador = 2 * i - 1
        termo = numerador / denominador
        termos.append(f"{numerador}/{denominador}")
        soma_serie += termo
    
    print(f"Série: {' + '.join(termos)}")
    print(f"Soma da série: {soma_serie:.4f}")
