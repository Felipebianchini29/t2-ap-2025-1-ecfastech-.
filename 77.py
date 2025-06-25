def exercicio_77():
    def combinar_listas(*listas):
        lista_combinada = []
        for lst in listas:
            for item in lst:
                lista_combinada.append(item)
        return lista_combinada

    todas_listas_usuario = []
    print("Digite elementos para as listas. Digite 'fim' para finalizar uma lista, depois enter para adicionar outra lista.")
    print("Digite 'fim_geral' quando terminar todas as listas.")
    
    numero_lista = 1
    while True:
        lista_atual = []
        print(f"\n--- Digite elementos para a Lista {numero_lista} ---")
        while True:
            elemento_entrada = input(f"Digite um elemento para a lista {numero_lista} (ou 'fim' para finalizar esta lista): ").strip()
            if elemento_entrada.lower() == 'fim':
                break
            lista_atual.append(elemento_entrada)
        
        todas_listas_usuario.append(lista_atual)
        
        adicionar_outra = input("Adicionar outra lista? (sim/não, ou 'fim_geral'): ").lower()
        if adicionar_outra == 'fim_geral':
            break
        elif adicionar_outra != 'sim':
            break
        numero_lista += 1

    if todas_listas_usuario:
        lista_final_combinada = combinar_listas(*todas_listas_usuario)
        print(f"\nTodas as listas inseridas pelo usuário: {todas_listas_usuario}")
        print(f"Listas combinadas do usuário: {lista_final_combinada}")
    else:
        print("Nenhuma lista foi inserida pelo usuário.")
