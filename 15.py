def exercicio_15():
    while True:
        try:
            n = int(input("Digite o número de termos para a série de Fibonacci: "))
            if n > 0:
                break
            else:
                print("Por favor, digite um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    serie_fib = []
    a, b = 1, 1
    for _ in range(n):
        serie_fib.append(a)
        a, b = b, a + b
    print(f"Série de Fibonacci até o {n}-ésimo termo: {serie_fib}.")