import json
import urllib.request
import os

with open("wolt_images.json", "r", encoding="utf-8") as f:
    data = json.load(f)

if not os.path.exists("wolt_imgs"):
    os.makedirs("wolt_imgs")

count = 0
for i, item in enumerate(data.get("imgs", [])):
    src = item.get("src")
    if src:
        try:
            filename = f"wolt_imgs/img_{i}.jpg"
            urllib.request.urlretrieve(src, filename)
            count += 1
        except Exception as e:
            pass

print(f"Downloaded {count} images")
