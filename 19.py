def exercicio_19():
    numeros = []
    while True:
        try:
            n = int(input("Digite a quantidade de números (N): "))
            if n > 0:
                break
            else:
                print("N deve ser um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    for i in range(n):
        while True:
            try:
                num = float(input(f"Digite o número {i+1} (entre 0 e 1000): "))
                if 0 <= num <= 1000:
                    numeros.append(num)
                    break
                else:
                    print("O número deve estar entre 0 e 1000.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

    if numeros:
        menor_valor = numeros[0]
        maior_valor = numeros[0]
        soma_valores = 0
        for num in numeros:
            if num < menor_valor:
                menor_valor = num
            if num > maior_valor:
                maior_valor = num
            soma_valores += num
        print(f"Menor valor: {menor_valor}.")
        print(f"Maior valor: {maior_valor}.")
        print(f"Soma dos valores: {soma_valores}.")
    else:
        print("Nenhum número válido foi digitado.")