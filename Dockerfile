# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho
COPY src .
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Cria o diretório 'data' para armazenar os arquivos CSV
RUN mkdir -p data

# Comando para executar os scripts
CMD ["sh", "-c", "if [ ! -f data/resultados.csv ]; then python fetch_data.py; fi && if [ ! -f data/resultados_processados.csv ]; then python process_data.py; fi && python analyze_data.py"]