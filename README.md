# CiscoCLICommandRefDataModel
Optimizing Cisco Command References for Azure Integration

Description:

This Python script scrapes data from Cisco Command Reference web pages, processes it, and stores it in a JSON file. The user is prompted to enter the URL of a website from which they want to scrape data. They  also provide a name for the data being scraped. The script extracts relevant information such as commands, descriptions, and examples from the HTML structure of the webpage.

Packages Required:
- requests: Allows sending HTTP requests to the provided URL.
- BeautifulSoup (from bs4): A Python library for parsing HTML and XML documents.
- json: A built-in Python library for encoding and decoding JSON data.

Functions:

1. scrape_website(url, key_value):
    - Parameters:
        - url: The URL of the website to scrape data from.
        - key_value: The name for the data being scraped (e.g., "BGP Show Commands").
    - Returns:
        - A dictionary containing the scraped data formatted as JSON.

Main Code:

Input:
- URL of the website to scrape data from.
- Name for the data being scraped.

Output:
- JSON file ('output.json') containing the scraped data in a structured json format.

