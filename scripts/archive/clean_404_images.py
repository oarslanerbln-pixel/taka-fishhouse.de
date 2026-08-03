import re

index_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    c = f.read()

# Remove the missing poster attribute (in case there are multiple)
c = c.replace('poster="assets/videos/taka-video-poster.jpg"', '')

# The images might be in an img tag like: <img src="assets/hamsi_web.jpg" ...>
# Let's just find and replace the whole <img> tag if it contains these missing images
c = re.sub(r'<img[^>]*src="assets/hamsi_web\.jpg"[^>]*>', '', c)
c = re.sub(r'<img[^>]*src="assets/_DSC4138_web\.jpg"[^>]*>', '', c)

# Just in case they are used in background-image styles inline
c = c.replace("url('assets/hamsi_web.jpg')", "none")
c = c.replace("url('assets/_DSC4138_web.jpg')", "none")

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("Removed missing images from index.html")
