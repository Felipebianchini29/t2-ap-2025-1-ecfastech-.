def exercicio_07():
    numeros = []
    for i in range(5):
        while True:
            try:
                num = float(input(f"Digite o número {i+1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
    
    if numeros:
        maior_numero = numeros[0]
        for num in numeros:
            if num > maior_numero:
                maior_numero = num
        print(f"O maior número é: {maior_numero}.")
    else:
        print("Nenhum número foi digitado.")