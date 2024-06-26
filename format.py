import json
import re

# Função para limpar o conteúdo em Markdown
def clean_markdown(content):
    # Remover links e textos em colchetes
    content = re.sub(r'\[.*?\]\(.*?\)', '', content)
    # Remover cabeçalhos de markdown
    content = re.sub(r'#{1,6} ', '', content)
    # Remover asteriscos e sublinhados
    content = re.sub(r'\*|_', '', content)
    # Remover texto em negrito e itálico
    content = re.sub(r'\*\*(.*?)\*\*', r'\1', content)
    content = re.sub(r'_(.*?)_', r'\1', content)
    # Remover outros caracteres especiais do Markdown
    content = re.sub(r'`', '', content)
    return content

# Ler o arquivo JSON
with open('response_3.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Limpar o conteúdo
data['content'] = clean_markdown(data['content'])

# Salvar o conteúdo limpo em um novo arquivo JSON
with open('response_clean.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Conteúdo limpo e salvo em 'response_clean.json'.")
