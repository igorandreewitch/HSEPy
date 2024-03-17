import hashlib
import json
import os
import shutil
import tempfile
import zipfile
import requests
import tkinter as tk
from tkinter import filedialog

# вычисляем хеш файла
def calculate_file_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()

# взаимодействие с API
def scan_file(file_path):
    file_hash = calculate_file_hash(file_path)
    api_url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {"x-apikey": "123"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка: {response.status_code} - {response.text}")
        return None

# Сохранение результатов в файл 
def save_result_to_file(result):
    file_path = filedialog.asksaveasfilename(defaultextension=".json")
    if file_path:
        with open(file_path, "w") as f:
            json.dump(result, f, indent=4)

# разархиватор
def scan_zip_archive(file_path, password=None):
    temp_dir = tempfile.TemporaryDirectory()

    with zipfile.ZipFile(file_path, 'r') as z:
        if password:
            z.setpassword(password.encode())
        z.extractall(temp_dir.name)

# выводим результат
    results = []
    for root, dirs, files in os.walk(temp_dir.name):
        for file in files:
            file_path = os.path.join(root, file)
            result = scan_file(file_path)
            if result:
                results.append(result)

        shutil.rmtree(temp_dir.name)

    if results:
        save_result_to_file(results)

    return results

def main():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    if file_path:
        if file_path.lower().endswith(".zip"):
            password = tk.simpledialog.askstring(title="Пароль", prompt="Введите пароль:")
            if password:
                scan_zip_archive(file_path, password)
            else:
                print("Архив запаролен, введите пароль.")
        else:
            result = scan_file(file_path)
            if result:
                save_result_to_file(result)

    root.mainloop()

if __name__ == "__main__":
    main()