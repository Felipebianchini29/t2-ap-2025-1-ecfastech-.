def exercicio_42():
    contagem_intervalos = {
        '[0-25]': 0,
        '[26-50]': 0,
        '[51-75]': 0,
        '[76-100]': 0
    }

    print("Digite números positivos. Digite um número negativo para finalizar.")
    while True:
        try:
            num = float(input("Digite um número: "))
            if num < 0:
                break

            if 0 <= num <= 25:
                contagem_intervalos['[0-25]'] += 1
            elif 26 <= num <= 50:
                contagem_intervalos['[26-50]'] += 1
            elif 51 <= num <= 75:
                contagem_intervalos['[51-75]'] += 1
            elif 76 <= num <= 100:
                contagem_intervalos['[76-100]'] += 1
            elif num > 100:
                print("Número é maior que 100 e não é contado nos intervalos especificados.")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    print("\n--- Contagem por Intervalos ---")
    for intervalo, contagem in contagem_intervalos.items():
        print(f"{intervalo}: {contagem} números.")
