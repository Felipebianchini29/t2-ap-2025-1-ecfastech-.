def exercicio_34():
    while True:
        try:
            num = int(input("Digite um número inteiro para determinar se ele é ou não primo: "))
            if num >= 0:
                break
            else:
                print("Por favor, digite um número inteiro não negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    if num <= 1:
        print(f"{num} não é um número primo.")
    else:
        e_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                e_primo = False
                break
        if e_primo:
            print(f"{num} é um número primo.")
        else:
            print(f"{num} não é um número primo.")