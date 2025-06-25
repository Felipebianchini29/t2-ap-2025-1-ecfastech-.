def exercicio_86():
    def criar_csv_exemplo():
        try:
            f = open("exemplo.csv", "w")
            f.write("Nome,Idade,Cidade\n")
            f.write("Alice,30,Nova Iorque\n")
            f.write("Bob,24,Londres\n")
            f.write("Carlos,35,Paris\n")
            f.close()
            print("Arquivo 'exemplo.csv' criado para teste.")
        except IOError as e:
            print(f"Erro ao criar 'exemplo.csv': {e}")
    # criar_csv_exemplo()

    def ler_csv_simples(nome_arquivo):
        dados = []
        try:
            f = open(nome_arquivo, 'r')
            linhas = []
            for linha in f:
                linhas.append(linha)
            f.close()

            if len(linhas) > 0:
                tem_cabecalho = input("O arquivo CSV tem uma linha de cabeçalho (sim/não)? ").lower()
                indice_inicio = 0
                if tem_cabecalho == 'sim':
                    indice_inicio = 1
                
                i = indice_inicio
                while i < len(linhas):
                    linha_limpa = ""
                    for char in linhas[i]:
                        if char != '\n':
                            linha_limpa += char
                    
                    if len(linha_limpa) > 0:
                        valores = []
                        valor_atual = []
                        j = 0
                        while j < len(linha_limpa):
                            if linha_limpa[j] == ',':
                                valores.append("".join(valor_atual))
                                valor_atual = []
                            else:
                                valor_atual.append(linha_limpa[j])
                            j += 1
                        valores.append("".join(valor_atual)) # Adiciona o último valor
                        dados.append(valores)
                    i += 1
            return dados
        except FileNotFoundError:
            print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
            return []
        except IOError as e:
            print(f"Ocorreu um erro ao ler o CSV: {e}")
            return []
    
    nome_arquivo = input("Digite o nome do arquivo CSV (ex: exemplo.csv): ")
    dados_csv = ler_csv_simples(nome_arquivo)
    if dados_csv:
        print(f"\nConteúdo de '{nome_arquivo}' (excluindo cabeçalho, se houver):")
        for linha in dados_csv:
            print(linha)
