import fitz  # PyMuPDF
import pandas as pd
import os

# Указываем путь к PDF файлу
pdf_path = './data/raw/dictionaty_rus_kub.pdf'

# Проверяем, существует ли файл
if not os.path.exists(pdf_path):
    print(f"Файл не найден: {pdf_path}")
    exit()

# Открываем PDF файл
document = fitz.open(pdf_path)

# Функция для извлечения текста из всех страниц PDF начиная с указанной страницы
def extract_text_from_pdf(document, start_page=5):
    text = ""
    for page_num in range(start_page, len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

# Извлекаем текст из PDF начиная с 5 страницы (индекс 4)
pdf_text = extract_text_from_pdf(document, start_page=5)

# Обрабатываем текст для создания датасета
lines = pdf_text.split('\n')
data = []

for line in lines:
    if line.strip():  # Пропускаем пустые строки
        parts = line.split('. ')
        if len(parts) >= 2:  # Может быть больше 2 частей, если несколько переводов
            russian = parts[0].strip()
            kubachin = ' '.join(parts[1:]).strip()
            data.append((russian, kubachin))

# Создаем DataFrame
df = pd.DataFrame(data, columns=['Russian', 'Kubachin'])

# Сохраняем DataFrame в CSV файл
csv_output_path = './data/processed/kubachin_dataset.csv'
df.to_csv(csv_output_path, index=False, encoding='utf-8')

print(f"Датасет успешно создан и сохранен в файл {csv_output_path}")
