def exercicio_46():
    while True:
        nome_atleta = input("\nDigite o nome do atleta (deixe em branco para finalizar): ").strip()
        if not nome_atleta:
            break

        saltos = []
        print(f"Digite as 5 distâncias de salto para {nome_atleta}:")
        for i in range(5):
            while True:
                try:
                    distancia = float(input(f"Salto {i+1} (em metros): "))
                    if distancia >= 0:
                        saltos.append(distancia)
                        break
                    else:
                        print("A distância não pode ser negativa.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
        
        if len(saltos) != 5: 
            print("Não foram inseridos 5 saltos válidos. Pulando este atleta.")
            continue

        melhor_salto = saltos[0]
        for salto in saltos:
            if salto > melhor_salto:
                melhor_salto = salto

        pior_salto = saltos[0]
        for salto in saltos:
            if salto < pior_salto:
                pior_salto = salto

        saltos_para_media = []
        saltos_temp = list(saltos)

        removido_melhor = False
        removido_pior = False

        for salto_valor in saltos_temp:
            if salto_valor == melhor_salto and not removido_melhor:
                removido_melhor = True
            elif salto_valor == pior_salto and not removido_pior:
                removido_pior = True
            else:
                saltos_para_media.append(salto_valor)
        
        # Para lidar com casos onde o melhor/pior podem ser repetidos e serem um dos 3 restantes
        # Melhor maneira de garantir a remoção de *apenas um* melhor e *apenas um* pior
        saltos_para_media = list(saltos)
        
        if melhor_salto in saltos_para_media:
            saltos_para_media.remove(melhor_salto)
        
        if pior_salto in saltos_para_media:
            # Precisa garantir que se melhor_salto == pior_salto (lista com valores iguais),
            # remove apenas uma vez.
            if len(saltos_para_media) == len(saltos) - 1 and melhor_salto == pior_salto:
                pass # Já removeu um, se eram o mesmo, o outro já foi o 'melhor'
            else:
                saltos_para_media.remove(pior_salto)


        if len(saltos_para_media) > 0:
            soma_restantes = 0
            for s in saltos_para_media:
                soma_restantes += s
            media_restantes = soma_restantes / len(saltos_para_media)
        else:
            media_restantes = 0

        print(f"\nAtleta: {nome_atleta}")
        print(f"Primeiro Salto: {saltos[0]:.1f} m")
        print(f"Segundo Salto: {saltos[1]:.1f} m")
        print(f"Terceiro Salto: {saltos[2]:.1f} m")
        print(f"Quarto Salto: {saltos[3]:.1f} m")
        print(f"Quinto Salto: {saltos[4]:.1f} m")
        print(f"\nMelhor salto: {melhor_salto:.1f} m")
        print(f"Pior salto: {pior_salto:.1f} m")
        print(f"Média dos demais saltos: {media_restantes:.1f} m")
        print(f"\nResultado final:")
        print(f"{nome_atleta}: {media_restantes:.1f} m")
