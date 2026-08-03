import sys

try:
    with open('index.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines[140:200]):
            print(f"{i+141}: {line.rstrip()}")
except Exception as e:
    print(f"Error: {e}")
