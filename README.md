# Análise de Repositórios Populares no GitHub

## 📌 Visão Geral
Este projeto coleta dados de repositórios populares no GitHub e analisa suas características, como idade, pull requests, releases e linguagem principal.

---

## 🔧 Como Configurar o Ambiente Python

Como as pastas do ambiente virtual e o arquivo `.env` estão no `.gitignore`, você precisará configurar o ambiente corretamente antes de rodar o projeto.

### **1️⃣ Criar e ativar o ambiente virtual**
No terminal, execute:

- **macOS/Linux**:
  ```sh
  python3 -m venv .venv
  source .venv/bin/activate
  ```

- **Windows (cmd)**:
  ```sh
  python -m venv .venv
  .venv\Scripts\activate
  ```

Agora, o terminal deve mostrar `(.venv)`, indicando que o ambiente virtual está ativado.

---

### **2️⃣ Instalar as dependências**
Com o ambiente ativado, instale as dependências:
```sh
pip install --upgrade pip
pip install -r requirements.txt
```
Se o arquivo `requirements.txt` não existir, instale manualmente:
```sh
pip install requests python-dotenv pandas
```

---

### **3️⃣ Criar o arquivo `.env`**
O `.env` não está no repositório, então você precisará criá-lo manualmente:

```sh
touch .env
```

Abra o `.env` e adicione as credenciais necessárias:
```ini
GITHUB_TOKEN=ghp_xxxxxxxSEU_TOKEN_AQUI
API_URL=https://api.github.com/graphql
```

🔹 **Gere um token de acesso no GitHub**: [GitHub Developer Settings](https://github.com/settings/tokens).

---

### **4️⃣ Testar o ambiente**
Para garantir que o ambiente está pronto, rode:
```sh
python -c "import requests, dotenv, pandas; print('Ambiente configurado corretamente!')"
```
Se a saída for:
```
Ambiente configurado corretamente!
```
Tudo está pronto para rodar o projeto! 🚀

---

## ▶️ Como Rodar o Projeto
Depois de configurar o ambiente, execute:
```sh
python src/fetch_data.py
```
Isso irá coletar dados dos repositórios e salvar em `data/resultados.csv`.

Se quiser processar os dados:
```sh
python src/process_data.py
```
Isso gerará um arquivo `data/resultados_processados.csv` com estatísticas sobre os repositórios.

---