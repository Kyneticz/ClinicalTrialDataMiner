from database_operations import connect_to_database, insert_article
from data_fetching import fetch_articles

def fetch_and_store_articles(query):
    # Fetch articles
    articles = fetch_articles(query)

    # Prepare article information for insertion
    article_info_list = []
    for article in articles:
        article_info = {
            'doi': article['doi'],
            'pubmed_id': article['pubmed_id'],
            'title': article['title'],
            'abstract': article['abstract']
        }
        article_info_list.append(article_info)

    # Connect to the database
    connection = connect_to_database()

    # Insert article information into the database
    for article_info in article_info_list:
        insert_article(connection, article_info)

    # Close the database connection
    connection.close()

    print(f"Successfully processed {len(article_info_list)} articles.")

def main():
    while True:
        # Prompt the user for a query
        query = input("Enter your search query for PubMed or type exit to finish search: ")
        if query.lower() == 'exit':
            break
        print(f"Searching PubMed for: {query}")

        # Fetch and store articles based on the user's query
        fetch_and_store_articles(query)

# Execute the main function
if __name__ == "__main__":
    main()