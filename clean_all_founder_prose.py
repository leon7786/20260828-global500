# -*- coding: utf-8 -*-
import os, re

base_dir = '/root/1CT-Share/20260828-global500/Founder'

def clean_markdown_prose(content):
    lines = content.split('\n')
    cleaned = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Keep opening golden quote directly under H1 (first 15 lines only)
        if i < 15 and (stripped.startswith('> **“') or stripped.startswith('> “') or stripped.startswith('> ——') or stripped.startswith('> --') or stripped.startswith('> **“宁') or stripped.startswith('> **“我们')):
            cleaned.append(line)
            continue
            
        # Strip blockquote prefix '>' anywhere else in the body
        if stripped.startswith('> '):
            unquoted = stripped[2:].strip()
            if unquoted.startswith('### '):
                cleaned.append('')
                cleaned.append(unquoted.replace('【', '').replace('】', ''))
            elif unquoted.startswith('**') and unquoted.endswith('**') and len(unquoted) < 40:
                cleaned.append('')
                cleaned.append(f"**{unquoted.replace('**', '')}**")
            elif unquoted.startswith('- ') or unquoted.startswith('• ') or unquoted.startswith('* '):
                cleaned.append(unquoted)
            elif unquoted.startswith('|'):
                cleaned.append(unquoted)
            else:
                cleaned.append(unquoted)
        elif stripped == '>':
            cleaned.append('')
        else:
            cleaned.append(line)
            
    result = '\n'.join(cleaned)
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result

cleaned_count = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.md') and not file.endswith('-backup.md'):
            fpath = os.path.join(root, file)
            with open(fpath, 'r', encoding='utf-8') as f:
                c = f.read()
            res = clean_markdown_prose(c)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(res)
            cleaned_count += 1

print(f"Successfully removed all body blockquotes and yellow box markers across {cleaned_count} active files in Founder!")
