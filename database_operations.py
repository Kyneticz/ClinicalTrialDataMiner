import mysql.connector
def connect_to_database():
    connection = mysql.connector.connect(
        host='localhost' ,
        user='root',
        password='MLSdatabaseproj',
        database='ClinicalDataMiner'
    )
    print(f"Database Connection Succesful")
    return connection

def insert_article(connection, article_info):
    if article_info is None:
        print("No article info provided.")
        return

    # Define cursor at the beginning of the function
    cursor = connection.cursor(dictionary=True)

    # Check if the article already exists in the database
    cursor.execute("""
        SELECT article_id FROM articles WHERE doi = %s LIMIT 1
    """, (article_info['doi'],))
    result = cursor.fetchone()

    if result is not None:
        print(f"Article with DOI '{article_info['doi']}' already exists.")
        return  # Exit the function early if the article already exists

    # Truncate the DOI to the maximum allowed length
    max_doi_length = 255
    article_info['doi'] = article_info['doi'][:max_doi_length]

    # Truncate the pubmed_id to the maximum allowed length
    max_pubmed_id_length = 255  # Adjust this value according to your database schema
    article_info['pubmed_id'] = article_info['pubmed_id'][:max_pubmed_id_length]

    # Prepare SQL statement for inserting the article
    query = """
        INSERT INTO Articles (doi, pubmed_id, title, abstract) 
        VALUES (%s, %s, %s, %s)
    """
    values = (article_info['doi'], article_info['pubmed_id'], article_info['title'], article_info['abstract'])

    # Execute the insert statement
    cursor.execute(query, values)

    # Commit the transaction
    connection.commit()

    print(f"Successfully added article with DOI '{article_info['doi']}'")