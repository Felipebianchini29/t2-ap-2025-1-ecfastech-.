def exercicio_57():
    linhas = 0
    colunas_da_primeira_linha = 0
    
    while True:
        try:
            linhas = int(input("Digite o número de linhas para a matriz: "))
            if linhas >= 0:
                break
            else:
                print("O número de linhas não pode ser negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    
    if linhas == 0:
        print("É matriz quadrada: True")
        print("Todas as linhas têm o mesmo número de colunas: True")
        return

    matriz = []
    print(f"Digite os elementos para uma matriz com {linhas} linhas. Digite as colunas para cada linha:")
    for r in range(linhas):
        while True:
            linha_str = input(f"Digite os elementos para a linha {r+1} separados por espaços: ")
            elementos_str = linha_str.split()
            linha_elementos = []
            e_valido_linha = True
            for elem_str in elementos_str:
                try:
                    linha_elementos.append(float(elem_str))
                except ValueError:
                    print("Entrada inválida. Por favor, digite números separados por espaços.")
                    e_valido_linha = False
                    break
            if e_valido_linha:
                matriz.append(linha_elementos)
                break

    e_matriz_quadrada = False
    if len(matriz) > 0:
        colunas_da_primeira_linha = len(matriz[0])
        if len(matriz) == colunas_da_primeira_linha:
            e_matriz_quadrada = True

    todas_linhas_mesmo_num_colunas = True
    if len(matriz) > 1:
        for r in range(1, len(matriz)):
            if len(matriz[r]) != colunas_da_primeira_linha:
                todas_linhas_mesmo_num_colunas = False
                break
    
    print("\n--- Matriz ---")
    for linha in matriz:
        print(linha)
    
    print(f"É matriz quadrada: {e_matriz_quadrada}.")
    print(f"Todas as linhas têm o mesmo número de colunas: {todas_linhas_mesmo_num_colunas}.")
