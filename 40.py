def exercicio_40():
    dados_cidades = []
    num_cidades = 5
    print(f"Digite os dados para {num_cidades} cidades (código da cidade, número de veículos de passeio, número de acidentes com vítimas).")

    for i in range(num_cidades):
        while True:
            try:
                codigo_cidade = int(input(f"\nDigite o código da cidade {i+1}: "))
                num_veiculos = int(input(f"Digite o número de veículos de passeio para a cidade {codigo_cidade} (em 1999): "))
                num_acidentes = int(input(f"Digite o número de acidentes de trânsito com vítimas para a cidade {codigo_cidade} (em 1999): "))

                if codigo_cidade <= 0 or num_veiculos < 0 or num_acidentes < 0:
                    print("Os valores devem ser não negativos. O código da cidade deve ser positivo. Por favor, redigite.")
                    continue
                
                dados_cidades.append({
                    'codigo': codigo_cidade,
                    'veiculos': num_veiculos,
                    'acidentes': num_acidentes
                })
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite números inteiros.")
    
    if not dados_cidades:
        print("Nenhum dado de cidade foi inserido.")
        return

    maior_acidentes = {'codigo': None, 'acidentes': -1}
    menor_acidentes = {'codigo': None, 'acidentes': float('inf')}

    for cidade in dados_cidades:
        if cidade['acidentes'] > maior_acidentes['acidentes']:
            maior_acidentes = {'codigo': cidade['codigo'], 'acidentes': cidade['acidentes']}
        if cidade['acidentes'] < menor_acidentes['acidentes']:
            menor_acidentes = {'codigo': cidade['codigo'], 'acidentes': cidade['acidentes']}
    
    print(f"\nMaior índice de acidentes de trânsito: {maior_acidentes['acidentes']} na cidade {maior_acidentes['codigo']}.")
    print(f"Menor índice de acidentes de trânsito: {menor_acidentes['acidentes']} na cidade {menor_acidentes['codigo']}.")

    total_veiculos = 0
    for cidade in dados_cidades:
        total_veiculos += cidade['veiculos']
    media_veiculos = total_veiculos / num_cidades
    print(f"Média de veículos nas cinco cidades juntas: {media_veiculos:.2f}.")

    acidentes_menos_2000_veiculos = []
    for cidade in dados_cidades:
        if cidade['veiculos'] < 2000:
            acidentes_menos_2000_veiculos.append(cidade['acidentes'])
    
    if acidentes_menos_2000_veiculos:
        soma_acidentes_menor_2000 = 0
        for acidentes in acidentes_menos_2000_veiculos:
            soma_acidentes_menor_2000 += acidentes
        media_acidentes_menos_2000 = soma_acidentes_menor_2000 / len(acidentes_menos_2000_veiculos)
        print(f"Média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio: {media_acidentes_menos_2000:.2f}.")
    else:
        print("Nenhuma cidade com menos de 2.000 veículos encontrada.")
