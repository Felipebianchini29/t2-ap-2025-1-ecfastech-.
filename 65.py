def exercicio_65():
    texto_completo = input("Digite a string completa: ")
    
    while True:
        try:
            indice_inicio = int(input("Digite o índice de início: "))
            indice_fim = int(input("Digite o índice de fim: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros para os índices.")
    
    tamanho_texto = len(texto_completo)

    if indice_inicio < 0:
        indice_inicio_ajustado = 0
    elif indice_inicio > tamanho_texto:
        indice_inicio_ajustado = tamanho_texto
    else:
        indice_inicio_ajustado = indice_inicio

    if indice_fim < 0:
        indice_fim_ajustado = 0
    elif indice_fim > tamanho_texto:
        indice_fim_ajustado = tamanho_texto
    else:
        indice_fim_ajustado = indice_fim

    if indice_inicio_ajustado > indice_fim_ajustado:
        temp = indice_inicio_ajustado
        indice_inicio_ajustado = indice_fim_ajustado
        indice_fim_ajustado = temp

    substring = ""
    i = indice_inicio_ajustado
    while i < indice_fim_ajustado:
        substring += texto_completo[i]
        i += 1
    
    print(f"String original: \"{texto_completo}\"")
    print(f"Índice de início: {indice_inicio}, Índice de fim: {indice_fim}")
    print(f"Substring extraída: \"{substring}\"")
    if indice_inicio_ajustado != indice_inicio or indice_fim_ajustado != indice_fim:
        print(f"(Índices ajustados para {indice_inicio_ajustado} e {indice_fim_ajustado} devido a estarem fora dos limites.)")
