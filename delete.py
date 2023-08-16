import os

# Путь к директории, где находятся файлы
directory = './'

# Получаем список файлов в директории
files = os.listdir(directory)

# Удаляем файлы с измененными адресами
for file in files:
    if file.startswith('output_file_') and file.endswith('.jpg'):
        file_path = os.path.join(directory, file)
        os.remove(file_path)
        print(f'Удален файл: {file_path}')

print('Готово!')