import requests
import time
from config import URL, HEADERS

def run_query(query, retries=3):
    """Executa a query GraphQL na API do GitHub."""
    for attempt in range(retries):
        response = requests.post(URL, json={'query': query}, headers=HEADERS, timeout=30)
<<<<<<< Updated upstream
        if response.status_code == 200:
            return response.json()
        elif attempt < retries - 1:
            time.sleep(2 ** attempt)  # Backoff exponencial para evitar bloqueios
=======

        if response.status_code == 200:
            return response.json()
        
        elif response.status_code == 401:
            print("Erro 401 - Bad credentials: Verifique se o GITHUB_TOKEN está correto e ativo.")
            print("Resposta completa:", response.text)
            raise Exception("Erro 401 - Autenticação falhou. Verifique o GITHUB_TOKEN.")
        
        elif attempt < retries - 1:
            print(f"Tentativa {attempt+1} falhou com código {response.status_code}. Retentando...")
            time.sleep(2 ** attempt)  # Backoff exponencial
        
>>>>>>> Stashed changes
        else:
            raise Exception(f"Query falhou com código {response.status_code}: {response.text}")
