def exercicio_60():
    string_original = input("Digite uma string para inverter: ")
    lista_caracteres = []
    for char in string_original:
        lista_caracteres.append(char)
    
    string_invertida_lista = []
    for i in range(len(lista_caracteres) - 1, -1, -1):
        string_invertida_lista.append(lista_caracteres[i])
    string_invertida = "".join(string_invertida_lista)
    
    print(f"String original: \"{string_original}\"")
    print(f"String invertida: \"{string_invertida}\"")