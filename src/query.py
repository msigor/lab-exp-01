# query.py

def get_query(after_cursor=None):
    after = f', after: "{after_cursor}"' if after_cursor else ''
    return f"""
    {{
      search(query: "stars:>10000", type: REPOSITORY, first: 10{after}) {{
        edges {{
          cursor
          node {{
            ... on Repository {{
              name
              createdAt
              pullRequests(states: MERGED) {{ totalCount }}
              releases {{ totalCount }}
              updatedAt
              primaryLanguage {{ name }}
              issues(first: 100) {{
                totalCount
                nodes {{ state }}
              }}
            }}
          }}
        }}
        pageInfo {{
          hasNextPage
          endCursor
        }}
      }}
    }}"""
