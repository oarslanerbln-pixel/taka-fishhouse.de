import json

with open("lieferando_nextdata.json", "r", encoding="utf-8") as f:
    data = json.load(f)

pp = data.get("props", {}).get("pageProps", {})
print("pageProps keys:", list(pp.keys()))

# Dig deeper
for k, v in pp.items():
    if isinstance(v, dict):
        print(f"  {k} (dict): {list(v.keys())[:8]}")
    elif isinstance(v, list):
        print(f"  {k} (list): len={len(v)}")
    else:
        print(f"  {k}: {str(v)[:80]}")
