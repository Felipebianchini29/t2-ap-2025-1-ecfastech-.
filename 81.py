def exercicio_81():
    def anexar_conteudo(nome_arquivo, conteudo_extra):
        try:
            f = open(nome_arquivo, 'a')
            f.write(conteudo_extra)
            f.close()
            print(f"Conteúdo adicionado com sucesso ao final de '{nome_arquivo}'.")
        except IOError as e:
            print(f"Erro ao adicionar conteúdo ao arquivo '{nome_arquivo}': {e}")
    
    nome_arquivo = input("Digite o nome do arquivo para adicionar conteúdo (ex: dados.txt): ")
    conteudo_extra = input("Digite o conteúdo extra para adicionar ao arquivo: ")
    
    anexar_conteudo(nome_arquivo, conteudo_extra)