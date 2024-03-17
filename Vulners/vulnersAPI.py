import requests
import json
import tkinter as tk
from tkinter import filedialog

file = [
    {"Program": "LibreOffice", "Version": "6.0.7"},
    {"Program": "7zip", "Version": "18.05"},
    {"Program": "Adobe Reader", "Version": "2018.011.20035"},
    {"Program": "nginx", "Version": "1.14.0"},
    {"Program": "Apache HTTP Server", "Version": "2.4.29"},
    {"Program": "DjVu Reader", "Version": "2.0.0.27"},
    {"Program": "Wireshark", "Version": "2.6.1"},
    {"Program": "Notepad++", "Version": "7.5.6"},
    {"Program": "Google Chrome", "Version": "68.0.3440.106"},
    {"Program": "Mozilla Firefox", "Version": "61.0.1"}
]
def save_to_file(file_path, data):
    with open(file_path, 'a') as f:
        json.dump(data, f, indent=4)

for i in file:
    Program = i["Program"]
    Version = i["Version"]
    
    url = 'https://vulners.com/api/v3/search/lucene/'
    data = {
        "query": Program ,
        "Version": Version, 
        "apiKey": "123" 
    }
        response = requests.post(url, json=data)
    assert response.status_code == 200, f"Unexpected statuscode: {response.status_code}"
#сохраняем в файл через диалоговое окно
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.asksaveasfilename(defaultextension=".json")
    
    if file_path:
        if file_path.endswith(".json"):
            save_to_file(file_path, response.json())
        else:
            file_path += ".json"
            save_to_file(file_path, response.json())
    
    root.destroy()