# -*- coding: utf-8 -*-
import os, urllib.request
from concurrent.futures import ThreadPoolExecutor

base_dir = '/root/1CT-Share/20260828-global500'
founder_dir = os.path.join(base_dir, 'Founder')
logo_dir = os.path.join(base_dir, 'assets', 'logos')
os.makedirs(logo_dir, exist_ok=True)

companies_101_150 = {
    101: {'folder': '101-REWE集团-REWE', 'domain': 'rewe-group.com', 'color': '#CC071E', 'bg': 'bg-red-700'},
    102: {'folder': '102-博世集团-Bosch', 'domain': 'bosch.com', 'color': '#EA1C24', 'bg': 'bg-red-600'},
    103: {'folder': '103-法国兴业银行-SocieteGenerale', 'domain': 'societegenerale.com', 'color': '#E2001A', 'bg': 'bg-rose-700'},
    104: {'folder': '104-中国电建-PowerChina', 'domain': 'powerchina.cn', 'color': '#005BAC', 'bg': 'bg-blue-700'},
    105: {'folder': '105-乐购-Tesco', 'domain': 'tesco.com', 'color': '#EE1C2E', 'bg': 'bg-red-600'},
    106: {'folder': '106-家乐福-Carrefour', 'domain': 'carrefour.com', 'color': '#004F9F', 'bg': 'bg-blue-800'},
    107: {'folder': '107-伊藤忠商事-Itochu', 'domain': 'itochu.co.jp', 'color': '#003A80', 'bg': 'bg-blue-900'},
    108: {'folder': '108-国家能源集团-CHNEnergy', 'domain': 'ceic.com', 'color': '#C8102E', 'bg': 'bg-red-700'},
    109: {'folder': '109-俄罗斯石油-Rosneft', 'domain': 'rosneft.com', 'color': '#F39200', 'bg': 'bg-amber-600'},
    110: {'folder': '110-加拿大皇家银行-RBC', 'domain': 'rbc.com', 'color': '#0051A5', 'bg': 'bg-blue-700'},
    111: {'folder': '111-日本生命保险-NipponLife', 'domain': 'nissay.co.jp', 'color': '#D0021B', 'bg': 'bg-red-600'},
    112: {'folder': '112-建发集团-CDGroup', 'domain': 'cndgroup.com', 'color': '#E31B23', 'bg': 'bg-red-600'},
    113: {'folder': '113-三菱日联金融-MUFG', 'domain': 'mufg.jp', 'color': '#D0021B', 'bg': 'bg-red-600'},
    114: {'folder': '114-日本电信电话-NTT', 'domain': 'group.ntt', 'color': '#0055A5', 'bg': 'bg-blue-700'},
    115: {'folder': '115-荣盛控股-Rongsheng', 'domain': 'rongsheng.net', 'color': '#0066B3', 'bg': 'bg-blue-600'},
    116: {'folder': '116-特斯拉-Tesla', 'domain': 'tesla.com', 'color': '#E82127', 'bg': 'bg-red-600'},
    117: {'folder': '117-华特迪士尼-Disney', 'domain': 'thewaltdisneycompany.com', 'color': '#113CCF', 'bg': 'bg-blue-700'},
    118: {'folder': '118-埃尼石油-Eni', 'domain': 'eni.com', 'color': '#FED100', 'bg': 'bg-yellow-500'},
    119: {'folder': '119-中国邮政-ChinaPost', 'domain': 'chinapost.com.cn', 'color': '#007A3D', 'bg': 'bg-emerald-700'},
    120: {'folder': '120-强生-JohnsonJohnson', 'domain': 'jnj.com', 'color': '#D51900', 'bg': 'bg-red-600'},
    121: {'folder': '121-百事公司-PepsiCo', 'domain': 'pepsico.com', 'color': '#004B93', 'bg': 'bg-blue-800'},
    122: {'folder': '122-敦豪集团-DHL', 'domain': 'group.dhl.com', 'color': '#D40511', 'bg': 'bg-red-600'},
    123: {'folder': '123-中国人保-PICC', 'domain': 'picc.com.cn', 'color': '#E60012', 'bg': 'bg-red-600'},
    124: {'folder': '124-三井物产-Mitsui', 'domain': 'mitsui.com', 'color': '#005BAC', 'bg': 'bg-blue-700'},
    125: {'folder': '125-上汽集团-SAIC', 'domain': 'saicmotor.com', 'color': '#00338D', 'bg': 'bg-blue-900'},
    126: {'folder': '126-迪奥-ChristianDior', 'domain': 'dior.com', 'color': '#000000', 'bg': 'bg-stone-900'},
    127: {'folder': '127-意大利国家电力-Enel', 'domain': 'enel.com', 'color': '#0099FF', 'bg': 'bg-sky-500'},
    128: {'folder': '128-波音-Boeing', 'domain': 'boeing.com', 'color': '#0033A0', 'bg': 'bg-blue-800'},
    129: {'扩张': '129-国药集团-Sinopharm', 'domain': 'sinopharm.com', 'color': '#0071CE', 'bg': 'bg-sky-600'},
    129: {'folder': '129-国药集团-Sinopharm', 'domain': 'sinopharm.com', 'color': '#0071CE', 'bg': 'bg-sky-600'},
    130: {'folder': '130-印度石油-IndianOil', 'domain': 'iocl.com', 'color': '#F47920', 'bg': 'bg-orange-600'},
    131: {'folder': '131-巴西国家石油-Petrobras', 'domain': 'petrobras.com.br', 'color': '#008542', 'bg': 'bg-green-700'},
    132: {'folder': '132-意昂集团-EON', 'domain': 'eon.com', 'color': '#ED1C24', 'bg': 'bg-red-600'},
    133: {'folder': '133-联合包裹-UPS', 'domain': 'ups.com', 'color': '#351C15', 'bg': 'bg-amber-950'},
    134: {'folder': '134-中国电信-ChinaTelecom', 'domain': 'chinatelecom.com.cn', 'color': '#005BAA', 'bg': 'bg-blue-700'},
    135: {'folder': '135-雷神技术-RTX', 'domain': 'rtx.com', 'color': '#D0202F', 'bg': 'bg-red-700'},
    136: {'folder': '136-拉杰什出口-RajeshExports', 'domain': 'rajeshexports.com', 'color': '#9E7E38', 'bg': 'bg-yellow-700'},
    137: {'folder': '137-联邦快递-FedEx', 'domain': 'fedex.com', 'color': '#4D148C', 'bg': 'bg-purple-900'},
    138: {'folder': '138-吉利控股-Geely', 'domain': 'geely.com', 'color': '#003366', 'bg': 'bg-blue-900'},
    139: {'folder': '139-前进保险-Progressive', 'domain': 'progressive.com', 'color': '#007AB8', 'bg': 'bg-sky-700'},
    140: {'folder': '140-道明银行-TDBank', 'domain': 'td.com', 'color': '#008A00', 'bg': 'bg-green-700'},
    141: {'folder': '141-索尼-Sony', 'domain': 'sony.com', 'color': '#000000', 'bg': 'bg-stone-900'},
    142: {'folder': '142-SK集团-SKGroup', 'domain': 'sk.com', 'color': '#E51937', 'bg': 'bg-red-600'},
    143: {'folder': '143-西门子-Siemens', 'domain': 'siemens.com', 'color': '#00646E', 'bg': 'bg-teal-800'},
    144: {'folder': '144-西班牙对外银行-BBVA', 'domain': 'bbva.com', 'color': '#004481', 'bg': 'bg-blue-800'},
    145: {'folder': '145-劳氏公司-Lowes', 'domain': 'lowes.com', 'color': '#004990', 'bg': 'bg-blue-800'},
    146: {'folder': '146-JBS公司-JBS', 'domain': 'jbs.com.br', 'color': '#C8102E', 'bg': 'bg-red-700'},
    147: {'folder': '147-能源转移-EnergyTransfer', 'domain': 'energytransfer.com', 'color': '#003A70', 'bg': 'bg-blue-900'},
    148: {'folder': '148-劳埃德银行-Lloyds', 'domain': 'lloydsbankinggroup.com', 'color': '#006A4E', 'bg': 'bg-emerald-800'},
    149: {'folder': '149-万喜集团-VINCI', 'domain': 'vinci.com', 'color': '#112233', 'bg': 'bg-slate-800'},
    150: {'folder': '150-法国农业信贷银行-CreditAgricole', 'domain': 'credit-agricole.com', 'color': '#007A5E', 'bg': 'bg-emerald-700'},
}

# 1. Create all folders
for rank, meta in companies_101_150.items():
    fdir = os.path.join(founder_dir, meta['folder'])
    os.makedirs(fdir, exist_ok=True)
    print(f"Directory verified: {meta['folder']}")

# 2. Download all logos in parallel
def download_one(rank):
    meta = companies_101_150[rank]
    domain = meta['domain']
    out_file = os.path.join(logo_dir, f"{rank:03d}.png")
    if os.path.exists(out_file) and os.path.getsize(out_file) > 500:
        return rank, True, "cached"
        
    urls_to_try = [
        f"https://logo.clearbit.com/{domain}",
        f"https://www.google.com/s2/favicons?domain={domain}&sz=128",
        f"https://icon.horse/icon/{domain}",
        f"https://icons.duckduckgo.com/ip3/{domain}.ico"
    ]
    
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
    results = list(executor.map(download_one, range(101, 151)))

ok_count = sum(1 for r in results if r[1])
print(f"Parallel download complete! Successfully downloaded {ok_count}/50 logos for Ranks 101-150.")

