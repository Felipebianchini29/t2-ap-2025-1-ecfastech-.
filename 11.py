def exercicio_11():
    while True:
        try:
            num1 = int(input("Digite o primeiro número inteiro: "))
            num2 = int(input("Digite o segundo número inteiro: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros.")

    if num1 > num2:
        num1, num2 = num2, num1

    soma_intervalo = 0
    print(f"Números inteiros no intervalo entre {num1} e {num2}:")
    for i in range(num1 + 1, num2):
        print(i, end=" ")
        soma_intervalo += i
    print()
    print(f"A soma dos números no intervalo é: {soma_intervalo}.")
