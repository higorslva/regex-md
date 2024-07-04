import os
import json

def ler_descricoes(diretorio):
    descricoes = []

    # Iterar sobre todos os arquivos no diretório
    for filename in os.listdir(diretorio):
        if filename.endswith('.json'):
            filepath = os.path.join(diretorio, filename)
            
            # Abrir e ler o arquivo JSON
            with open(filepath, 'r', encoding='utf-8') as file:
                dados = json.load(file)
                
                # Recuperar o valor da chave "descricao"
                if 'descricao' in dados:
                    descricoes.append(dados['descricao'])

    return descricoes

def salvar_descricoes(descricoes, arquivo_saida):
    with open(arquivo_saida, 'w', encoding='utf-8') as file:
        json.dump(descricoes, file, ensure_ascii=False, indent=4)

def main():
    diretorio = 'formatado/conteudo/formatado'  # Substitua pelo caminho do seu diretório
    arquivo_saida = 'descricoes.json'

    descricoes = ler_descricoes(diretorio)
    salvar_descricoes(descricoes, arquivo_saida)
    print(f"Descrições salvas em {arquivo_saida}")

if __name__ == "__main__":
    main()
