# -*- coding: utf-8 -*-
import os, re

def streamline_intro(content):
    # Split by the first major chapter heading ## 第一章
    m = re.search(r'\n(## 第一章[^\n]*)', content)
    if not m:
        # try without space or different format
        m = re.search(r'\n(## [0-9一两二三四五六七八九十]+[^\n]*)', content)
        
    if not m:
        return content
        
    chapter_start_idx = m.start()
    intro_part = content[:chapter_start_idx].strip()
    body_part = content[chapter_start_idx:].strip()
    
    # Extract H1
    h1_match = re.search(r'^(# [^\n]+)', intro_part)
    h1_title = h1_match.group(1) if h1_match else "# 创始人全景史诗传记"
    
    # Extract concise quote if exists (under 120 chars)
    quote_matches = re.findall(r'> [“"”\']*(.*?)[”"\'\s]*\n> —— (.*?)\n', intro_part, flags=re.DOTALL)
    quote_text = ""
    if quote_matches:
        q_content, q_author = quote_matches[0]
        q_content_clean = q_content.replace('**', '').replace('“', '').replace('”', '').strip()
        if len(q_content_clean) > 80:
            q_content_clean = q_content_clean[:78] + "..."
        quote_text = f"\n\n> **“{q_content_clean}”** —— {q_author.strip()}"
    else:
        # check simple quote
        simple_q = re.findall(r'> \*\*“([^”]+)”\*\*', intro_part)
        if simple_q:
            q_clean = simple_q[0].strip()
            if len(q_clean) > 80: q_clean = q_clean[:78] + "..."
            quote_text = f"\n\n> **“{q_clean}”**"

    # Assemble streamlined header
    new_intro = f"{h1_title}{quote_text}\n\n---\n\n{body_part}"
    return new_intro

# Test on 004 UnitedHealth
p = '/root/1CT-Share/20260828-global500/Founder/004-联合健康-UnitedHealth/founder.md'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

res = streamline_intro(text)
print("=== RESULT FOR 004 UnitedHealth (First 35 lines) ===")
print("\n".join(res.split("\n")[:35]))
