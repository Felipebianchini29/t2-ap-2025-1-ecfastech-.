def exercicio_72():
    def converter_temperatura(valor, unidade_origem, unidade_destino):
        unidades_validas = ['C', 'F', 'K']
        e_unidade_valida_origem = False
        for u in unidades_validas:
            if unidade_origem == u:
                e_unidade_valida_origem = True
                break
        
        e_unidade_valida_destino = False
        for u in unidades_validas:
            if unidade_destino == u:
                e_unidade_valida_destino = True
                break

        if not e_unidade_valida_origem or not e_unidade_valida_destino:
            return "Erro: Unidades inválidas. Por favor, use 'C', 'F' ou 'K'."

        if unidade_origem == unidade_destino:
            return valor

        celsius = 0.0
        if unidade_origem == 'F':
            celsius = (valor - 32) / 1.8
        elif unidade_origem == 'K':
            celsius = valor - 273.15
        else:
            celsius = valor
        
        if unidade_destino == 'F':
            return celsius * 1.8 + 32
        elif unidade_destino == 'K':
            return celsius + 273.15
        else:
            return celsius

    while True:
        try:
            valor = float(input("Digite o valor da temperatura: "))
            unidade_origem = input("Digite a unidade original (C, F, K): ").upper()
            unidade_destino = input("Digite a unidade de destino (C, F, K): ").upper()
            
            valor_convertido = converter_temperatura(valor, unidade_origem, unidade_destino)
            
            if isinstance(valor_convertido, str) and "Erro" in valor_convertido:
                print(valor_convertido)
            else:
                print(f"{valor:.2f} {unidade_origem} é {valor_convertido:.2f} {unidade_destino}.")
            
            outra_conversao = input("Realizar outra conversão? (sim/não): ").lower()
            if outra_conversao != 'sim':
                break

        except ValueError:
            print("Entrada inválida para o valor da temperatura. Por favor, digite um número.")

# exercicio_72()

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
