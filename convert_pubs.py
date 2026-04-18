import os
import re

input_file = r"d:\iDLab\code\yangyujie-jack.github.io\_pages\publications.md"
out_dir = r"d:\iDLab\code\yangyujie-jack.github.io\_publications"

os.makedirs(out_dir, exist_ok=True)

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

entries = content.split('\n\n')
count = 0
for i, e in enumerate(entries):
    e = e.strip()
    if not e.startswith('**') or "On the Equilibrium between Feasible Zone" in e:
        continue
    
    lines = [L.strip() for L in e.split('\n')]
    title = re.sub(r'^\*\*', '', lines[0]) 
    title = re.sub(r'\*\*\\?$', '', title)
    title = title.replace('**', '').replace('\\', '').replace('"', '\\"').strip()
    
    authors = lines[1].replace('\\', '').strip()
    
    venue_line = lines[2].replace('\\', '').strip()
    matches = re.findall(r'\d{4}', venue_line)
    year = matches[-1] if matches else '2000'
    venue = venue_line.replace(f', {year}', '')
    venue = re.sub(r',?$', '', venue.strip()).replace('"', '\\"')
    venue = re.sub(r'\*([^*(]+?)\s*\(([^)]+)\)\s*\*', r'*\1* (**\2**)', venue)
    
    paperurl = ''
    codeurl = ''
    website = ''
    if len(lines) > 3:
        links = ' '.join(lines[3:])
        if '[paper]' in links:
            m = re.search(r'\[paper\]\((.*?)\)', links)
            if m: paperurl = m.group(1)
        if '[code]' in links:
            m = re.search(r'\[code\]\((.*?)\)', links)
            if m: codeurl = m.group(1)
        if '[website]' in links:
            m = re.search(r'\[website\]\((.*?)\)', links)
            if m: website = m.group(1)

    slug = re.sub(r'[^a-zA-Z0-9]', '-', title.split()[:5]).lower() if isinstance(title.split()[:5], str) else '-'.join(title.split()[:5]).lower()
    slug = re.sub(r'[^a-z0-9]', '-', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    
    month_val = 12 - (i % 12)
    day_val = 28 - (i % 28)
    date_str = f"{year}-{month_val:02d}-{day_val:02d}"

    front_matter = [
        '---',
        f'title: "{title}"',
        'collection: publications',
        f'permalink: /publication/{date_str}-{slug}',
        f'date: {date_str}',
        f'collection_order: {i}',
        f'venue: "{venue}"',
        f'authors: "{authors}"',
    ]
    if "On the Equilibrium between Feasible Zone and Uncertain Model in Safe Exploration" in title:
        front_matter.extend([
            'header:',
            '  teaser: "pub_safe_exploration.png"'
        ])
    if paperurl: front_matter.append(f'paperurl: "{paperurl}"')
    if website: front_matter.append(f'website: "{website}"')
    if codeurl: front_matter.append(f'codeurl: "{codeurl}"')
    front_matter.append('---')
    front_matter.append('')

    filename = os.path.join(out_dir, f"{date_str}-{slug}.md")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(front_matter))
    count += 1

print(f"Processed {count} files.")