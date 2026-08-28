# -*- coding: utf-8 -*-
import os, re

base_dir = '/root/1CT-Share/20260828-global500/Founder'

def streamline_intro(content):
    m = re.search(r'\n(##\s*(?:[🎬🩺🏭⚡🛒🔬🌪️🏛️🧭]*\s*)?(?:第[一1]章|01|1\.)[^\n]*)', content)
    if not m:
        m = re.search(r'\n(## [^\n]+)', content)
        
    if not m:
        return content
        
    chapter_start_idx = m.start()
    intro_part = content[:chapter_start_idx].strip()
    body_part = content[chapter_start_idx:].strip()
    
    h1_match = re.search(r'^(# [^\n]+)', intro_part)
    h1_title = h1_match.group(1).strip() if h1_match else "# 创始人全景传记"
    
    quote_matches = re.findall(r'> [“"”\']*(.*?)[”"\'\s]*\n> —— (.*?)(?:\n|$)', intro_part, flags=re.DOTALL)
    quote_line = ""
    if quote_matches:
        q_text, q_author = quote_matches[0]
        q_text = q_text.replace('**', '').replace('“', '').replace('”', '').strip()
        q_author = q_author.replace('**', '').strip()
        if len(q_text) > 75:
            q_text = q_text[:72] + "..."
        quote_line = f"\n\n> **“{q_text}”** —— {q_author}"
    else:
        simple_q = re.findall(r'> \*\*“([^”]+)”\*\*', intro_part)
        if simple_q:
            q_text = simple_q[0].strip()
            if len(q_text) > 75: q_text = q_text[:72] + "..."
            quote_line = f"\n\n> **“{q_text}”**"

    streamlined = f"{h1_title}{quote_line}\n\n---\n\n{body_part}"
    streamlined = re.sub(r'\n---\n\s*## 🧭[^\n]*\n\s*---\n', '\n---\n', streamlined)
    streamlined = re.sub(r'\n{3,}', '\n\n', streamlined)
    return streamlined

count = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.md') and not file.endswith('-backup.md'):
            fpath = os.path.join(root, file)
            with open(fpath, 'r', encoding='utf-8') as f:
                c = f.read()
            res = streamline_intro(c)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(res)
            count += 1

print(f"Batch streamlined intros across {count} active files in Founder!")
