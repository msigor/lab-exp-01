import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

def carregar_dados(caminho_arquivo="data/resultados_processados.csv"):
    """
    Carrega os dados de um arquivo CSV para um DataFrame.
    """
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        sys.exit(1)
    return pd.read_csv(caminho_arquivo)

def gerar_graficos_e_csv(df):
    """
    Gera gráficos para análise visual dos dados coletados e salva os resultados em um CSV.
    """
    # Garante que o diretório de saída existe
    output_dir = "output"
    data_dir = "data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # Configuração global do estilo dos gráficos
    sns.set_theme(style="whitegrid")
    
    # Criando dicionário para armazenar os valores estatísticos
    estatisticas = {}
    
    # 1. Histograma da idade dos repositórios
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Idade (anos)"], bins=20, kde=True)
    plt.title("Distribuição da Idade dos Repositórios")
    plt.xlabel("Idade (anos)")
    plt.ylabel("Frequência")
    plt.savefig(f"{output_dir}/histograma_idade.png")
    plt.show()
    estatisticas["Mediana da Idade dos Repositórios (anos)"] = df["Idade (anos)"].median()
    
    # 2. Gráfico de barras das linguagens mais usadas
    plt.figure(figsize=(10, 6))
    top_languages = df["Linguagem Primária"].value_counts().head(10)
    sns.barplot(x=top_languages.values, y=top_languages.index, palette="viridis")
    plt.title("Top 10 Linguagens Mais Utilizadas")
    plt.xlabel("Número de Repositórios")
    plt.ylabel("Linguagem")
    plt.savefig(f"{output_dir}/linguagens_mais_usadas.png")
    plt.show()
    estatisticas["Linguagens Mais Usadas"] = top_languages.to_dict()
    
    # 3. Gráfico de dispersão entre idade dos repositórios e número de releases
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=df["Idade (anos)"], y=df["Total de Releases"], alpha=0.6)
    plt.title("Relação entre Idade e Número de Releases")
    plt.xlabel("Idade do Repositório (anos)")
    plt.ylabel("Total de Releases")
    plt.savefig(f"{output_dir}/dispersao_idade_releases.png")
    plt.show()
    estatisticas["Mediana do Total de Releases"] = df["Total de Releases"].median()
    
    # 4. Gráfico de barras comparando Pull Requests aceitas por linguagem
    pr_por_linguagem = df.groupby("Linguagem Primária")["Pull Requests Aceitas"].median().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=pr_por_linguagem.values, y=pr_por_linguagem.index, palette="coolwarm")
    plt.title("Média de Pull Requests Aceitas por Linguagem")
    plt.xlabel("Mediana de Pull Requests Aceitas")
    plt.ylabel("Linguagem")
    plt.savefig(f"{output_dir}/pr_por_linguagem.png")
    plt.show()
    estatisticas["Mediana de Pull Requests Aceitas"] = df["Pull Requests Aceitas"].median()
    
    # 5. Gráfico de barras comparando Releases por linguagem
    releases_por_linguagem = df.groupby("Linguagem Primária")["Total de Releases"].median().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=releases_por_linguagem.values, y=releases_por_linguagem.index, palette="magma")
    plt.title("Média de Releases por Linguagem")
    plt.xlabel("Mediana de Releases")
    plt.ylabel("Linguagem")
    plt.savefig(f"{output_dir}/releases_por_linguagem.png")
    plt.show()
    
    # 6. Gráfico de barras comparando frequência de atualização por linguagem
    atualizacao_por_linguagem = df.groupby("Linguagem Primária")["Dias desde última atualização"].median().sort_values().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=atualizacao_por_linguagem.values, y=atualizacao_por_linguagem.index, palette="Blues")
    plt.title("Média de Dias Desde Última Atualização por Linguagem")
    plt.xlabel("Mediana de Dias Desde Última Atualização")
    plt.ylabel("Linguagem")
    plt.savefig(f"{output_dir}/atualizacao_por_linguagem.png")
    plt.show()
    estatisticas["Mediana dos Dias Desde Última Atualização"] = df["Dias desde última atualização"].median()
    estatisticas["Mediana da Taxa de Fechamento de Issues"] = df["Taxa de Fechamento de Issues"].median()
    
    # Salvar os dados estatísticos em um CSV na pasta data
    df_estatisticas = pd.DataFrame(list(estatisticas.items()), columns=["Métrica", "Valor"])
    df_estatisticas.to_csv(f"data/estatisticas_repositorios.csv", index=False)
    print(f"✅ Estatísticas detalhadas salvas em '{data_dir}/estatisticas_repositorios.csv'")

def main():
    df = carregar_dados()
    gerar_graficos_e_csv(df)

if __name__ == "__main__":
    main()
