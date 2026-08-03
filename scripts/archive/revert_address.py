import os

files_to_update = [
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\index.html",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\index.html"
]

for file_path in files_to_update:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Adresi geri Kottbusser Damm'a ceviriyoruz
    content = content.replace("Adalbertstraße 97", "Kottbusser Damm 35")
    content = content.replace("10999 Berlin", "10967 Berlin")
    
    # Harita linkini guncelliyoruz
    content = content.replace("Adalbertstra%C3%9Fe%2097%2C%2010999%20Berlin", "Kottbusser%20Damm%2035%2C%2010967%20Berlin")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Address and maps reverted to Kottbusser Damm 35.")
