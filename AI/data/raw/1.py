import pandas as pd

# Замените 'input.xlsx' на путь к вашему Excel файлу
excel_file_path = './AI/data/raw/phrases.xlsx'
# Замените 'output.csv' на желаемое имя выходного CSV файла
csv_file_path = './AI/data/processed/phrase.csv'

# Чтение Excel файла
df = pd.read_excel(excel_file_path)

# Сохранение в CSV формате
df.to_csv(csv_file_path, index=False)