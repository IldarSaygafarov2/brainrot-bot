import json
from pprint import pprint

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://brainrot.fandom.com'
URL = 'https://brainrot.fandom.com/wiki/Category:Italian_Brainrot'


def get_soup(url: str = URL):
    html = requests.get(url)
    html.raise_for_status()
    return BeautifulSoup(html.text, 'html.parser')


def get_data():
    soup = get_soup()

    members_wrappers = soup.find_all(
        'div', class_='category-page__members-wrapper')

    result = {}

    for member in members_wrappers:
        first_char = member.find(
            'div', class_='category-page__first-char').get_text(strip=True)

        result[first_char] = []

        items = member.find_all('li', class_='category-page__member')
        
        print(f'[PROCCESSING] char {first_char}')
        for item in items:
            name = item.get_text(strip=True),
            print(f'==== [PROCCESSING] {name}')
            link = f'{BASE_URL}{item.find("a").get("href")}'
            
            inner_soup = get_soup(link)
            _image = inner_soup.find('a', class_='mw-file-description image')
            image = _image.get('href') if _image else ''
            
            result[first_char].append({
                'name': name,
                'image_link': image
            })

    return result


data = get_data()

with open('brainrot_data.json', mode='w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

