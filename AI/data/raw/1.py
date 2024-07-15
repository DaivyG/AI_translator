import pandas as pd
import csv

# Пример исходных данных
with open('./AI/data/raw/numbers.txt') as f:
    data = f.read()

# Разделение на строки и обработка данных
lines = data.strip().split('\n')
cleaned_data = []

# Проход по строкам и извлечение пар "кубачинский - русский"
for line in lines:
    russian, kubanch = map(str.strip, line.split(' – '))
    cleaned_data.append((russian, kubanch))

# Преобразование в DataFrame
df = pd.DataFrame(cleaned_data, columns=['Russian', 'Kubachin'])

# Сохранение данных в CSV-файл
df.to_csv('./AI/data/processed/numbers.csv', index=False, encoding='utf-8')

# Проверка результата
print(df)