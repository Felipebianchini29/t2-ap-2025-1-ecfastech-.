def exercicio_17():
    while True:
        try:
            num = int(input("Digite um número inteiro para calcular seu fatorial: "))
            if num >= 0:
                break
            else:
                print("Por favor, digite um número inteiro não negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    if num == 0:
        fatorial = 1
    else:
        fatorial = 1
        for i in range(1, num + 1):
            fatorial *= i
    print(f"O fatorial de {num} é: {fatorial}.")