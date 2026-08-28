# -*- coding: utf-8 -*-
import os, urllib.request
from concurrent.futures import ThreadPoolExecutor

base_dir = '/root/1CT-Share/20260828-global500'
logo_dir = os.path.join(base_dir, 'assets', 'logos')
os.makedirs(logo_dir, exist_ok=True)

from curate_real_logos import real_logos
from build_site_data import brand_meta

def download_one(rank):
    out_file = os.path.join(logo_dir, f"{rank:03d}.png")
    if os.path.exists(out_file) and os.path.getsize(out_file) > 500:
        return rank, True, "cached"
        
    meta = brand_meta.get(rank, {})
    domain = meta.get('domain', '')
    
    urls_to_try = []
    if rank in real_logos:
        urls_to_try.append(real_logos[rank])
    if domain:
        urls_to_try.append(f"https://logo.clearbit.com/{domain}")
        urls_to_try.append(f"https://www.google.com/s2/favicons?domain={domain}&sz=128")
        urls_to_try.append(f"https://icon.horse/icon/{domain}")
        urls_to_try.append(f"https://icons.duckduckgo.com/ip3/{domain}.ico")
        
    for url in urls_to_try:
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
            })
            with urllib.request.urlopen(req, timeout=3.5) as resp:
                data = resp.read()
                if len(data) > 150:
                    with open(out_file, 'wb') as f:
                        f.write(data)
                    return rank, True, f"ok ({len(data)}B)"
        except Exception:
            continue
            
    return rank, False, "failed"

with ThreadPoolExecutor(max_workers=25) as executor:
    results = list(executor.map(download_one, range(1, 101)))

ok_count = sum(1 for r in results if r[1])
print(f"Parallel download complete! Successfully downloaded {ok_count}/100 logos.")
for r in results:
    if not r[1]:
        print(f"Failed logo for Rank {r[0]:03d}")
