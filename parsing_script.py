import requests
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import urlparse

def is_valid_url(url):
    # Simple URL validation
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])

def scrape_website(url, key_value):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return {}

    soup = BeautifulSoup(response.content, 'html.parser')
    json_array = []
    articles = soup.find_all('article')

    for article in articles:
        description = article.find('p')
        description_text = description.text.strip() if description else "No description available"

        refsyn_sections = article.find_all('section', class_='refsyn')
        for refsyn_section in refsyn_sections:
            command = refsyn_section.find('p')
            command_text = command.text.strip() if command else "Unknown Command"

            example_sections = article.find_all('section', class_='example command_examples')
            examples_text = ""

            for example_section in example_sections:
                pre_tags = example_section.find_all('pre', class_='pre codeblock')
                for pre_tag in pre_tags:
                    pre_text = pre_tag.get_text().replace('\u00a0', ' ')
                    examples_text += pre_text + '\n'

            json_object = {
                "command": command_text,
                "description": description_text,
                "example": examples_text.strip()
            }

            if json_object["command"].startswith("show"):
                json_array.append(json_object)

    return {key_value: json_array}

def main():
    json_array = []

    while True:
        webpage_url = input("Enter the URL of the website to parse data from:\n")
        if not is_valid_url(webpage_url):
            print("Invalid URL. Please enter a valid URL.")
            continue

        key = input("Enter the name for the data that will be scraped from the webpage:\n").strip()
        if not key:
            print("Key cannot be empty.")
            continue

        data = scrape_website(webpage_url, key)
        if data:
            json_array.append(data)

        continue_loop = input("Would you like to parse from another page? (yes/no): ").strip().lower()
        if continue_loop != "yes":
            break

    try:
        with open('output.json', 'w') as file:
            json.dump(json_array, file, indent=4)
        print("Data saved to output.json successfully.")
    except IOError as e:
        print(f"Error writing to output.json: {e}")

if __name__ == "__main__":
    main()

