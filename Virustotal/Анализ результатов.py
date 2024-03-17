import json

# Открываем файл JSON
with open('otvet\VT2.json', 'r') as file:
    data = json.load(file)

# Фильтруем записи, где свойство "category" равно "malicious"
filtered_data = [entry['data']['attributes']['last_analysis_results'][key] for entry in data for key in entry['data']['attributes']['last_analysis_results'] if entry['data']['attributes']['last_analysis_results'][key]['category'] == 'malicious']

# Выводим нужные свойства "engine_name", "category" и "result"
for entry in filtered_data:
    print(f"Engine Name: {entry['engine_name']}, Category: {entry['category']}, Result: {entry['result']}")
