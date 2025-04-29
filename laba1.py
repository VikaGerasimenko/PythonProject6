import requests
from bs4 import BeautifulSoup

def parse():
    url = 'https://auto.drom.ru/all/'

    page = requests.get(url)
    print(page.status_code)

    soup = BeautifulSoup(page.text, "html.parser")

    ad_elements = soup.find_all('div', class_='css-1f68fiz ea1vuk60', limit=20)

    with open('car_ads.txt', 'w', encoding='utf-8') as file:
        for ad_element in ad_elements:
         title_element = ad_element.find('h3', class_='css-16kqa8y efwtv890')
         price_element = ad_element.find('span', class_='css-46itwz e162wx9x0')
         link_element = ad_element.find('a')

         title = title_element.text.strip()
         price = price_element.text.strip()
         link = link_element['href']

         file.write(f'Название: {title}, Цена: {price}, Ссылка: {link}\n')

print("Список объявлений успешно записан в файл car_ads.txt")
parse()