def exercicio_05():
    while True:
        try:
            populacao_a = float(input("Digite a população inicial do país A: "))
            taxa_crescimento_a = float(input("Digite a taxa de crescimento anual do país A (ex: 0.03 para 3%): "))
            populacao_b = float(input("Digite a população inicial do país B: "))
            taxa_crescimento_b = float(input("Digite a taxa de crescimento anual do país B (ex: 0.015 para 1.5%): "))

            if populacao_a <= 0 or populacao_b <= 0 or taxa_crescimento_a < 0 or taxa_crescimento_b < 0:
                print("As populações devem ser positivas e as taxas não negativas. Tente novamente.")
                continue

            anos = 0
            if populacao_a >= populacao_b and taxa_crescimento_a <= taxa_crescimento_b:
                print("A população A nunca ultrapassará ou igualará a população B com essas taxas.")
                print(f"População A inicial: {populacao_a:.2f}, Taxa A: {taxa_crescimento_a * 100:.2f}%")
                print(f"População B inicial: {populacao_b:.2f}, Taxa B: {taxa_crescimento_b * 100:.2f}%")
            else:
                pop_a_atual = populacao_a
                pop_b_atual = populacao_b
                while pop_a_atual < pop_b_atual:
                    pop_a_atual *= (1 + taxa_crescimento_a)
                    pop_b_atual *= (1 + taxa_crescimento_b)
                    anos += 1
                print(f"Serão necessários {anos} anos para que a população A ultrapasse ou iguale a população B.")
                print(f"População A final: {pop_a_atual:.2f}")
                print(f"População B final: {pop_b_atual:.2f}")

        except ValueError:
            print("Entrada inválida. Por favor, digite números para as populações e taxas.")

        repetir = input("Deseja realizar outro cálculo? (sim/não): ").lower()
        if repetir != 'sim':
            break