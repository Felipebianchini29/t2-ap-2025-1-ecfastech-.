def exercicio_53():
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
    
    while True:
        try:
            elemento_alvo = float(input("Digite o elemento para contar: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    contagem = 0
    for r in range(linhas):
        for c in range(colunas):
            if matriz[r][c] == elemento_alvo:
                contagem += 1
    
    print("\n--- Matriz ---")
    for linha in matriz:
        print(linha)
    
    print(f"O elemento {elemento_alvo} aparece {contagem} vez(es) na matriz.")
