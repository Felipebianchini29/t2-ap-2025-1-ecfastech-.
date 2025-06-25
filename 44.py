def exercicio_44():
    candidatos_nomes = {
        1: "José",
        2: "João",
        3: "Maria",
        4: "Pedro"
    }

    votos = {
        'candidato_1': 0,
        'candidato_2': 0,
        'candidato_3': 0,
        'candidato_4': 0,
        'nulo': 0,
        'branco': 0
    }
    total_votos_lancados = 0

    print("--- Eleição Presidencial ---")
    print("Códigos de Voto:")
    for codigo, nome in candidatos_nomes.items():
        print(f"{codigo} - {nome}")
    print("5 - Voto Nulo")
    print("6 - Voto em Branco")
    print("0 - Finalizar Votação")

    while True:
        try:
            voto = int(input("Digite seu voto: "))
            if voto == 0:
                break

            total_votos_lancados += 1

            if voto in [1, 2, 3, 4]:
                votos[f'candidato_{voto}'] += 1
            elif voto == 5:
                votos['nulo'] += 1
            elif voto == 6:
                votos['branco'] += 1
            else:
                print("Voto inválido. Por favor, digite 1, 2, 3, 4, 5, 6, ou 0 para finalizar.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    print("\n--- Resultados da Eleição ---")
    print("Total de Votos:")
    for codigo, nome in candidatos_nomes.items():
        print(f"  {nome}: {votos[f'candidato_{codigo}']} votos.")
    print(f"Total de Votos Nulos: {votos['nulo']}.")
    print(f"Total de Votos em Branco: {votos['branco']}.")

    if total_votos_lancados > 0:
        percentual_nulos = (votos['nulo'] / total_votos_lancados) * 100
        percentual_brancos = (votos['branco'] / total_votos_lancados) * 100
        print(f"Percentual de Votos Nulos: {percentual_nulos:.2f}%.")
        print(f"Percentual de Votos em Branco: {percentual_brancos:.2f}%.")
    else:
        print("Nenhum voto foi computado.")
