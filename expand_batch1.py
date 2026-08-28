# -*- coding: utf-8 -*-
"""Expand Batch 1 (Rank 003-010) founder.md to full 25KB-38KB standard"""

import os

base_dir = "/root/1CT-Share/20260828-global500/Founder"

def write_founder(dir_name, content):
    target = os.path.join(base_dir, dir_name, "founder.md")
    with open(target, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Updated {dir_name}/founder.md -> {len(content.encode('utf-8')):,} bytes")

