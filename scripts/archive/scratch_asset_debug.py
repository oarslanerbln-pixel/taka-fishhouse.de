import os
import re
from urllib.parse import urlparse

ROOT_DIR = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus'

def check_html_file(filepath):
    errors = []
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Find all src and href attributes
    pattern = re.compile(r'(?:src|href|poster)=["\']([^"\']+)["\']')
    matches = pattern.findall(content)

    for match in matches:
        # Ignore external links and data uris
        if match.startswith('http') or match.startswith('data:') or match.startswith('mailto:') or match.startswith('tel:') or match.startswith('#'):
            continue
            
        # Ignore query params (e.g. style.css?v=1.0)
        clean_match = match.split('?')[0].split('#')[0]
        
        # Calculate absolute path based on the html file location
        base_dir = os.path.dirname(filepath)
        target_path = os.path.normpath(os.path.join(base_dir, clean_match))
        
        if not os.path.exists(target_path):
            errors.append(f"Missing asset in {os.path.relpath(filepath, ROOT_DIR)}: {match} (Expected: {target_path})")

    return errors

def check_css_file(filepath):
    errors = []
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Find all url(...)
    pattern = re.compile(r'url\((?:["\']?)(.*?)(?:["\']?)\)')
    matches = pattern.findall(content)

    for match in matches:
        if match.startswith('http') or match.startswith('data:'):
            continue
            
        clean_match = match.split('?')[0].split('#')[0]
        base_dir = os.path.dirname(filepath)
        target_path = os.path.normpath(os.path.join(base_dir, clean_match))
        
        if not os.path.exists(target_path):
            errors.append(f"Missing asset in {os.path.relpath(filepath, ROOT_DIR)}: {match} (Expected: {target_path})")

    return errors

all_errors = []

for root, _, files in os.walk(ROOT_DIR):
    # skip .git, .vercel, node_modules etc
    if '.git' in root or '.vercel' in root or 'node_modules' in root:
        continue
        
    for file in files:
        filepath = os.path.join(root, file)
        if file.endswith('.html'):
            all_errors.extend(check_html_file(filepath))
        elif file.endswith('.css'):
            all_errors.extend(check_css_file(filepath))

if all_errors:
    print("\n--- ASSET DEBUG REPORT ---")
    for error in all_errors:
        print(error)
else:
    print("\n--- ASSET DEBUG REPORT ---")
    print("No missing local assets found in HTML or CSS!")
