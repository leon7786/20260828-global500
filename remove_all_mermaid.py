# -*- coding: utf-8 -*-
import os
import re

base_dir = '/root/1CT-Share/20260828-global500'
count = 0
files_modified = 0

pattern = re.compile(r'```mermaid\s*[\r\n]+[\s\S]*?[\r\n]+```\s*[\r\n]*', re.MULTILINE)

for root, dirs, files in os.walk(base_dir):
    # skip .git
    if '.git' in root:
        continue
    for file in files:
        if file.endswith('.md'):
            fp = os.path.join(root, file)
            with open(fp, 'r', encoding='utf-8') as f:
                content = f.read()
            
            matches = pattern.findall(content)
            if matches:
                new_content = pattern.sub('', content)
                # Clean up any leftover empty trailing double dividers if any
                new_content = re.sub(r'---\s*\n\s*---\s*\n', '---\n', new_content)
                with open(fp, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                files_modified += 1
                count += len(matches)
                print(f"Removed {len(matches)} mermaid block(s) from: {os.path.relpath(fp, base_dir)}")

print(f"\nDone! Total {count} mermaid block(s) removed across {files_modified} markdown files.")
