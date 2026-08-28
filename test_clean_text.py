# -*- coding: utf-8 -*-
import os, re

def transform_ascii_to_native_markdown(text):
    # Regex to find all ```text ... ``` and ``` ... ```
    def convert_block(match):
        raw = match.group(1).strip()
        lines = [l for l in raw.split('\n') if l.strip()]
        
        # Detect if it's a table with pipes like | 1952年 | 事件 |
        is_table = False
        table_rows = []
        for l in lines:
            if re.match(r'^[=\-\+]{5,}$', l.strip()):
                continue
            if '|' in l:
                # check if line has columns
                parts = [p.strip() for p in l.split('|') if p.strip()]
                if len(parts) >= 2:
                    is_table = True
                    table_rows.append(parts)

        if is_table and len(table_rows) >= 3 and any(('年' in r[0] or '19' in r[0] or '20' in r[0] or '年份' in r[0] or '模型' in r[0] or '红利' in r[0]) for r in table_rows):
            # Render as native markdown table
            header = table_rows[0]
            # check if header is actual header or title
            if len(header) == 1:
                title = header[0]
                rows = table_rows[1:]
                out = [f"> ### 📊 {title}\n"]
                if rows:
                    if len(rows[0]) == 2:
                        out.append("| 年份 / 主题 | 核心历史事件与战略影响 |")
                        out.append("| :--- | :--- |")
                    elif len(rows[0]) == 3:
                        out.append("| 序号 / 年份 | 关键历史节点 | 商业战略影响 |")
                        out.append("| :--- | :--- | :--- |")
                    else:
                        cols = [f"字段{i+1}" for i in range(len(rows[0]))]
                        out.append("| " + " | ".join(cols) + " |")
                        out.append("| " + " | ".join([":---"] * len(cols)) + " |")
                    for r in rows:
                        out.append("| " + " | ".join([f"**{r[0]}**"] + r[1:]) + " |")
                return "\n".join(out)
            else:
                out = ["| " + " | ".join(header) + " |"]
                out.append("| " + " | ".join([":---"] * len(header)) + " |")
                for r in table_rows[1:]:
                    if len(r) == len(header):
                        out.append("| " + " | ".join([f"**{r[0]}**"] + r[1:]) + " |")
                    elif len(r) > len(header):
                        merged = [r[0]] + r[1:len(header)-1] + [" - ".join(r[len(header)-1:])]
                        out.append("| " + " | ".join([f"**{merged[0]}**"] + merged[1:]) + " |")
                return "\n".join(out)

        # Otherwise format as clean callout card (> ...)
        cleaned_lines = []
        for l in lines:
            if re.match(r'^[=\-\+]{5,}$', l.strip()):
                continue
            m_pipe = re.match(r'^\|\s*(.*?)\s*\|$', l.strip())
            if m_pipe:
                c = m_pipe.group(1).strip()
                if c: cleaned_lines.append(c)
            else:
                cleaned_lines.append(l.strip())
        
        out = []
        for l in cleaned_lines:
            if not l: continue
            if any(l.startswith(k) for k in ['【传主', '【双星', '【双奠基', '【联合健康', '【中国石油', '【核心', '【中国能源']):
                out.append(f"> ### 📋 {l}")
            elif l.startswith('•') or l.startswith('-'):
                out.append(f"> {l}")
            elif ('：' in l or ':' in l) and not l.startswith('http'):
                parts = re.split(r'[:：]', l, maxsplit=1)
                out.append(f"> - **{parts[0].strip()}**：{parts[1].strip()}")
            else:
                out.append(f"> **{l}**" if ('——' in l or '历史' in l or '名场面' in l) else f"> {l}")
        return "\n".join(out)

    content = re.sub(r'```text\s*(.*?)\s*```', convert_block, text, flags=re.DOTALL)
    content = re.sub(r'```\s*(.*?)\s*```', convert_block, content, flags=re.DOTALL)
    return content

# Test on Top 2 Walmart
p = '/root/1CT-Share/20260828-global500/Founder/002-沃尔玛-Walmart/founder.md'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

res = transform_ascii_to_native_markdown(text)
print("Walmart original ``` count:", text.count("```"))
print("Walmart cleaned ``` count:", res.count("```"))
print("\n--- SAMPLE RESULT (Lines 1 to 45) ---")
print("\n".join(res.split("\n")[:45]))
