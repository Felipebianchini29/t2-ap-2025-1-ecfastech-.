def exercicio_03():
    while True:
        nome = input("Digite seu nome (mais de 3 caracteres): ")
        if len(nome) > 3:
            break
        else:
            print("O nome deve ter mais de 3 caracteres.")

    while True:
        try:
            idade = int(input("Digite sua idade (entre 0 e 150): "))
            if 0 <= idade <= 150:
                break
            else:
                print("A idade deve estar entre 0 e 150.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a idade.")

    while True:
        try:
            salario = float(input("Digite seu salário (maior que zero): R$ "))
            if salario > 0:
                break
            else:
                print("O salário deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o salário.")

    while True:
        sexo = input("Digite seu sexo ('f' para feminino, 'm' para masculino): ").lower()
        if sexo in ['f', 'm']:
            break
        else:
            print("Entrada inválida. Por favor, digite 'f' ou 'm'.")

    while True:
        estado_civil = input("Digite seu estado civil ('s', 'c', 'v', 'd'): ").lower()
        if estado_civil in ['s', 'c', 'v', 'd']:
            break
        else:
            print("Entrada inválida. Por favor, digite 's', 'c', 'v' ou 'd'.")

    print("\nInformações validadas com sucesso:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: {salario:.2f}")
    print(f"Sexo: {sexo}")
    print(f"Estado Civil: {estado_civil}")