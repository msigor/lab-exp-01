Aqui está a versão atualizada do `README.md` com informações sobre os arquivos de relatório na pasta `docs/`:

---

# Análise de Repositórios Populares no GitHub

## 📌 Visão Geral
Este projeto coleta dados de repositórios populares no GitHub e analisa suas características, como idade, pull requests, releases e linguagem principal. Com o Docker Compose, você pode rodar o projeto de forma rápida e sem a necessidade de configurar manualmente o ambiente Python.

---

## 🐳 Como Rodar o Projeto com Docker Compose

### **1️⃣ Pré-requisitos**
Certifique-se de ter instalado:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

### **2️⃣ Criar o arquivo `.env`**
O arquivo `.env` é necessário para configurar o token de acesso à API do GitHub. Crie o arquivo na raiz do projeto:

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

### **3️⃣ Rodar o Projeto**
Com o Docker Compose, você pode rodar o projeto com um único comando. Na raiz do projeto, execute:

```sh
docker-compose up
```

Isso irá:
1. Construir a imagem Docker com todas as dependências necessárias.
2. Executar o script `fetch_data.py` para coletar dados dos repositórios.
3. Salvar os dados coletados em `data/resultados.csv`.

---

### **4️⃣ Processar os Dados (Opcional)**
Se desejar processar os dados coletados e gerar estatísticas, execute:

```sh
docker-compose run app python src/process_data.py
```

Isso irá gerar um arquivo `data/resultados_processados.csv` com as estatísticas dos repositórios.

---

### **5️⃣ Parar o Projeto**
Para parar e remover os contêineres, execute:

```sh
docker-compose down
```

---

## 🛠️ Estrutura do Projeto
- **`src/`**: Contém os scripts Python para coleta e processamento de dados.
  - `fetch_data.py`: Coleta dados dos repositórios no GitHub.
  - `process_data.py`: Processa os dados coletados e gera estatísticas.
- **`data/`**: Armazena os arquivos de dados gerados (`resultados.csv` e `resultados_processados.csv`).
- **`docs/`**: Contém os relatórios gerados a partir da análise dos dados.
  - `Relatório 01 - Características de repositórios populares.pdf`: Relatório em formato PDF com a análise detalhada dos dados.
  - `Relatório 01 - Características de repositórios populares.docx`: Relatório em formato Word (DOCX) com a análise detalhada dos dados.
- **`Dockerfile`**: Configuração do ambiente Docker.
- **`docker-compose.yml`**: Define os serviços e configurações do Docker Compose.
- **`.env`**: Armazena variáveis de ambiente, como o token do GitHub.

---

## 🔍 Como Funciona o Docker Compose
O arquivo `docker-compose.yml` define um serviço chamado `app` que:
1. Utiliza a imagem base do Python.
2. Instala as dependências listadas no `requirements.txt`.
3. Monta o diretório local no contêiner para permitir acesso aos scripts e dados.
4. Executa os scripts Python dentro do contêiner.

---

## 📊 Resultados
Após a execução, você encontrará os seguintes arquivos na pasta `data/`:
- `resultados.csv`: Dados brutos coletados dos repositórios.
- `resultados_processados.csv`: Estatísticas processadas sobre os repositórios.

Além disso, na pasta `docs/`, você encontrará os relatórios gerados:
- **`Relatório 01 - Características de repositórios populares.pdf`**: Um relatório em formato PDF que descreve as características dos repositórios populares, incluindo gráficos, tabelas e análises detalhadas.
- **`Relatório 01 - Características de repositórios populares.docx`**: O mesmo relatório em formato Word (DOCX), permitindo edições e personalizações adicionais.

---

## ❓ Dúvidas ou Problemas?
Se encontrar algum problema ou tiver dúvidas, sinta-se à vontade para abrir uma _issue_ no repositório ou entrar em contato.

---

## 📄 Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

--- 

Se precisar de mais detalhes ou ajustes, é só avisar! 😊