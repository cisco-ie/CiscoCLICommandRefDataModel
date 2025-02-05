import requests
from bs4 import BeautifulSoup
import json

def scrape_website(url, key_value):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        json_array = []
        articles = soup.find_all('article')
        
        if articles:
            for index, article in enumerate(articles, start=1):
                paragraphs = article.find('p')
                description = paragraphs.text.strip() if paragraphs else None
                refsyn_sections = article.find_all('section', class_='refsyn')
                
                if refsyn_sections:
                    for refsyn_section in refsyn_sections:
                        first_paragraph = refsyn_section.find('p')
                        json_object = {
                            "command": first_paragraph.text.strip() if first_paragraph else None,
                            "description": ' '.join(description.split()),  
                            "example": ""  
                        }
                        example_sections = article.find_all('section', class_='example command_examples')
                        
                        if example_sections:
                            examples_text = "" 
                            for example_section in example_sections:
                                pre_tags = example_section.find_all('pre', class_='pre codeblock')
                                
                                for pre_tag in pre_tags:
                                    pre_text = pre_tag.get_text()
                                    pre_text = pre_text.replace('\u00a0', ' ')
                                    examples_text += pre_text + '\n'
                        
                            json_object["example"] = examples_text.strip()
                        if json_object["command"] and json_object["command"].startswith("show"):
                            json_array.append(json_object)
        d = {f"{key_value}":json_array}           
        return d
            

json_array = []
while True:
    webpage_url = input("Enter the URL of the website to parse data from:\n")
    key = input("Enter the name for the data that will be scrapped from the webpage:\n")
    data = scrape_website(webpage_url,key)
    json_array.append(data)
    continue_loop = input("Would you like to parse from another page? (yes/no): ")
    if continue_loop.lower() != "yes":
        break

with open('output.json', 'w') as file:
    file.write(json.dumps(json_array, indent=4))
