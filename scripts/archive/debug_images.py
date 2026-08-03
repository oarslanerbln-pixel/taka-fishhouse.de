import re, os, sys

sys.stdout.reconfigure(encoding='utf-8')

MENU_FILE = 'assets/js/menu-data.js'
BASE_DIR = os.getcwd()

with open(MENU_FILE, 'r', encoding='utf-8') as f:
    raw = f.read()

# Find all items with image fields
# Pattern: nameTR before image
items_forward = re.findall(
    r'"nameTR"\s*:\s*"([^"]+)"[^}]{0,300}?"image"\s*:\s*"([^"]+)"',
    raw, re.DOTALL
)
items_backward = re.findall(
    r'"image"\s*:\s*"([^"]+)"[^}]{0,300}?"nameTR"\s*:\s*"([^"]+)"',
    raw, re.DOTALL
)

all_items = {}
for name, img in items_forward:
    all_items[name.strip()] = img.strip()
for img, name in items_backward:
    if name.strip() not in all_items:
        all_items[name.strip()] = img.strip()

missing_local = []
external_urls = []
ok_local = []

for name, img in sorted(all_items.items()):
    if img.startswith('http'):
        external_urls.append((name, img))
    else:
        local_path = os.path.join(BASE_DIR, img.replace('/', os.sep))
        if os.path.exists(local_path):
            ok_local.append((name, img))
        else:
            missing_local.append((name, img))

print('=== MISSING LOCAL FILES (%d) ===' % len(missing_local))
for name, img in missing_local:
    print('  MISSING: %-45s -> %s' % (name[:45], img))

print()
print('=== EXTERNAL URLs (%d) ===' % len(external_urls))
for name, img in external_urls:
    print('  EXT: %-45s -> %s' % (name[:45], img[:70]))

print()
print('=== OK LOCAL (%d) ===' % len(ok_local))
for name, img in ok_local:
    print('  OK:  %-45s -> %s' % (name[:45], img))

print()
print('SUMMARY: %d OK | %d External | %d MISSING' % (len(ok_local), len(external_urls), len(missing_local)))
