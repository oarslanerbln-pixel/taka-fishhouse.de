import os
import re
from urllib.parse import urlparse

html_file = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\index.html"
base_dir = os.path.dirname(html_file)

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Bulunacak elementler: img src, video src, source src, a href, link href
img_srcs = re.findall(r'<img[^>]+src=["\'](.*?)["\']', content)
video_srcs = re.findall(r'<video[^>]+src=["\'](.*?)["\']', content)
source_srcs = re.findall(r'<source[^>]+src=["\'](.*?)["\']', content)
video_posters = re.findall(r'<video[^>]+poster=["\'](.*?)["\']', content)
a_hrefs = re.findall(r'<a[^>]+href=["\'](.*?)["\']', content)
link_hrefs = re.findall(r'<link[^>]+href=["\'](.*?)["\']', content)

def check_local_asset(url, asset_type):
    if url.startswith('http') or url.startswith('mailto:') or url.startswith('tel:') or url.startswith('#'):
        return None # Harici veya link
    
    # URL query/hash parametrelerini at
    path = url.split('?')[0].split('#')[0]
    if not path:
        return None
        
    full_path = os.path.join(base_dir, path.replace('/', os.sep))
    if not os.path.exists(full_path):
        return f"[{asset_type}] MISSING: {url}"
    return None

issues = []

# Asset checks
all_assets = []
all_assets.extend([("IMG", s) for s in img_srcs])
all_assets.extend([("VIDEO", s) for s in video_srcs])
all_assets.extend([("SOURCE", s) for s in source_srcs])
all_assets.extend([("POSTER", s) for s in video_posters])
all_assets.extend([("STYLESHEET/ICON", s) for s in link_hrefs])

for atype, url in all_assets:
    issue = check_local_asset(url, atype)
    if issue and issue not in issues:
        issues.append(issue)

# Placeholder checks
if "Lorem ipsum" in content or "lorem ipsum" in content.lower():
    issues.append("[CONTENT] Found 'Lorem ipsum' placeholder text.")
    
empty_links = [h for h in a_hrefs if h == '#' or h == '']
if empty_links:
    issues.append(f"[LINK] Found {len(empty_links)} empty links ('#' or empty).")

# specific structural checks
if "DE XXX XXX XXX" in content:
    issues.append("[CONTENT] Found placeholder VAT ID (DE XXX XXX XXX).")

print("--- AUDIT RESULTS FOR index.html ---")
if issues:
    for i in issues:
        print(i)
else:
    print("No obvious missing assets or placeholders found.")

