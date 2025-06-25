def exercicio_84():
    def substituir_em_arquivo(nome_arquivo, texto_antigo, texto_novo):
        try:
            f = open(nome_arquivo, 'r')
            conteudo = ""
            for linha in f:
                conteudo += linha
            f.close()
            
            conteudo_modificado_lista = []
            i = 0
            while i < len(conteudo):
                corresponde = True
                j = 0
                while j < len(texto_antigo):
                    if i + j >= len(conteudo) or conteudo[i + j] != texto_antigo[j]:
                        corresponde = False
                        break
                    j += 1
                
                if corresponde:
                    conteudo_modificado_lista.append(texto_novo)
                    i += len(texto_antigo)
                else:
                    conteudo_modificado_lista.append(conteudo[i])
                    i += 1
            
            conteudo_modificado = "".join(conteudo_modificado_lista)
            
            f = open(nome_arquivo, 'w')
            f.write(conteudo_modificado)
            f.close()
            print(f"Todas as ocorrências de '{texto_antigo}' substituídas por '{texto_novo}' em '{nome_arquivo}'.")
        except FileNotFoundError:
            print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        except IOError as e:
            print(f"Erro durante a substituição no arquivo: {e}")

    nome_arquivo = input("Digite o nome do arquivo para realizar a substituição (ex: dados.txt): ")
    texto_antigo = input("Digite o texto a ser substituído: ")
    texto_novo = input("Digite o novo texto: ")
    
    substituir_em_arquivo(nome_arquivo, texto_antigo, texto_novo)
