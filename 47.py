def exercicio_47():
    while True:
        nome_ginasta = input("\nDigite o nome do ginasta (deixe em branco para finalizar): ").strip()
        if not nome_ginasta:
            break

        notas = []
        print(f"Digite as 7 notas para {nome_ginasta}:")
        for i in range(7):
            while True:
                try:
                    nota = float(input(f"Nota {i+1}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("A nota deve ser entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
        
        if len(notas) != 7:
            print("Não foram inseridas 7 notas válidas. Pulando este ginasta.")
            continue

        melhor_nota = notas[0]
        for n in notas:
            if n > melhor_nota:
                melhor_nota = n

        pior_nota = notas[0]
        for n in notas:
            if n < pior_nota:
                pior_nota = n

        notas_para_media = list(notas)

        if melhor_nota in notas_para_media:
            notas_para_media.remove(melhor_nota)
        
        if pior_nota in notas_para_media:
            if len(notas_para_media) == len(notas) - 1 and melhor_nota == pior_nota:
                pass
            else:
                notas_para_media.remove(pior_nota)

        if len(notas_para_media) > 0:
            soma_restantes = 0
            for n_restante in notas_para_media:
                soma_restantes += n_restante
            media_restantes = soma_restantes / len(notas_para_media)
        else:
            media_restantes = 0

        print(f"\nAtleta: {nome_ginasta}")
        for nota_item in notas:
            print(f"Nota: {nota_item:.1f}")
        
        print(f"\nResultado final:")
        print(f"Atleta: {nome_ginasta}")
        print(f"Melhor nota: {melhor_nota:.1f}")
        print(f"Pior nota: {pior_nota:.1f}")
        print(f"Média: {media_restantes:.2f}")
