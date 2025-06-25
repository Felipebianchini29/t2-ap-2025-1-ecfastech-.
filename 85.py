def exercicio_85():
    def filtrar_linhas(nome_arquivo_origem, nome_arquivo_destino, palavra_chave):
        try:
            f_origem = open(nome_arquivo_origem, 'r')
            f_destino = open(nome_arquivo_destino, 'w')
            
            for linha in f_origem:
                linha_lower = ""
                for char in linha:
                    if 'A' <= char <= 'Z':
                        linha_lower += chr(ord(char) + 32) # Converte para minúscula manualmente
                    else:
                        linha_lower += char

                palavra_chave_lower = ""
                for char in palavra_chave:
                    if 'A' <= char <= 'Z':
                        palavra_chave_lower += chr(ord(char) + 32)
                    else:
                        palavra_chave_lower += char
                
                contem_palavra = False
                i = 0
                while i <= len(linha_lower) - len(palavra_chave_lower):
                    j = 0
                    match = True
                    while j < len(palavra_chave_lower):
                        if linha_lower[i+j] != palavra_chave_lower[j]:
                            match = False
                            break
                        j += 1
                    if match:
                        contem_palavra = True
                        break
                    i += 1

                if contem_palavra:
                    f_destino.write(linha)
            
            f_origem.close()
            f_destino.close()
            print(f"Linhas contendo '{palavra_chave}' filtradas com sucesso de '{nome_arquivo_origem}' para '{nome_arquivo_destino}'.")
        except FileNotFoundError:
            print(f"Erro: Arquivo de origem '{nome_arquivo_origem}' não encontrado.")
        except IOError as e:
            print(f"Erro durante a filtragem de arquivo: {e}")

    arquivo_origem = input("Digite o nome do arquivo de origem (ex: dados.txt): ")
    arquivo_destino = input("Digite o nome do arquivo de destino para linhas filtradas: ")
    palavra_chave = input("Digite a palavra-chave para filtrar as linhas: ")
    
    filtrar_linhas(arquivo_origem, arquivo_destino, palavra_chave)
