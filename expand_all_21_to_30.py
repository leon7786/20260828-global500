# -*- coding: utf-8 -*-
import os

base_dir = '/root/1CT-Share/20260828-global500/Founder'

for rank in range(21, 31):
    dirs = [d for d in os.listdir(base_dir) if d.startswith(f"{rank:03d}-")]
    if dirs:
        d = dirs[0]
        fpath = os.path.join(base_dir, d, "founder.md")
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
        size = len(c.encode("utf-8"))
        print(f"[{rank:03d}] {d}: {size} bytes")

print("Expansion check completed!")
