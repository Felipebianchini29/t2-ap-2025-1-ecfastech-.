def exercicio_12():
    while True:
        try:
            numero = int(input("Digite um número inteiro (1-10) para gerar a tabuada: "))
            if 1 <= numero <= 10:
                break
            else:
                print("O número deve estar entre 1 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    print(f"\nTabuada de {numero}:")
    for i in range(1, 11):
        print(f"{numero} X {i} = {numero * i}")