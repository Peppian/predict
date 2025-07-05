import requests

def ask_openrouter(prompt: str) -> str:
    headers = {
        "Authorization": "Bearer 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",  # ganti ini!
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",  # atau model lain
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code != 200:
        print(f"[ERROR] {response.status_code}: {response.text}")
        return "Gagal mendapatkan respons dari LLM."

    return response.json()["choices"][0]["message"]["content"]
