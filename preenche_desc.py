import os
import json

def ler_descricoes(arquivo_descricoes):
    with open(arquivo_descricoes, 'r', encoding='utf-8') as file:
        descricoes = json.load(file)
    return descricoes

def preencher_descricoes(diretorio, descricoes):
    # Iterar sobre todos os arquivos no diretório
    for filename in os.listdir(diretorio):
        if filename.endswith('.json'):
            filepath = os.path.join(diretorio, filename)
            
            # Abrir e ler o arquivo JSON
            with open(filepath, 'r+', encoding='utf-8') as file:
                dados = json.load(file)
                
                # Preencher a descrição do arquivo de acordo com o dicionário de descrições
                if filename in descricoes:
                    dados['descricao'] = descricoes[filename]
                    
                    # Voltar ao início do arquivo e reescrever os dados atualizados
                    file.seek(0)
                    json.dump(dados, file, ensure_ascii=False, indent=4)
                    file.truncate()

def main():
    diretorio = 'formatado/links/formatado'  # Substitua pelo caminho do seu diretório
    arquivo_descricoes = 'descricoes.json'

    # Ler as descrições do arquivo separado
    descricoes = ler_descricoes(arquivo_descricoes)
    
    # Preencher as descrições nos arquivos JSON de origem
    preencher_descricoes(diretorio, descricoes)
    print("Descrições preenchidas nos arquivos de origem com sucesso.")

if __name__ == "__main__":
    main()
