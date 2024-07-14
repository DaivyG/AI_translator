input_file = './AI/data/raw/file.txt'
output_file = './AI/data/processed/processed_dataset.txt'

# Открываем файлы для чтения и записи
with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
    lines = f_in.readlines()
    
    for line in lines:
        line = line.strip()
        if '(' in line and ')' in line:
            # Находим позиции скобок
            start_idx = line.index('(')
            end_idx = line.index(')')
            
            # Разделяем фразы
            first_phrase = line[:start_idx].strip()
            second_phrase = line[start_idx+1:end_idx].strip()
            
            # Записываем обе фразы в новый файл
            f_out.write(first_phrase + '\n')
            f_out.write(second_phrase + '\n')
        else:
            # Если скобок нет, просто записываем строку
            f_out.write(line + '\n')

print(f"Файл {output_file} успешно создан.")
