import requests
import json
from bs4 import BeautifulSoup
import csv
import re

def get_data(api):
    response = requests.get(f"{api}")
    if response.status_code == 200:
        return response.content
    else:
        print(f"There's a {response.status_code} error with your request")

def get_links(json_str):
    data = json.loads(json_str)
    items = data.get("items", [])
    tags = []
    text = []
    for item in items:
        if("java" in item.get("tags")):
            link = item.get("link")
            if link:
                text.append(get_text(link))

            tags.append("java")

        if("python" in item.get("tags")):
            link = item.get("link")
            if link:
                text.append(get_text(link))

            tags.append("python")

    print_to_csv(tags, text)

def get_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        elements = soup.find_all(class_="js-post-body")
        
        # Collect text from each element
        cleaned_text = []
        for element in elements:
            clean_text = element.get_text()
            # Remove non-text characters using regex
            clean_text = re.sub(r'[^a-zA-Z\s]', '', clean_text)
            cleaned_text.append(clean_text.strip())
        
        return cleaned_text
    else:
        print(f"There's a {response.status_code} error with your request")
        return None

def print_to_csv(tags, texts):
    with open('articles.csv', 'a', newline='') as csvfile:
        fieldnames = ['text', 'tag']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
        writer.writeheader()
        for tag, text in zip(tags, texts):
            writer.writerow({'text': text, 'tag': tag})

    print("CSV file has been created successfully.")


data = get_data("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow&pagesize=100")
get_links(data)
