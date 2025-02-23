import csv
from query import get_query
from github_api import run_query

def sumByState(issues, state):
    return sum(1 for issue in issues if issue['state'] == state)

def fetch_repositories(target_count=1000):
    print("Coleta dados de repositórios do GitHub.")
    repos = []
    after_cursor = None
    consulta = 1

    while len(repos) < target_count:
        print(f"Consulta #{consulta} com after_cursor: {after_cursor}")
        query = get_query(after_cursor)
        result = run_query(query)
        
        if 'data' in result:
            search_data = result['data']['search']
            for edge in search_data['edges']:
                repo = edge['node']
                issues = repo['issues']['nodes']
                closed_issues = sumByState(issues, 'CLOSED')
                open_issues = sumByState(issues, 'OPEN')
                print(f"Processando repositório #{len(repos)} {repo['name']}...")
                repos.append([
                    repo['name'], repo['createdAt'], repo['pullRequests']['totalCount'],
                    repo['releases']['totalCount'], repo['updatedAt'],
                    repo['primaryLanguage']['name'] if repo['primaryLanguage'] else 'N/A',
                    closed_issues, open_issues
                ])
            if not search_data['pageInfo']['hasNextPage']:
                print("Fim das páginas de resultados. Encerrando consultas.")
                break
            after_cursor = search_data['pageInfo']['endCursor']
            consulta += 1
        else:
            print("Erro na resposta da API:", result)
            break
    print(f"Total de repositórios coletados: {len(repos)}")
    return repos

if __name__ == "__main__":
    print("Iniciando a coleta de dados...")
    repositories = fetch_repositories()
    print("Coleta de dados concluída!")

    with open("data/resultados.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Data de Criação", "Pull Requests Aceitas", "Total de Releases", "Última Atualização", "Linguagem Primária", "Issues Fechadas", "Issues Abertas"])
        writer.writerows(repositories)

    print(f"✅ Dados coletados e salvos em 'data/resultados.csv' ({len(repositories)} repositórios)")
