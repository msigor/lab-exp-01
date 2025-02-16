from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

# Obtém as variáveis de ambiente
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
URL = os.getenv("API_URL")  # Alterado para corresponder ao github_api.py

# Configuração dos headers para chamadas à API do GitHub
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Verificação das variáveis carregadas
if not GITHUB_TOKEN:
    raise ValueError("Erro: GITHUB_TOKEN não foi carregado do .env.")
if not URL:
    raise ValueError("Erro: API_URL (URL) não foi carregado do .env.")

print(f"URL: {URL}")
print(f"GITHUB_TOKEN: {GITHUB_TOKEN[:5]}... (oculto para segurança)")
