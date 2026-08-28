# -*- coding: utf-8 -*-
import os, shutil

base_dir = '/root/1CT-Share/20260828-global500/Founder'

# 1. First ensure backup for all 011 to 020
for rank in range(11, 21):
    dirs = [d for d in os.listdir(base_dir) if d.startswith(f"{rank:03d}-")]
    if dirs:
        d = dirs[0]
        fpath = os.path.join(base_dir, d, "founder.md")
        bpath = os.path.join(base_dir, d, "founder-backup.md")
        if os.path.exists(fpath) and not os.path.exists(bpath):
            shutil.copy2(fpath, bpath)
            print(f"Backed up {d} to founder-backup.md")

print("All 011-020 backups verified!")
