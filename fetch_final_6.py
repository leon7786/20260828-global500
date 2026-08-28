# -*- coding: utf-8 -*-
import os, urllib.request

logo_dir = '/root/1CT-Share/20260828-global500/assets/logos'

final_urls = {
    49: "https://commons.wikimedia.org/wiki/Special:FilePath/China_Railway_Group_Limited_logo.svg",
    53: "https://commons.wikimedia.org/wiki/Special:FilePath/China_Mobile_logo.svg",
    76: "https://commons.wikimedia.org/wiki/Special:FilePath/Mitsubishi_logo.svg",
    83: "https://commons.wikimedia.org/wiki/Special:FilePath/CNOOC_logo.svg",
    87: "https://commons.wikimedia.org/wiki/Special:FilePath/Shandong_Energy_logo.svg",
    89: "https://commons.wikimedia.org/wiki/Special:FilePath/Gazprom-Logo.svg"
}

headers = {
    'User-Agent': 'Global500Bot/2.0 (Mozilla/5.0 Educational Research)',
}

for rank, url in final_urls.items():
    out_file = os.path.join(logo_dir, f"{rank:03d}.png")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = resp.read()
            if len(data) > 100:
                with open(out_file, 'wb') as f:
                    f.write(data)
                print(f"[{rank:03d}] Downloaded successfully ({len(data)}B)")
    except Exception as e:
        print(f"[{rank:03d}] Error: {e}")

files = [f for f in os.listdir(logo_dir) if f.endswith('.png')]
print(f"Current total in {logo_dir}: {len(files)}/100")
