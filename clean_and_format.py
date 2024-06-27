import json
import re
import os
import pandas as pd

# Função para extrair prompts e targets
def extract_prompts_targets(content):
    pattern = re.compile(r'\[(.*?)\]')
    matches = pattern.finditer(content)
    
    results = []
    previous_end = 0
    
    for match in matches:
        prompt = match.group(1)
        start, end = match.span()
        target = content[previous_end:start].strip()
        if target:
            results.append({'prompt': prompt, 'target': target})
        previous_end = end
    
    if previous_end < len(content):
        remaining_content = content[previous_end:].strip()
        if remaining_content:
            results.append({'prompt': 'default_prompt', 'target': remaining_content})
    
    return results

# Definir pastas de entrada e saída
input_folder = 'limpo'
output_folder = 'formatado'

# Criar a pasta de saída se não existir
os.makedirs(output_folder, exist_ok=True)

# Processar todos os arquivos na pasta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        # Caminho completo para o arquivo
        file_path = os.path.join(input_folder, filename)
        
        # Ler o arquivo JSON
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                print(f"Erro ao decodificar {filename}: {e}")
                continue
        
        # Verificar se o JSON contém a estrutura esperada
        if isinstance(data, dict) and 'content' in data:
            # Extrair prompts e targets
            results = extract_prompts_targets(data['content'])
            
            # Criar DataFrame com os resultados
            df = pd.DataFrame(results)
            
            # Caminho para o arquivo JSON de saída
            output_file = os.path.join(output_folder, filename)
            
            # Salvar o DataFrame em um novo arquivo JSON
            df.to_json(output_file, orient='records', force_ascii=False, indent=4)
            print(f"Conteúdo formatado e salvo no arquivo '{output_file}'.")
        else:
            print(f"Estrutura de dados inválida em {filename}")

print("Processamento concluído.")
