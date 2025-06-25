def exercicio_26():
    while True:
        try:
            total_eleitores = int(input("Digite o número total de eleitores: "))
            if total_eleitores >= 0:
                break
            else:
                print("O número de eleitores não pode ser negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    votos = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        'nulo': 0,
        'branco': 0
    }
    
    print("\n--- Eleição Presidencial ---")
    print("Códigos de Voto:")
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    print("4 - Candidato 4")
    print("5 - Voto Nulo")
    print("6 - Voto em Branco")
    print("0 - Finalizar Votação")

    for i in range(total_eleitores):
        while True:
            try:
                voto = int(input(f"Eleitor {i+1}, digite seu voto: "))
                if voto == 0:
                    break 
                elif voto in [1, 2, 3, 4]:
                    votos[voto] += 1
                    break
                elif voto == 5:
                    votos['nulo'] += 1
                    break
                elif voto == 6:
                    votos['branco'] += 1
                    break
                else:
                    print("Voto inválido. Por favor, digite 1, 2, 3, 4, 5, 6, ou 0 para finalizar.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")
        if voto == 0:
            break

    total_votos_validos = votos[1] + votos[2] + votos[3] + votos[4]
    total_votos_lancados = total_votos_validos + votos['nulo'] + votos['branco']

    print("\n--- Resultados da Eleição ---")
    print("Total de Votos:")
    for cand_num in [1, 2, 3, 4]:
        print(f"  Candidato {cand_num}: {votos[cand_num]} votos.")
    print(f"Total de Votos Nulos: {votos['nulo']}.")
    print(f"Total de Votos em Branco: {votos['branco']}.")

    if total_votos_lancados > 0:
        percentual_nulos = (votos['nulo'] / total_votos_lancados) * 100
        percentual_brancos = (votos['branco'] / total_votos_lancados) * 100
        print(f"Percentual de Votos Nulos: {percentual_nulos:.2f}%.")
        print(f"Percentual de Votos em Branco: {percentual_brancos:.2f}%.")
    else:
        print("Nenhum voto foi computado.")
