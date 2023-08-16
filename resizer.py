import os

# Читаем исходный файл
with open('1.jpg', 'rb') as file:
    data = bytearray(file.read())

# Заменяем адрес в шестнадцатеричном формате
for i in range(256):
    new_address = i.to_bytes(1, 'big')  # Преобразуем число в байтовое значение
    data[0x000000E3:0x000000E4] = new_address

    # Создаем новый файл с измененным адресом
    new_filename = f'output_file_{i:02X}.jpg'
    with open(new_filename, 'wb') as new_file:
        new_file.write(data)

    print(f'Создан файл: {new_filename}')

print('Готово!')