# -*- coding: utf-8 -*-

# Update update_progress_md.py
with open('/root/1CT-Share/20260828-global500/update_progress_md.py', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace("range(1, 101)", "range(1, 151)")
c = c.replace("with 100 company rows", "with 150 company rows")
c = c.replace("100 / 100 (100%)", "150 / 150 (100%)")
with open('/root/1CT-Share/20260828-global500/update_progress_md.py', 'w', encoding='utf-8') as f:
    f.write(c)

# Update update_founder_readme.py
with open('/root/1CT-Share/20260828-global500/update_founder_readme.py', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace("range(1, 101)", "range(1, 151)")
c = c.replace("with 100 company entries", "with 150 company entries")
with open('/root/1CT-Share/20260828-global500/update_founder_readme.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated update_progress_md.py & update_founder_readme.py to 150 companies!")
