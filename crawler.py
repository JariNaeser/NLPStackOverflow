import requests
import json
from bs4 import BeautifulSoup

def get_data(api):
    response = requests.get(f"{api}")
    if response.status_code == 200:
        return response.content
    else:
        print(f"Hello person, there's a {response.status_code} error with your request")

def get_links(json_str):
    data = json.loads(json_str)
    items = data.get("items", [])
    links = []
    for item in items:
        link = item.get("link")
        if link:
            links.append(link)
    return links

def get_text(urls):
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            elements = soup.find_all(class_="js-post-body")
            print([element.get_text(strip=True) for element in elements])
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")

data = get_data("https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow&pagesize=1")
links = get_links(data)
get_text(links)
