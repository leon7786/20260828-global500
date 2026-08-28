# -*- coding: utf-8 -*-
import os, re

base_dir = '/root/1CT-Share/20260828-global500/Founder'

def clean_markdown_prose(content):
    lines = content.split('\n')
    cleaned = []
    
    in_opening_quote = False
    quote_count = 0
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Check if line is the top opening quote right under H1
        if i < 15 and (stripped.startswith('> **“') or stripped.startswith('> “') or stripped.startswith('> ——') or stripped.startswith('> --')):
            cleaned.append(line)
            continue
            
        # If line starts with '> ### 📋' or '> -' or '> •' or other '>' blockquote markers inside the body
        if stripped.startswith('> '):
            unquoted = stripped[2:].strip()
            # If it was a header like > ### 📋 【传主档案速览】 -> ### 📋 传主档案速览
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
            # empty quote line
            cleaned.append('')
        else:
            cleaned.append(line)
            
    result = '\n'.join(cleaned)
    # clean up multiple empty lines
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result

# Test on 001, 002, 003
for fld in ['001-亚马逊-Amazon', '002-沃尔玛-Walmart', '003-国家电网-StateGrid']:
    p = os.path.join(base_dir, fld, 'founder.md')
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        res = clean_markdown_prose(c)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(res)
        print(f"Cleaned {fld}: remaining '>' lines = {len([l for l in res.splitlines() if l.startswith('>')])}")

