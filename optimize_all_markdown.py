# -*- coding: utf-8 -*-
import os
import re

base_dir = '/root/1CT-Share/20260828-global500/Founder'
modified = 0

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.md'):
            fp = os.path.join(root, file)
            with open(fp, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # 1. Remove empty Chronological Epic section if it has no content
            content = re.sub(
                r'## 🧭 全景生命历程与重大历史决断编年轴.*?\n+---\s*\n+',
                '',
                content,
                flags=re.DOTALL
            )
            content = re.sub(
                r'## 🧭 全景生命历程与重大历史决断编年轴.*?\n+(?=## )',
                '',
                content,
                flags=re.DOTALL
            )

            # 2. Clean up multiple consecutive dividers
            content = re.sub(r'---\s*\n(\s*---\s*\n)+', '---\n\n', content)
            content = re.sub(r'\n{3,}', '\n\n', content)

            if content != original:
                with open(fp, 'w', encoding='utf-8') as f:
                    f.write(content.strip() + '\n')
                modified += 1

print(f"Optimized markdown formatting across {modified} files!")
