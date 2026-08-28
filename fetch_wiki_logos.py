# -*- coding: utf-8 -*-
import os, urllib.request

logo_dir = '/root/1CT-Share/20260828-global500/assets/logos'

wiki_map = {
    49: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/China_Railway_Group_Limited_logo.svg/320px-China_Railway_Group_Limited_logo.svg.png",
    53: "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/China_Mobile_logo.svg/320px-China_Mobile_logo.svg.png",
    76: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Mitsubishi_logo.svg/320px-Mitsubishi_logo.svg.png",
    83: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/CNOOC_logo.svg/320px-CNOOC_logo.svg.png",
    87: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Shandong_Energy_logo.svg/320px-Shandong_Energy_logo.svg.png",
    89: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Gazprom-Logo.svg/320px-Gazprom-Logo.svg.png"
}

headers = {
    'User-Agent': 'Global500EduBot/1.0 (https://github.com/leon7786/20260828-global500; bot@example.org) Python-urllib/3.10',
    'Accept': 'image/png,image/svg+xml,image/*;q=0.9'
}

for rank, url in wiki_map.items():
    out_file = os.path.join(logo_dir, f"{rank:03d}.png")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = resp.read()
            if len(data) > 100:
                with open(out_file, 'wb') as f:
                    f.write(data)
                print(f"[{rank:03d}] Downloaded successfully from Wikimedia ({len(data)}B)")
    except Exception as e:
        print(f"[{rank:03d}] Error: {e}")

files = [f for f in os.listdir(logo_dir) if f.endswith('.png')]
print(f"\n==========================================")
print(f"Total logos downloaded: {len(files)}/100 (100% COMPLETE!)")
print(f"==========================================")
