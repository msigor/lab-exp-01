import pandas as pd
import sys
import os

def carregar_dados(caminho_arquivo="data/resultados.csv"):
    """
    Carrega os dados de um arquivo CSV para um DataFrame.
    Valida se o arquivo existe antes de tentar carregá-lo.
    """
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        sys.exit(1)  # Encerra o programa com código de erro 1
    return pd.read_csv(caminho_arquivo)

def calcular_metricas(df):
    """
    Calcula as métricas necessárias a partir do DataFrame.
    """
    # Cálculo das medianas para métricas numéricas
    mediana_idade = df["Idade (anos)"].median()
    mediana_pr_aceitas = df["Pull Requests Aceitas"].median()
    mediana_releases = df["Total de Releases"].median()
    mediana_atualizacao = df["Dias desde última atualização"].median()
    mediana_taxa_fechamento = df["Taxa de Fechamento de Issues"].median()

    # Contagem das linguagens primárias
    contagem_linguagens = df["Linguagem Primária"].value_counts()

    # Resultados
    resultados = {
        "Mediana da idade dos repositórios (anos)": mediana_idade,
        "Mediana de pull requests aceitas": mediana_pr_aceitas,
        "Mediana do total de releases": mediana_releases,
        "Mediana dos dias desde última atualização": mediana_atualizacao,
        "Mediana da taxa de fechamento de issues": mediana_taxa_fechamento,
        "Contagem de linguagens primárias": contagem_linguagens.to_dict(),
    }
    return resultados

def exibir_resultados(resultados):
    """
    Exibe os resultados de forma organizada.
    """
    print("Análise dos dados dos repositórios populares:")
    print("--------------------------------------------")
    print(f"Mediana da idade dos repositórios: {resultados['Mediana da idade dos repositórios (anos)']:.2f} anos")
    print(f"Mediana de pull requests aceitas: {resultados['Mediana de pull requests aceitas']}")
    print(f"Mediana do total de releases: {resultados['Mediana do total de releases']}")
    print(f"Mediana dos dias desde última atualização: {resultados['Mediana dos dias desde última atualização']} dias")
    print(f"Mediana da taxa de fechamento de issues: {resultados['Mediana da taxa de fechamento de issues']:.2%}")
    print("\nContagem de linguagens primárias:")
    for linguagem, contagem in resultados["Contagem de linguagens primárias"].items():
        print(f"{linguagem}: {contagem} repositórios")
        
def salvar_resultados_csv(resultados, caminho_saida):
    """
    Salva os resultados em um arquivo CSV.
    """
    # Cria um DataFrame a partir dos resultados
    df_resultados = pd.DataFrame({
        "Métrica": [
            "Mediana da idade dos repositórios (anos)",
            "Mediana de pull requests aceitas",
            "Mediana do total de releases",
            "Mediana dos dias desde última atualização",
            "Mediana da taxa de fechamento de issues",
        ],
        "Valor": [
            resultados["Mediana da idade dos repositórios (anos)"],
            resultados["Mediana de pull requests aceitas"],
            resultados["Mediana do total de releases"],
            resultados["Mediana dos dias desde última atualização"],
            resultados["Mediana da taxa de fechamento de issues"],
        ]
    })

    # Salva o DataFrame em um arquivo CSV
    df_resultados.to_csv(caminho_saida, index=False)
    print(f"Resultados salvos em '{caminho_saida}'.")

if __name__ == "__main__":
    """
    Função principal do script.
    """

    # Carrega os dados
    df = carregar_dados('data/resultados_processados.csv')

    # Calcula as métricas
    resultados = calcular_metricas(df)

    # Exibe os resultados
    exibir_resultados(resultados)
    
    # Salva os resultados em um arquivo CSV
    salvar_resultados_csv(resultados, 'data/resultados_analisados.csv')