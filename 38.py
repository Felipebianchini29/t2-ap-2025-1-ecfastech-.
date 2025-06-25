def exercicio_38():
    while True:
        try:
            salario_inicial = float(input("Digite o salário inicial do funcionário (ex: 1000 para R$ 1.000,00): "))
            if salario_inicial > 0:
                break
            else:
                print("O salário inicial deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    ano_atual = 2025 
    
    salario = salario_inicial
    
    if 1995 <= ano_atual:
        if ano_atual == 1995:
            pass
        elif ano_atual == 1996:
            salario *= (1 + 0.015)
        elif ano_atual > 1996:
            salario_1996 = salario_inicial * (1 + 0.015)
            salario = salario_1996
            percentual_aumento = 0.015 * 2 

            for ano in range(1997, ano_atual + 1):
                salario *= (1 + percentual_aumento)
                percentual_aumento *= 2 
    
    print(f"O salário atual do funcionário em {ano_atual} é: R$ {salario:.2f}.")
