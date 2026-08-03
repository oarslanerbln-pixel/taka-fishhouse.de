import os

def fix_html():
    file_path = '../index.html'
    if not os.path.exists(file_path):
        file_path = 'index.html'
        
    with open(file_path, 'rb') as f:
        content = f.read().decode('utf-8', errors='ignore')
    
    # Ensure </section> is present before the story section
    story_marker = '<!-- ============================\r\n     STORY / ABOUT SECTION'
    story_marker_alt = '<!-- ============================\n     STORY / ABOUT SECTION'
    
    marker = story_marker if story_marker in content else story_marker_alt
    
    if marker in content:
        # Check if it's already preceded by </section>
        idx = content.find(marker)
        before_marker = content[max(0, idx-20):idx]
        if '</section>' not in before_marker:
            content = content.replace(marker, '</section>\n\n' + marker)
            print("Successfully added missing </section> before the Story section.")
        else:
            print("The </section> tag is already present.")
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed index.html encoding successfully.")

if __name__ == '__main__':
    fix_html()
