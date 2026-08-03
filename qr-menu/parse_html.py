import json
import re

with open('page.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Look for window.__PRELOADED_STATE__ or __NEXT_DATA__
match = re.search(r'id="__NEXT_DATA__" type="application/json">([^<]+)</script>', html)
if match:
    data = json.loads(match.group(1))
    with open('lieferando_next_data.json', 'w', encoding='utf-8') as out:
        json.dump(data, out, ensure_ascii=False, indent=2)
    print("Found __NEXT_DATA__")
else:
    print("No __NEXT_DATA__ found. Let's look for __PRELOADED_STATE__")
    match2 = re.search(r'window\.__PRELOADED_STATE__\s*=\s*(\{.*?\});', html)
    if match2:
        data = json.loads(match2.group(1))
        with open('lieferando_next_data.json', 'w', encoding='utf-8') as out:
            json.dump(data, out, ensure_ascii=False, indent=2)
        print("Found __PRELOADED_STATE__")
    else:
        print("Could not find state JSON")
