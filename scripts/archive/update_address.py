import os
import re

files_to_update_address = [
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\index.html",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\index.html"
]

for file_path in files_to_update_address:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Adres degisimi
    content = content.replace("Kottbusser Damm 35", "Adalbertstraße 97")
    content = content.replace("10967 Berlin", "10999 Berlin")
    
    # Eger durak adi varsa onu da güncelleyelim - Adalbertstrasse'ye yakin u-bahn duragi Kottbusser Tor
    # Gerci Kottbusser Tor ayni zamanda Adalbertstrasse'nin bitisigi, o yuzden metro duragi olarak "Kottbusser Tor (U1, U3, U8)" kalsin veya degissin. 
    # Kottbusser Tor (U8) geciyordu. Kalsin o mantikli.
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Addresses updated.")
