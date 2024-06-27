import json
import re
import os

def clean_markdown(content):
    content = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1 \2', content)           # Remover colchetes e parênteses de links
    content = re.sub(r'(#)', ' ', content)                               # Remover jogo da velha
    #content = re.sub(r'\n', ' ', content)                               # Remover "\n" do markdown
    content = re.sub(r'#{1,6} ', '', content)                            # Remover cabeçalhos de markdown
    content = re.sub(r'\*|_', '', content)                               # Remover asteriscos e sublinhados
    content = re.sub(r'\*\*(.*?)\*\*', r'\1', content)                   # Remover texto em negrito
    content = re.sub(r'_(.*?)_', r'\1', content)                         # Remover texto em itálico
    content = re.sub(r'`', '', content)                                  # Remover outros caracteres especiais do Markdown
    content = re.sub(r'^Topo.*?http://mail.tjap.jus.br/', '', content)   # Remover header
    content = re.sub(r'Tribunal.*?feriados\.', '', content)              # Remover footer simples
    return content

input_folder = 'testesLimpJSON/jsons'
output_folder = 'testesLimpJSON/limpo'

# Criar a pasta de saída se não existir
os.makedirs(output_folder, exist_ok=True)

# Processar todos os arquivos na pasta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        # Caminho completo para o arquivo
        file_path = os.path.join(input_folder, filename)
        
        # Ler o arquivo JSON
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        del data['markdown']
        # Limpar o conteúdo
        data['content'] = clean_markdown(data['content'])
        
        # Caminho completo para o arquivo limpo
        cleaned_file_path = os.path.join(output_folder, filename)
        
        # Salvar o conteúdo limpo em um novo arquivo JSON
        with open(cleaned_file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

print(f"Conteúdo limpo e salvo na pasta '{output_folder}'.")
