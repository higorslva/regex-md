import requests
from openai import OpenAI

client = OpenAI(api_key='OPENAI_API')


def fetch_json_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def fetch_json_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text  # Returns raw JSON string
    else:
        return None


def generate_summary_for_json(api_url):
    json_str = fetch_json_from_api(api_url)  # Raw JSON string
    if json_str is None:
        return "Failed to fetch or parse JSON data from the API."

    system_message = "You are a helpful assistant. You will generate a summary of the JSON file."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": json_str}
        ],
        temperature=1,
        max_tokens=1812,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content

api_url = "ENDPOINT_URL"
summary = generate_summary_for_json(api_url)
print(summary)