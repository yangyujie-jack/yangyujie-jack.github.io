import os   
import re
out_dir = r'_publications'
files = [f for f in os.listdir(out_dir) if f.endswith('.md')]
for file in files:
    path = os.path.join(out_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'venue: \"\*(.*?)\*\s*(.*?)?\"', r'venue: \"\1 \2\"', content)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
print('Done!')
