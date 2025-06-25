def exercicio_23():
    def e_primo_com_divisoes(numero):
        if numero <= 1:
            return False, 0
        divisoes = 0
        for i in range(2, int(numero**0.5) + 1):
            divisoes += 1
            if numero % i == 0:
                return False, divisoes
        return True, divisoes

    while True:
        try:
            n = int(input("Digite um número inteiro N para encontrar os primos entre 1 e N: "))
            if n > 1:
                break
            else:
                print("Por favor, digite um número inteiro maior que 1.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    numeros_primos = []
    total_divisoes = 0
    print(f"Números primos entre 1 e {n}:")
    for num in range(1, n + 1):
        e_p, contagem_divisoes = e_primo_com_divisoes(num)
        total_divisoes += contagem_divisoes
        if e_p:
            numeros_primos.append(num)
            print(num, end=" ")
    print()
    print(f"Total de números primos encontrados: {len(numeros_primos)}")
    print(f"Total de divisões executadas para encontrar os primos: {total_divisoes}.")
