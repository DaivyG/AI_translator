import pandas as pd

# Пример исходных данных
with open('./AI/data/raw/words.txt', encoding='utf-8') as f:
    data = f.read()

# Разделение на строки и удаление скобок и их содержимого
lines = data.split('\n')
cleaned_data = []
for line in lines:
    # Разделение по синонимам
    pairs = line.split('.')
    for pair in pairs:
        if not pair:
            continue
        if '–' in pair:
            russian, kubachin = map(str.strip, pair.split('–'))
        if ',' in kubachin:
            values = map(str.strip, kubachin.split(','))
            for value in values:
                cleaned_data.append((russian, value))
        elif '/' in kubachin:
            values = map(str.strip, kubachin.split('/'))
            for value in values:
                cleaned_data.append((russian, value))
        else:
            cleaned_data.append((russian, kubachin))

# Преобразование в DataFrame для сохранения в CSV
df = pd.DataFrame(cleaned_data, columns=['Russian', 'Kubachin'])

df.to_csv('./AI/data/processed/words.csv', index=False, encoding='utf-8')