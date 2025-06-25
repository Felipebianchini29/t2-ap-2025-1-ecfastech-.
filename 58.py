def exercicio_58():
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
    
    matriz_invertida = []
    for i in range(len(matriz) - 1, -1, -1):
        matriz_invertida.append(matriz[i])
    
    print("\n--- Matriz Original ---")
    for linha in matriz:
        print(linha)
    
    print("\n--- Matriz Invertida (linhas invertidas) ---")
    for linha in matriz_invertida:
        print(linha)
