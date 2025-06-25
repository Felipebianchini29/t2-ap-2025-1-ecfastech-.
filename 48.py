def exercicio_48():
    while True:
        num_str = input("Digite um número inteiro positivo para inverter: ")
        e_digito = True
        for char in num_str:
            if not ('0' <= char <= '9'):
                e_digito = False
                break
        
        if e_digito and len(num_str) > 0:
            num_int = int(num_str)
            if num_int >= 0:
                break
            else:
                print("Entrada inválida. Por favor, digite um número inteiro positivo.")
        else:
            print("Entrada inválida. Por favor, digite um número inteiro positivo.")
    
    inverted_num_list = []
    for i in range(len(num_str) - 1, -1, -1):
        inverted_num_list.append(num_str[i])
    inverted_num_str = "".join(inverted_num_list)
    
    print(f"{num_str} => {inverted_num_str}")