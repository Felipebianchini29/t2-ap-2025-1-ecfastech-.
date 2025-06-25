def exercicio_50():
    while True:
        try:
            n = int(input("Digite o número de termos (N) para H: "))
            if n > 0:
                break
            else:
                print("Por favor, digite um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    
    valor_h = 0
    for i in range(1, n + 1):
        valor_h += 1 / i
    
    print(f"O valor de H com {n} termos é: {valor_h:.4f}.")