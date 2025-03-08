import requests
import time
from config import URL, HEADERS

def run_query(query, retries=3):
    for attempt in range(retries):
        response = requests.post(URL, json={'query': query}, headers=HEADERS, timeout=30)
        if response.status_code == 200:
            return response.json()
        elif attempt < retries - 1:
            time.sleep(2 ** attempt)  # Backoff exponencial para evitar bloqueios
        else:
            raise Exception(f"Query falhou com código {response.status_code}: {response.text}")
