def exercicio_13():
    while True:
        try:
            base = float(input("Digite o número base: "))
            expoente = int(input("Digite o expoente (número inteiro): "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")

    resultado = 1.0
    if expoente >= 0:
        for _ in range(expoente):
            resultado *= base
    else:
        if base == 0:
            print("Erro: Divisão por zero indefinida para base zero e expoente negativo.")
            return
        for _ in range(abs(expoente)):
            resultado /= base
    print(f"{base} elevado a {expoente} é: {resultado}.")