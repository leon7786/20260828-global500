# -*- coding: utf-8 -*-
import os, urllib.request

logo_dir = '/root/1CT-Share/20260828-global500/assets/logos'

manual_urls = {
    49: [ # 中国中铁 CREC
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/China_Railway_Group_Limited_logo.svg/200px-China_Railway_Group_Limited_logo.svg.png",
        "https://www.crecg.com/images/logo.png"
    ],
    53: [ # 中国移动 China Mobile
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/China_Mobile_logo.svg/200px-China_Mobile_logo.svg.png",
        "https://www.chinamobileltd.com/images/logo.png"
    ],
    76: [ # 三菱商事 Mitsubishi Corp
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Mitsubishi_logo.svg/200px-Mitsubishi_logo.svg.png",
        "https://logo.clearbit.com/mitsubishicorp.com"
    ],
    83: [ # 中海油 CNOOC
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/CNOOC_logo.svg/200px-CNOOC_logo.svg.png",
        "http://www.cnooc.com.cn/images/logo.png"
    ],
    86: [ # 南方电网 CSG
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/China_Southern_Power_Grid_logo.svg/200px-China_Southern_Power_Grid_logo.svg.png",
        "http://www.csg.cn/images/logo.png"
    ],
    87: [ # 山东能源 Shandong Energy
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Shandong_Energy_logo.svg/200px-Shandong_Energy_logo.svg.png",
        "http://www.shandong-energy.com/images/logo.png"
    ],
    89: [ # 俄罗斯天然气 Gazprom
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Gazprom-Logo.svg/200px-Gazprom-Logo.svg.png",
        "https://logo.clearbit.com/gazprom.com"
    ],
    100: [ # 中国宝武 China Baowu
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/China_Baowu_Steel_Group_logo.svg/200px-China_Baowu_Steel_Group_logo.svg.png",
        "http://www.baowugroup.com/images/logo.png"
    ]
}

for rank, urls in manual_urls.items():
    out_file = os.path.join(logo_dir, f"{rank:03d}.png")
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
            })
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = resp.read()
                if len(data) > 100:
                    with open(out_file, 'wb') as f:
                        f.write(data)
                    print(f"[{rank:03d}] Successfully downloaded from {url} ({len(data)}B)")
                    break
        except Exception as e:
            print(f"[{rank:03d}] Failed {url}: {e}")

files = [f for f in os.listdir(logo_dir) if f.endswith('.png')]
print(f"\nFinal count in {logo_dir}: {len(files)}/100 logos!")
