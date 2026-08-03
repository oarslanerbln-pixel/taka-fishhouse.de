import urllib.request
import re

url = "https://www.google.com/search?sa=X&sca_esv=8ca67e5d7398939f&rlz=1C1CHBF_deDE1173DE1173&biw=1440&bih=731&sxsrf=APpeQnsqbMy2e7jNuK2s-Ro49eSb56i5fg:1782730589462&q=Taka%20Fish%20House%20Rezensionen&rflfq=1&num=20&stick=H4sIAAAAAAAAAONgkxI2NDA3MTQxMzIxNjIzMTW3MLM03sDI-IpROiQxO1HBLbM4Q8Ejv7Q4VSEotSo1rzgzPy81bxErPlkAlrakfVYAAAA&rldimm=1074146243264578693&tbm=lcl&hl=de-DE"

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8', errors='ignore')
    
    print("Phone:", re.findall(r'(\+49[0-9\s]+)', html)[:5])
    print("Address:", re.findall(r'Kottbusser Damm \d+|Adalbertstraße \d+', html)[:5])
    print("Rating:", re.findall(r'[45],[0-9]', html)[:10])
except Exception as e:
    print("Failed", e)
