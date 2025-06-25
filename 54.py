def exercicio_54():
    linhas = 0
    colunas = 0
    while True:
        try:
            linhas = int(input("Digite o número de linhas para a matriz: "))
            colunas = int(input("Digite o número de colunas para a matriz: "))
            if linhas > 0 and colunas > 0:
                break
            else:
                print("O número de linhas e colunas deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros.")

    matriz = []
    print(f"Digite os elementos para uma matriz {linhas}x{colunas}:")
    for r in range(linhas):
        linha = []
        for c in range(colunas):
            while True:
                try:
                    elemento = float(input(f"Digite o elemento na posição [{r+1}][{c+1}]: "))
                    linha.append(elemento)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
        matriz.append(linha)

    matriz_transposta = []
    for c in range(colunas):
        nova_linha = []
        for r in range(linhas):
            nova_linha.append(matriz[r][c])
        matriz_transposta.append(nova_linha)
    
    print("\n--- Matriz Original ---")
    for linha in matriz:
        print(linha)
    
    print("\n--- Matriz Transposta ---")
    for linha in matriz_transposta:
        print(linha)