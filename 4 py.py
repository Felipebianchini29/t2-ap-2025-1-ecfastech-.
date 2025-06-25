def exercicio_04():
    populacao_a = 80000
    taxa_crescimento_a = 0.03
    populacao_b = 200000
    taxa_crescimento_b = 0.015
    anos = 0

    while populacao_a < populacao_b:
        populacao_a *= (1 + taxa_crescimento_a)
        populacao_b *= (1 + taxa_crescimento_b)
        anos += 1
    print(f"Serão necessários {anos} anos para que a população A ultrapasse ou iguale a população B.")
    print(f"População A final: {populacao_a:.2f}")
    print(f"População B final: {populacao_b:.2f}")