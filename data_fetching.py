from pymed import PubMed

pubmed = PubMed(tool='my_tool', email = 'johncgsantos@gmail.com')
my_api_key = '97c1904baf8e8df9f16104f38262d0563f08'
pubmed.parameters.update({'api_key': my_api_key})

def fetch_articles(query):
    # Initialize PubMed API

    # Search PubMed
    search_results = pubmed.query(query)

    # Extract articles
    articles = []
    for result in search_results:
        article = {
            'doi': result.doi,
            'pubmed_id': result.pubmed_id,
            'title': result.title,
            'abstract': result.abstract
        }
        articles.append(article)

    return [articles] if articles else []