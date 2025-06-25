def exercicio_80():
    def escrever_novo_arquivo(nome_arquivo, conteudo):
        try:
            f = open(nome_arquivo, 'w')
            f.write(conteudo)
            f.close()
            print(f"Arquivo '{nome_arquivo}' criado/sobrescrito com sucesso com o conteúdo fornecido.")
        except IOError as e:
            print(f"Erro ao escrever no arquivo '{nome_arquivo}': {e}")
    
    nome_arquivo = input("Digite o nome do arquivo para criar/sobrescrever: ")
    conteudo_para_escrever = input("Digite o conteúdo para escrever no arquivo: ")
    
    escrever_novo_arquivo(nome_arquivo, conteudo_para_escrever)
