def exercicio_10():
    while True:
        try:
            num1 = int(input("Digite o primeiro número inteiro: "))
            num2 = int(input("Digite o segundo número inteiro: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros.")
    if num1 > num2:
        num1, num2 = num2, num1 

    print(f"Números inteiros no intervalo entre {num1} e {num2}:")
