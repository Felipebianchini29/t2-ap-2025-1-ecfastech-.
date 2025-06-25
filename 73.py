def exercicio_73():
    def filtrar_numeros(lista, tipo):
        lista_filtrada = []
        if tipo == 'pares':
            for num in lista:
                if num % 2 == 0:
                    lista_filtrada.append(num)
        elif tipo == 'impares':
            for num in lista:
                if num % 2 != 0:
                    lista_filtrada.append(num)
        elif tipo == 'positivos':
            for num in lista:
                if num > 0:
                    lista_filtrada.append(num)
        elif tipo == 'negativos':
            for num in lista:
                if num < 0:
                    lista_filtrada.append(num)
        else:
            print("Aviso: Tipo inválido especificado. Retornando uma lista vazia.")
            return []
        return lista_filtrada

    minha_lista = []
    print("Digite números para a lista (digite 'fim' para finalizar):")
    while True:
        entrada_num = input("Digite um número: ")
        if entrada_num.lower() == 'fim':
            break
        try:
            minha_lista.append(float(entrada_num))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'fim'.")
    
    if not minha_lista:
        print("Nenhum número foi inserido.")
        return

    while True:
        tipo_filtro = input("Digite o tipo de filtro ('pares', 'impares', 'positivos', 'negativos'): ").lower()
        
        lista_resultado = filtrar_numeros(minha_lista, tipo_filtro)
        print(f"Lista original: {minha_lista}")
        print(f"Lista filtrada ({tipo_filtro}): {lista_resultado}")

        outro_filtro = input("Aplicar outro filtro? (sim/não): ").lower()
        if outro_filtro != 'sim':
            break