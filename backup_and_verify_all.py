# -*- coding: utf-8 -*-
import os
import shutil

base_dir = '/root/1CT-Share/20260828-global500/Founder'

dirs = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and d[:3].isdigit()])

print(f"Total founder directories: {len(dirs)}")

missing_bios = []
total_bytes = 0

for d in dirs:
    fpath = os.path.join(base_dir, d, 'founder.md')
    bpath = os.path.join(base_dir, d, 'founder-backup.md')
    if not os.path.exists(fpath):
        missing_bios.append(d)
    else:
        sz = os.path.getsize(fpath)
        total_bytes += sz
        # backup
        shutil.copyfile(fpath, bpath)

print(f"Verified files: {len(dirs) - len(missing_bios)} / {len(dirs)}")
if missing_bios:
    print(f"Missing biographies: {missing_bios}")
else:
    print(f"All {len(dirs)} biographies verified and backed up to founder-backup.md!")
    print(f"Total corpus size: {total_bytes:,} bytes (Average per bio: {total_bytes / len(dirs):,.0f} bytes)")

