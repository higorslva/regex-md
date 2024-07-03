import requests
import json

url = "https://api-publica.datajud.cnj.jus.br/api_publica_trf1/_search"

payload = json.dumps({
  "query": {
    "match": {
      "numeroProcesso": "00008323520184013202"
    }
  }
})

#Substituir <API Key> pela Chave Pública
headers = {
  'Authorization': 'ApiKey cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw==',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)