# -*- coding: utf-8 -*-
import os, re

base_dir = '/root/1CT-Share/20260828-global500/Founder'

def streamline_intro(content):
    # Find the start of the first actual narrative chapter (e.g. ## 第一章, ## 🎬 第一章, ## 🩺 第一章, ## 1., etc.)
    m = re.search(r'\n(##\s*(?:[🎬🩺🏭⚡🛒🔬🌪️🏛️🧭]*\s*)?(?:第[一1]章|01|1\.)[^\n]*)', content)
    if not m:
        m = re.search(r'\n(## [^\n]+)', content)
        
    if not m:
        return content
        
    chapter_start_idx = m.start()
    intro_part = content[:chapter_start_idx].strip()
    body_part = content[chapter_start_idx:].strip()
    
    # Extract H1
    h1_match = re.search(r'^(# [^\n]+)', intro_part)
    h1_title = h1_match.group(1).strip() if h1_match else "# 创始人全景传记"
    
    # Extract the best single concise quote (under 70 words)
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
        # Check simple quote
        simple_q = re.findall(r'> \*\*“([^”]+)”\*\*', intro_part)
        if simple_q:
            q_text = simple_q[0].strip()
            if len(q_text) > 75: q_text = q_text[:72] + "..."
            quote_line = f"\n\n> **“{q_text}”**"

    # Assemble streamlined document
    streamlined = f"{h1_title}{quote_line}\n\n---\n\n{body_part}"
    
    # Clean up any leftover '🧭 全景生命历程' or standalone empty dividers
    streamlined = re.sub(r'\n---\n\s*## 🧭[^\n]*\n\s*---\n', '\n---\n', streamlined)
    streamlined = re.sub(r'\n{3,}', '\n\n', streamlined)
    return streamlined

# Test on Top 1 to 10
for i in range(1, 11):
    dirs = [d for d in os.listdir(base_dir) if d.startswith(f"{i:03d}-")]
    if dirs:
        d = dirs[0]
        fpath = os.path.join(base_dir, d, "founder.md")
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
        res = streamline_intro(c)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(res)
        print(f"Streamlined intro for {d}: new length = {len(res.encode('utf-8'))} bytes")

