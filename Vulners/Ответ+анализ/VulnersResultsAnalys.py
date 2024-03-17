import json
import tkinter as tk
from tkinter import filedialog

# Открываем файл с данными JSON
with open('otvet\\vul\\7\\10.json', 'r') as file:
    data = json.load(file)

# Фильтруем записи по условию, что свойство "cvelist" не пустое
filtered_data = [record for record in data['data']['search'] if record['_source'].get('cvelist')]

# Выводим нужные свойства "title", "cvelist" и "id" для отфильтрованных записей
for record in filtered_data:
    print("Title:", record['_source']['title'])
    print("CVE List:", record['_source']['cvelist'])
    print("ID:", record['_source']['id'])
    print()

# Создаем окно tkinter для выбора места сохранения файла
root = tk.Tk()

# Открываем диалоговое окно для выбора места сохранения файла
save_path = filedialog.asksaveasfilename(parent=root, defaultextension=".txt", filetypes=[("Text files", "*.txt")])

# Сохраняем результаты в указанном месте
with open(save_path, 'w') as output_file:
    for record in filtered_data:
        output_file.write("Title: " + record['_source']['title'] + "\n")
        output_file.write("CVE List: " + str(record['_source']['cvelist']) + "\n")
        output_file.write("ID: " + record['_source']['id'] + "\n\n")

print("Результаты сохранены в файл по выбранному пути.")