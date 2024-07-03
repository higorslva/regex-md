import json
from firecrawl import FirecrawlApp

# Inicializa a aplicação Firecrawl com a chave de API
app = FirecrawlApp(api_key='fc-67df28709c2247a191cb575325c6ba0e')


urls = [
                "https:"
                ]

# Função para salvar a resposta em um arquivo JSON
def save_response_to_json(response, file_name):
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(response, json_file, ensure_ascii=False, indent=4)

# Itera sobre a lista de URLs
for idx, url in enumerate(urls):
    try:
        # Faz a requisição para raspar o conteúdo da URL especificada
        response = app.scrape_url(url=url)
        
        # Verifica se a resposta é válida
        if response:
            # Define o nome do arquivo JSON com base no índice e na URL
            file_name = f'response_{idx + 1}.json'
            
            # Salva a resposta em um arquivo JSON
            save_response_to_json(response, file_name)
            
            print(f'Resposta da URL {url} salva em {file_name}')
        else:
            print(f"A resposta da URL {url} é inválida ou ocorreu um erro ao fazer a requisição.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar a URL {url}: {e}")