import pandas as pd
from datetime import datetime, timezone

def process_csv(file_path="data/resultados.csv"):
    """
    Processa os dados do CSV para análise estatística.

    Args:
        file_path (str): Caminho para o arquivo CSV contendo os dados.

    Returns:
        pd.DataFrame: DataFrame com os dados processados.
    """
    try:
        # Carrega o arquivo CSV
        df = pd.read_csv(file_path)

        # Verifica se as colunas necessárias estão presentes
        required_columns = [
            "Data de Criação", "Última Atualização", 
            "Issues Fechadas", "Issues Abertas"
        ]
        if not all(column in df.columns for column in required_columns):
            raise ValueError(f"O arquivo CSV deve conter as colunas: {required_columns}")

        # Converte as colunas de data para datetime
        df["Data de Criação"] = pd.to_datetime(df["Data de Criação"], utc=False)
        df["Última Atualização"] = pd.to_datetime(df["Última Atualização"], utc=False)

        # Calcula a idade do repositório em anos
        now = datetime.now()
        df["Idade (anos)"] = (now - df["Data de Criação"]).dt.days / 365

        # Calcula os dias desde a última atualização
        df["Dias desde última atualização"] = (now - df["Última Atualização"]).dt.days

        # Calcula a taxa de fechamento de issues
        df["Taxa de Fechamento de Issues"] = df["Issues Fechadas"] / (
            df["Issues Fechadas"] + df["Issues Abertas"]
        )

        return df

    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em '{file_path}'.")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro
    except Exception as e:
        print(f"Erro ao processar o arquivo CSV: {e}")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro

if __name__ == "__main__":
    # Processa o CSV e salva os resultados
    df = process_csv()

    if not df.empty:
        # Exibe estatísticas básicas dos dados
        print(df.describe())

        # Salva os dados processados em um novo arquivo CSV
        output_path = "data/resultados_processados.csv"
        df.to_csv(output_path, index=False)
        print(f"✅ Dados processados e salvos em '{output_path}'")
    else:
        print("❌ Nenhum dado foi processado devido a erros.")