def exercicio_20():
    while True:
        while True:
            try:
                num = int(input("Digite um número inteiro positivo (menor que 16) para calcular seu fatorial: "))
                if 0 <= num < 16:
                    break
                else:
                    print("Por favor, digite um número inteiro positivo menor que 16.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")

        if num == 0:
            fatorial = 1
        else:
            fatorial = 1
            for i in range(1, num + 1):
                fatorial *= i
        print(f"O fatorial de {num} é: {fatorial}.")

        repetir = input("Deseja calcular outro fatorial? (sim/não): ").lower()
        if repetir != 'sim':
            break