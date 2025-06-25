def exercicio_62():
    string_entrada = input("Digite uma string para verificar se é um palíndromo: ")
    
    caracteres_alfanumericos = []
    for char in string_entrada:
        if ('a' <= char.lower() <= 'z') or ('0' <= char <= '9'):
            caracteres_alfanumericos.append(char.lower())
    
    string_normalizada = ""
    for char in caracteres_alfanumericos:
        string_normalizada += char

    string_invertida_lista = []
    for i in range(len(string_normalizada) - 1, -1, -1):
        string_invertida_lista.append(string_normalizada[i])
    string_invertida = "".join(string_invertida_lista)
    
    e_palindromo = False
    if string_normalizada == string_invertida:
        e_palindromo = True
    
    print(f"A string \"{string_entrada}\" é um palíndromo: {e_palindromo}.")