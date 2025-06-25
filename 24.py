def exercicio_24():
    notas = []
    while True:
        try:
            n = int(input("Digite a quantidade de notas (N): "))
            if n > 0:
                break
            else:
                print("N deve ser um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    for i in range(n):
        while True:
            try:
                nota = float(input(f"Digite a nota {i+1}: "))
                notas.append(nota)
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

    if notas:
        soma_notas = 0
        for nota in notas:
            soma_notas += nota
        media = soma_notas / len(notas)
        print(f"A média aritmética das {n} notas é: {media:.2f}.")
    else:
        print("Nenhuma nota foi digitada.")
