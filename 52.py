def exercicio_52():
    while True:
        try:
            tamanho = int(input("Digite o tamanho da matriz quadrada (ex: 3 para 3x3): "))
            if tamanho > 0:
                break
            else:
                print("O tamanho da matriz deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    matriz = []
    print(f"Digite os elementos para uma matriz {tamanho}x{tamanho}, linha por linha:")
    for r in range(tamanho):
        linha = []
        for c in range(tamanho):
            while True:
                try:
                    elemento = float(input(f"Digite o elemento na posição [{r+1}][{c+1}]: "))
                    linha.append(elemento)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
        matriz.append(linha)

    soma_diagonal_principal = 0
    soma_diagonal_secundaria = 0

    for i in range(tamanho):
        soma_diagonal_principal += matriz[i][i]
        soma_diagonal_secundaria += matriz[i][tamanho - 1 - i]
    
    print("\n--- Matriz ---")
    for linha in matriz:
        print(linha)
    
    print(f"\nSoma dos elementos da diagonal principal: {soma_diagonal_principal:.2f}.")
    print(f"Soma dos elementos da diagonal secundária: {soma_diagonal_secundaria:.2f}.")

