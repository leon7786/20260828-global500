# -*- coding: utf-8 -*-
import os, urllib.request, time

base_dir = '/root/1CT-Share/20260828-global500'
logo_dir = os.path.join(base_dir, 'assets', 'logos')
os.makedirs(logo_dir, exist_ok=True)

# Curated real logo sources (Tier 1: Clearbit / Wikimedia high-res / Official, Tier 2: Google 128px favicon, Tier 3: IconHorse)
from curate_real_logos import real_logos
from build_site_data import brand_meta

success = 0
failed = []

for rank in range(1, 101):
    out_file = os.path.join(logo_dir, f"{rank:03d}.png")
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
    
    downloaded = False
    for url in urls_to_try:
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
            })
            with urllib.request.urlopen(req, timeout=4) as resp:
                data = resp.read()
                if len(data) > 150: # Valid image
                    with open(out_file, 'wb') as f:
                        f.write(data)
                    downloaded = True
                    # print(f"[{rank:03d}] Downloaded from {url} ({len(data)} bytes)")
                    break
        except Exception as e:
            continue
            
    if downloaded:
        success += 1
    else:
        failed.append(rank)
        print(f"[{rank:03d}] Failed to download logo for domain: {domain}")

print(f"\nDownloaded {success}/100 logos into {logo_dir}! Failed: {len(failed)}")
