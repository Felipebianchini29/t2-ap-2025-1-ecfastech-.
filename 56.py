def exercicio_56():
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
    for r in range(linhas):
        linha = []
        for c in range(colunas):
            linha.append(r * c)
        matriz.append(linha)
    
    print("\n--- Matriz Gerada (elemento[i][j] = i*j) ---")
    for linha in matriz:
        print(linha)

