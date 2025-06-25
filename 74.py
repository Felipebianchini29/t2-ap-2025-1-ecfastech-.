def exercicio_75():
    def sao_anagramas(palavra1, palavra2):
        lista_caracteres1 = []
        for char in palavra1:
            if ('a' <= char.lower() <= 'z') or ('0' <= char <= '9'):
                lista_caracteres1.append(char.lower())

        lista_caracteres2 = []
        for char in palavra2:
            if ('a' <= char.lower() <= 'z') or ('0' <= char <= '9'):
                lista_caracteres2.append(char.lower())
        
        # Implementação manual de um bubble sort para ordenar
        n1 = len(lista_caracteres1)
        for i in range(n1 - 1):
            for j in range(0, n1 - i - 1):
                if lista_caracteres1[j] > lista_caracteres1[j+1]:
                    lista_caracteres1[j], lista_caracteres1[j+1] = lista_caracteres1[j+1], lista_caracteres1[j]
        
        n2 = len(lista_caracteres2)
        for i in range(n2 - 1):
            for j in range(0, n2 - i - 1):
                if lista_caracteres2[j] > lista_caracteres2[j+1]:
                    lista_caracteres2[j], lista_caracteres2[j+1] = lista_caracteres2[j+1], lista_caracteres2[j]
        
        e_anagrama = False
        if len(lista_caracteres1) == len(lista_caracteres2):
            todos_iguais = True
            for i in range(len(lista_caracteres1)):
                if lista_caracteres1[i] != lista_caracteres2[i]:
                    todos_iguais = False
                    break
            if todos_iguais:
                e_anagrama = True
        
        return e_anagrama

    while True:
        palavra1 = input("Digite a primeira string: ")
        palavra2 = input("Digite a segunda string: ")
        
        sao_anagramas_resultado = sao_anagramas(palavra1, palavra2)
        print(f"'{palavra1}' e '{palavra2}' são anagramas: {sao_anagramas_resultado}.")

        outra_verificacao = input("Verificar outro par? (sim/não): ").lower()
        if outra_verificacao != 'sim':
            break