import requests
from bs4 import BeautifulSoup
import csv

# URL сайта, который будем парсить
url = "http://yourlang.ru/dictionary/11/view"

# Отправляем запрос на сайт
response = requests.get(url)
response.raise_for_status()  # Проверяем успешность запроса

# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Находим все строки таблицы
rows = soup.find_all('tr')

# Открываем CSV файл для записи
with open('dictionary.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Russian', 'Kubachin'])  # Заголовки колонок

    # Проходимся по всем строкам таблицы
    for row in rows:
        # Извлекаем все ячейки в строке
        cells = row.find_all('td')
        
        if len(cells) >= 3:  # Проверяем, что есть как минимум 3 ячейки
            russian_word = cells[1].find('span').get('data-content', '')
            kubachin_word = cells[2].find('span').get('data-content', '')
            
            # Записываем данные в CSV файл
            csvwriter.writerow([russian_word, kubachin_word])

print("Данные успешно сохранены в dictionary.csv")
