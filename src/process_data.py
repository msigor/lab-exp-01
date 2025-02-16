import pandas as pd
from datetime import datetime

def process_csv(file_path="data/resultados.csv"):
    """Processa os dados do CSV para análise estatística."""
    df = pd.read_csv(file_path)

    # Converter datas para formato datetime
    df["Data de Criação"] = pd.to_datetime(df["Data de Criação"])
    df["Última Atualização"] = pd.to_datetime(df["Última Atualização"])

    # Calcular idade do repositório
    df["Idade (anos)"] = df["Data de Criação"].apply(lambda x: (datetime.now() - x).days / 365)

    # Tempo desde última atualização
    df["Dias desde última atualização"] = df["Última Atualização"].apply(lambda x: (datetime.now() - x).days)

    # Razão de fechamento de issues
    df["Taxa de Fechamento de Issues"] = df["Issues Fechadas"] / (df["Issues Fechadas"] + df["Issues Abertas"])

    return df

if __name__ == "__main__":
    df = process_csv()
    print(df.describe())  # Exibe estatísticas básicas dos dados
    df.to_csv("data/resultados_processados.csv", index=False)
    print("✅ Dados processados e salvos em 'data/resultados_processados.csv'")
