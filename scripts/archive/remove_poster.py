import os

index_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    c = f.read()

# Remove the missing poster attribute to avoid 404
c = c.replace('poster="assets/videos/taka-video-poster.jpg"', '')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("Removed missing poster.")
