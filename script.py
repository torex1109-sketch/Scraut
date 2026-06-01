import requests
import json

pdf_url = "https://github.com/progit/progit2/releases/download/2.1.449/progit.pdf"
response_pdf = requests.get(pdf_url)
with open("progit.pdf", "wb") as pdf_file:
    pdf_file.write(response_pdf.content)

json_url = "http://api.open-notify.org/astros.json"
response_json = requests.get(json_url)
data = response_json.json()
with open("astros.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print("Всі завдання виконано успішно. Файли збережено!")