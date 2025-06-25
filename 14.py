def exercicio_14():
    pares_contagem = 0
    impares_contagem = 0
    for i in range(10):
        while True:
            try:
                num = int(input(f"Digite o número inteiro {i+1}: "))
                if num % 2 == 0:
                    pares_contagem += 1
                else:
                    impares_contagem += 1
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")
    print(f"Quantidade de números pares: {pares_contagem}.")
    print(f"Quantidade de números ímpares: {impares_contagem}.")
