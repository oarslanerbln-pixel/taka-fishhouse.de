import json
import re

def parse_js_object(content):
    # This is a bit hacky, but we can extract the translations object using regex
    match = re.search(r'const translations = (\{.*?\});', content, re.DOTALL)
    if not match:
        return None
    # We can't parse JS with json.loads directly due to unquoted keys or trailing commas, 
    # but let's try to extract keys manually for each lang
    langs = ['tr', 'de', 'en', 'ru', 'es', 'ar']
    keys_by_lang = {l: set() for l in langs}
    
    for lang in langs:
        lang_block = re.search(fr'{lang}:\s*{{(.*?)\n\s*}},?\n', content, re.DOTALL)
        if lang_block:
            lines = lang_block.group(1).split('\n')
            for line in lines:
                if ':' in line:
                    key = line.split(':')[0].strip().strip('"\'')
                    if key and not key.startswith('//'):
                        keys_by_lang[lang].add(key)
    return keys_by_lang

content = open('assets/js/translations.js', 'r', encoding='utf-8').read()
keys = parse_js_object(content)
if keys:
    base_keys = keys['de']
    for lang in keys:
        if lang == 'de': continue
        missing = base_keys - keys[lang]
        extra = keys[lang] - base_keys
        print(f"Language {lang.upper()}: {len(keys[lang])} keys")
        if missing:
            print(f"  Missing {len(missing)} keys: {list(missing)[:5]}")
        if extra:
            print(f"  Extra {len(extra)} keys: {list(extra)[:5]}")
else:
    print("Could not parse translations.js")
