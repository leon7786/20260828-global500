# -*- coding: utf-8 -*-
import os, json

with open('/root/1CT-Share/20260828-global500/build_site_data.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Let's check how brand_meta is structured in build_site_data.py
from setup_101_to_150 import companies_101_150

extra_meta = ""
for rank, info in companies_101_150.items():
    extra_meta += f"    {rank}: {{'domain': '{info['domain']}', 'color': '{info['color']}', 'bg': '{info['bg']}'}},\n"

# Replace the range(1, 101) with range(1, 151)
code = code.replace("range(1, 101)", "range(1, 151)")
code = code.replace("for rank in range(1, 101):", "for rank in range(1, 151):")
code = code.replace("Generated site_data.json with 100 companies!", "Generated site_data.json with 150 companies!")

# Insert extra_meta into brand_meta
target_str = "    100: {'domain': 'baowugroup.com', 'color': '#00338D', 'bg': 'bg-blue-900'},"
if target_str in code:
    code = code.replace(target_str, target_str + "\n" + extra_meta)

with open('/root/1CT-Share/20260828-global500/build_site_data.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_site_data.py to 150 companies!")
