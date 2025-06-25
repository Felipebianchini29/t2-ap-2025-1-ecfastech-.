def exercicio_35():
    def e_primo(numero):
        if numero <= 1:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True

    while True:
        try:
            n = int(input("Digite um número inteiro para gerar uma lista de números primos até ele: "))
            if n > 1:
                break
            else:
                print("Por favor, digite um número inteiro maior que 1.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    numeros_primos = []
    for num in range(1, n + 1):
        if e_primo(num):
            numeros_primos.append(num)
    print(f"Números primos entre 1 e {n}: {numeros_primos}.")
