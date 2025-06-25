def exercicio_08():
    numeros = []
    soma_total = 0
    for i in range(5):
        while True:
            try:
                num = float(input(f"Digite o número {i+1}: "))
                numeros.append(num)
                soma_total += num
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
    
    if numeros:
        media = soma_total / len(numeros)
        print(f"A soma dos números é: {soma_total}.")
        print(f"A média dos números é: {media:.2f}.")
    else:
        print("Nenhum número foi digitado.")
