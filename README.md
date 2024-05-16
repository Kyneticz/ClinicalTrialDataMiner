# Clinical Trial Data Miner Project

## Overview

This project aims to develop a comprehensive tool for mining clinical trial data focusing on the Dietary Inflammatory Index (DII) and its relation to specific inflammatory biomarkers. The tool leverages a relational database schema to efficiently store and analyze data extracted from PubMed/NCBI articles.

## Conceptualizing the Database Schema

### Tables

#### Articles Table
- **article_id** (PK): Unique identifier for each article.
- **doi**: Digital Object Identifier of the article.
- **pubmed_id**: PubMed ID of the article.
- **title**: Title of the article.
- **abstract**: Abstract of the article.

#### DII_Scores Table
- **article_id** (FK): References the `article_id` in the Articles table.
- **score**: The DII score for the article.

#### Biomarkers Table
- **biomarker_id** (PK): Unique identifier for each biomarker.
- **name**: Name of the biomarker.

#### Biomarker_References Table
- **article_id** (FK): References the `article_id` in the Articles table.
- **biomarker_id** (FK): References the `biomarker_id` in the Biomarkers table.
- **reference_count**: Number of times the biomarker is mentioned in the article.

#### DII_Biomarkers Table
- **article_id** (FK): References the `article_id` in the Articles table.
- **biomarker_id** (FK): References the `biomarker_id` in the Biomarkers table.
- **score**: The DII score for the specific biomarker in the article.

## Getting Started

### Prerequisites

- Python installed.
- Basic knowledge of SQL.
- Familiarity with Python libraries: NumPy, Pandas, BeautifulSoup, PyMed, or any suggested. This project will use PyMed.

## Database Setup

After setting up your environment and obtaining API access, the next step is to create the database schema. Below are the SQL commands to create the necessary tables for storing and relating the articles, DII scores, biomarkers, and their references.

### Creating Tables

Execute the following SQL commands in your MySQL database to create the tables:
sql -- Create the Articles table CREATE TABLE Articles ( article_id INT AUTO_INCREMENT PRIMARY KEY, doi VARCHAR(255) UNIQUE, pubmed_id VARCHAR(255) UNIQUE, title VARCHAR(255), abstract TEXT );

-- Create the DII_Scores table CREATE TABLE DII_Scores ( article_id INT, score DECIMAL(5,2), FOREIGN KEY (article_id) REFERENCES Articles(article_id) ON DELETE CASCADE );

-- Create the Biomarkers table CREATE TABLE Biomarkers ( biomarker_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) UNIQUE );

-- Create the Biomarker_References table CREATE TABLE Biomarker_References ( article_id INT, biomarker_id INT, reference_count INT, FOREIGN KEY (article_id) REFERENCES Articles(article_id) ON DELETE CASCADE, FOREIGN KEY (biomarker_id) REFERENCES Biomarkers(biomarker_id) ON DELETE CASCADE );

-- Create the DII_Biomarkers table CREATE TABLE DII_Biomarkers ( article_id INT, biomarker_id INT, score DECIMAL(5,2), FOREIGN KEY (article_id) REFERENCES Articles(article_id) ON DELETE CASCADE, FOREIGN KEY (biomarker_id) REFERENCES Biomarkers(biomarker_id) ON DELETE CASCADE );

### Steps to Start the Data Miner

1. **Set Up Your Environment**
   - Install Python and the necessary libraries as listed above.

2. **API Access**
   - Register for an API key from PubMed/NCBI's public API.

3. **Data Collection**
   - Write a Python script using the Entrez module to search for articles.
   - Scrape abstracts and other relevant information using BeautifulSoup.

4. **Data Cleaning and Storage**
   - Clean the collected data using Pandas.
   - Store data in CSV files.

5. **Database Setup**
   - Set up a MySQL database.
   - Create tables according to the schema design.

6. **Data Import**
   - Write a script to import cleaned data into the MySQL database.

7. **Data Analysis and Visualization**
   - Perform data analysis and visualization using Matplotlib or Seaborn.

8. **Iterate and Improve**
   - Refine processes based on insights gained.

## Contributing

Contributions are welcome Feel free to submit pull requests or open issues for discussion.

## License

This project is licensed under the MIT License.
