import csv
from query import get_query
from github_api import run_query

def fetch_repositories(target_count=100):
    """Coleta dados de repositórios do GitHub."""
    repos = []
    after_cursor = None

    while len(repos) < target_count:
        query = get_query(after_cursor)
        result = run_query(query)
        
        if 'data' in result:
            search_data = result['data']['search']
            for edge in search_data['edges']:
                repo = edge['node']
                closed_issues = sum(1 for issue in repo['issues']['nodes'] if issue['state'] == 'CLOSED')
                open_issues = sum(1 for issue in repo['issues']['nodes'] if issue['state'] == 'OPEN')
                repos.append([
                    repo['name'], repo['createdAt'], repo['pullRequests']['totalCount'],
                    repo['releases']['totalCount'], repo['updatedAt'],
                    repo['primaryLanguage']['name'] if repo['primaryLanguage'] else 'N/A',
                    closed_issues, open_issues
                ])
            
            if not search_data['pageInfo']['hasNextPage']:
                break
            after_cursor = search_data['pageInfo']['endCursor']
        else:
            print("Erro na resposta da API:", result)
            break
    
    return repos

if __name__ == "__main__":
    repositories = fetch_repositories()

    with open("data/resultados.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Data de Criação", "Pull Requests Aceitas", "Total de Releases", "Última Atualização", "Linguagem Primária", "Issues Fechadas", "Issues Abertas"])
        writer.writerows(repositories)

    print(f"✅ Dados coletados e salvos em 'data/resultados.csv' ({len(repositories)} repositórios)")
