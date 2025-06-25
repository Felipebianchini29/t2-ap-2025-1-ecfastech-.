def exercicio_16():
    serie_fib = []
    a, b = 0, 1
    while a <= 500:
        serie_fib.append(a)
        a, b = b, a + b
    print(f"Série de Fibonacci até que o valor seja maior que 500: {serie_fib}.")
