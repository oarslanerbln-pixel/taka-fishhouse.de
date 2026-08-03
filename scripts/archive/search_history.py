import os
import glob
from datetime import datetime

history_dir = r"c:\Users\oarsl\AppData\Roaming\Cursor\User\History"
if not os.path.exists(history_dir):
    print("No Cursor history found.")
else:
    print("Searching in Cursor History...")
    count = 0
    # Walk all files
    for root, dirs, files in os.walk(history_dir):
        for f in files:
            path = os.path.join(root, f)
            try:
                # check modification time
                mtime = os.path.getmtime(path)
                # Only check files modified today
                if datetime.fromtimestamp(mtime).date() == datetime.today().date():
                    with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                        content = file.read(5000)
                        if "premium-splash" in content or "TAKA Fish House" in content or "karadenizSplash" in content:
                            print(f"FOUND MATCH IN: {path} (Modified: {datetime.fromtimestamp(mtime)})")
                            count += 1
            except Exception:
                pass
    print(f"Total found: {count}")
