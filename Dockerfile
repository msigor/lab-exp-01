FROM python:3.9-slim

WORKDIR /app

COPY src .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p data

CMD ["sh", "-c", """if [ ! -f data/resultados.csv ]; then python fetch_data.py; fi && if [ ! -f data/resultados_processados.csv ]; then python process_data.py; fi && python analyze_data.py"]