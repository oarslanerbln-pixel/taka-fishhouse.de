import os
import subprocess
import time
from datetime import datetime, timedelta

def check_history():
    out_file = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\scratch\history_output.txt"
    with open(out_file, "w", encoding="utf-8") as f:
        # Try to run git log
        try:
            result = subprocess.run(["git", "log", "--since=3 days ago", "--stat"], capture_output=True, text=True, check=True)
            f.write("=== GIT HISTORY (Last 3 days) ===\n")
            f.write(result.stdout)
            f.write("\n\n")
        except Exception as e:
            f.write(f"Git log failed: {e}\n\n")
        
        # Check file modification times
        f.write("=== RECENTLY MODIFIED FILES (Last 3 days) ===\n")
        root_dir = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus"
        three_days_ago = time.time() - (3 * 24 * 60 * 60)
        
        for dirpath, dirnames, filenames in os.walk(root_dir):
            if '.git' in dirpath or '.venv' in dirpath or 'node_modules' in dirpath:
                continue
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    mtime = os.path.getmtime(filepath)
                    if mtime > three_days_ago:
                        mod_time_str = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
                        f.write(f"{mod_time_str} - {os.path.relpath(filepath, root_dir)}\n")
                except Exception:
                    pass

if __name__ == "__main__":
    check_history()
