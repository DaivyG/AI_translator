import pandas as pd
import csv

# Пример исходных данных
with open('./AI/data/raw/proverbs and sayings.txt') as f:
    data = f.read()

# Разделение на строки и обработка данных
lines = data.strip().split('\n')
cleaned_data = []

# Проход по строкам и извлечение пар "кубачинский - русский"
for i in range(0, len(lines), 2):
    kubachin = lines[i].strip().lstrip('• ').rstrip('.')
    russian = lines[i + 1].strip().rstrip('.')
    cleaned_data.append((russian, kubachin))

# Преобразование в DataFrame
df = pd.DataFrame(cleaned_data, columns=['Russian', 'Kubachin'])

# Сохранение данных в CSV-файл
df.to_csv('./AI/data/processed/proverbs and sayings.csv', index=False, encoding='utf-8')

# Проверка результата
print(df)