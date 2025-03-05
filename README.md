# **Análise de Repositórios Populares no GitHub**

## 📌 **Visão Geral**
Este projeto coleta e analisa dados de repositórios populares no GitHub, avaliando características como:
- **Idade do repositório**
- **Quantidade de Pull Requests aceitas**
- **Número total de releases**
- **Última atualização**
- **Linguagem principal**
- **Taxa de fechamento de issues**

Além da coleta e processamento dos dados, o projeto agora inclui **visualizações gráficas** e **um relatório CSV com estatísticas detalhadas**, permitindo uma análise mais rica dos repositórios estudados.

---

## 🐳 **Como Rodar o Projeto com Docker Compose**

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

### **4️⃣ Processar os Dados**
Após a coleta, processe os dados e gere estatísticas executando:

```sh
docker-compose run app python src/process_data.py
```

Isso irá gerar:
- **`data/resultados_processados.csv`**: Estatísticas processadas dos repositórios.

---

### **5️⃣ Gerar Análises e Gráficos**
Agora, execute a análise dos dados e gere gráficos:

```sh
docker-compose run app python src/analyze_data.py
```

Isso criará:
- **Gráficos na pasta `output/`**:
  - `histograma_idade.png` – Distribuição da idade dos repositórios.
  - `linguagens_mais_usadas.png` – Linguagens mais utilizadas.
  - `dispersao_idade_releases.png` – Relação entre idade e número de releases.
  - `pr_por_linguagem.png` – Pull Requests aceitas por linguagem.
  - `releases_por_linguagem.png` – Total de releases por linguagem.
  - `atualizacao_por_linguagem.png` – Frequência de atualização por linguagem.

- **Arquivo CSV com todas as estatísticas na pasta `data/`**:
  - `estatisticas_repositorios.csv` – Contém os valores estatísticos extraídos dos dados coletados.

---

### **6️⃣ Parar o Projeto**
Para parar e remover os contêineres, execute:

```sh
docker-compose down
```

---

## 🛠️ **Estrutura do Projeto**
```
📂 src/                        # Scripts Python do projeto
 ├── fetch_data.py             # Coleta dados dos repositórios do GitHub
 ├── process_data.py           # Processa e estrutura os dados coletados
 ├── analyze_data.py           # Gera gráficos e estatísticas detalhadas
📂 data/                        # Armazena arquivos CSV gerados
 ├── resultados.csv            # Dados brutos coletados
 ├── resultados_processados.csv # Dados processados
 ├── estatisticas_repositorios.csv # Estatísticas geradas a partir dos dados
📂 output/                      # Gráficos gerados
 ├── histograma_idade.png      
 ├── linguagens_mais_usadas.png
 ├── dispersao_idade_releases.png
 ├── pr_por_linguagem.png
 ├── releases_por_linguagem.png
 ├── atualizacao_por_linguagem.png
📂 docs/                        # Relatórios criados
 ├── Relatório 01 - Características de repositórios populares.pdf
 ├── Relatório 01 - Características de repositórios populares.docx
📄 Dockerfile                   # Configuração do ambiente Docker
📄 docker-compose.yml           # Define serviços do Docker Compose
📄 .env                         # Variáveis de ambiente do GitHub Token
```

---

## 📊 **Resultados**
Após a execução, você encontrará os seguintes arquivos na pasta `data/`:
- `resultados.csv`: Dados brutos coletados dos repositórios.
- `resultados_processados.csv`: Estatísticas processadas sobre os repositórios.
- `estatisticas_repositorios.csv`: Resumo estatístico das métricas analisadas.

Na pasta `output/`, estarão os gráficos gerados.

Além disso, na pasta `docs/`, você encontrará os relatórios criados após a análise dos dados:
- **`Relatório 01 - Características de repositórios populares.pdf`** – Relatório em formato PDF detalhando as análises dos repositórios.
- **`Relatório 01 - Características de repositórios populares.docx`** – O mesmo relatório em formato Word, para edição e personalização.
