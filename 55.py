def exercicio_55():
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
    
    if not matriz or not matriz[0]:
        print("A matriz está vazia. Não é possível encontrar o menor/maior elemento.")
        return

    menor_elemento = matriz[0][0]
    maior_elemento = matriz[0][0]

    for r in range(linhas):
        for c in range(colunas):
            if matriz[r][c] < menor_elemento:
                menor_elemento = matriz[r][c]
            if matriz[r][c] > maior_elemento:
                maior_elemento = matriz[r][c]
    
    print("\n--- Matriz ---")
    for linha in matriz:
        print(linha)
    
    print(f"\nMenor elemento na matriz: {menor_elemento:.2f}.")
    print(f"Maior elemento na matriz: {maior_elemento:.2f}.")
