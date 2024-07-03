import json
import re
import os

# Função para extrair descrições e links do texto
def extract_descriptions_and_links(content):
    pattern = re.compile(r'\[(.*?)\]\((.*?)\)')
    matches = pattern.findall(content)
    return matches

# Função principal
def main():
    input_directory = 'formatar'  # Nome da pasta de entrada
    output_directory = 'formatar/formatado'  # Nome da pasta de saída
    
    # Cria a pasta de saída se ela não existir
    os.makedirs(output_directory, exist_ok=True)
    
    # Lista todos os arquivos JSON na pasta de entrada
    for filename in os.listdir(input_directory):
        if filename.startswith('response_') and filename.endswith('.json'):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
            
            with open(input_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                        
            content = data.pop('content', '')
            metadata = data.pop('metadata', {})
            source_url = metadata.get('sourceURL', '')
            
            # Extrair descrições e links
            descriptions_and_links = extract_descriptions_and_links(content)
            
            # Criar a estrutura de saída
            output_data = []
            for description, link in descriptions_and_links:
                output_data.append({
                    "opcao": description,
                    "link": link,
                    "sourceURL": source_url,
                    "descrição": content
                })

            # Salvar o JSON de saída
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()
