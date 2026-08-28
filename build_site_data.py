# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = '/root/1CT-Share/20260828-global500'
founder_dir = os.path.join(base_dir, 'Founder')

# Industry and country classification mapping for top 100
country_map = {
    'Amazon': '🇺🇸 美国', 'Walmart': '🇺🇸 美国', 'StateGrid': '🇨🇳 中国', 'UnitedHealth': '🇺🇸 美国',
    'SaudiAramco': '🇸🇦 沙特', 'Apple': '🇺🇸 美国', 'McKesson': '🇺🇸 美国', 'Alphabet': '🇺🇸 美国',
    'CVSHealth': '🇺🇸 美国', 'CNPC': '🇨🇳 中国', 'BerkshireHathaway': '🇺🇸 美国', 'Sinopec': '🇨🇳 中国',
    'Volkswagen': '🇩🇪 德国', 'Toyota': '🇯🇵 日本', 'ExxonMobil': '🇺🇸 美国', 'Cencora': '🇺🇸 美国',
    'CSCEC': '🇨🇳 中国', 'Microsoft': '🇺🇸 美国', 'JPMorganChase': '🇺🇸 美国', 'Costco': '🇺🇸 美国',
    'Cigna': '🇺🇸 美国', 'Shell': '🇬🇧 英国', 'Foxconn': '🇨🇳 中国', 'Glencore': '🇨🇭 瑞士',
    'Trafigura': '🇸🇬 新加坡', 'Samsung': '🇰🇷 韩国', 'CardinalHealth': '🇺🇸 美国', 'NVIDIA': '🇺🇸 美国',
    'ICBC': '🇨🇳 中国', 'Meta': '🇺🇸 美国', 'ElevanceHealth': '🇺🇸 美国', 'Centene': '🇺🇸 美国',
    'BP': '🇬🇧 英国', 'BankOfAmerica': '🇺🇸 美国', 'ABC': '🇨🇳 中国', 'Chevron': '🇺🇸 美国',
    'CCB': '🇨🇳 中国', 'Ford': '🇺🇸 美国', 'GM': '🇺🇸 美国', 'TotalEnergies': '🇫🇷 法国',
    'JD': '🇨🇳 中国', 'ChinaLife': '🇨🇳 中国', 'Stellantis': '🇳🇱 荷兰', 'BOC': '🇨🇳 中国',
    'Citigroup': '🇺🇸 美国', 'HomeDepot': '🇺🇸 美国', 'FannieMae': '🇺🇸 美国', 'PingAn': '🇨🇳 中国',
    'CREC': '🇨🇳 中国', 'BMW': '🇩🇪 德国'
}

def get_country(folder_name):
    for key, val in country_map.items():
        if key.lower() in folder_name.lower():
            return val
    if '中国' in folder_name or '中铁' in folder_name or '建行' in folder_name or '中海油' in folder_name or '宝武' in folder_name or '中电建' in folder_name:
        return '🇨🇳 中国'
    return '🌍 跨国/其他'

def get_industry(folder_name):
    fn = folder_name.lower()
    if any(k in fn for k in ['apple', 'alphabet', 'microsoft', 'nvidia', 'meta', 'tencent', 'dell']):
        return '💻 科技与芯片'
    if any(k in fn for k in ['amazon', 'walmart', 'costco', 'jd', 'target', 'homedepot', 'ahold']):
        return '🛒 零售与电商'
    if any(k in fn for k in ['aramco', 'cnpc', 'sinopec', 'exxon', 'shell', 'bp', 'chevron', 'total', 'gazprom', 'cnooc']):
        return '🛢️ 石油与能源'
    if any(k in fn for k in ['unitedhealth', 'mckesson', 'cvs', 'cencora', 'cigna', 'cardinal', 'elevance', 'centene']):
        return '🏥 医疗与健康'
    if any(k in fn for k in ['volkswagen', 'toyota', 'ford', 'gm', 'stellantis', 'bmw', 'mercedes', 'byd', 'hyundai']):
        return '🚗 汽车与出行'
    if any(k in fn for k in ['jpmorgan', 'icbc', 'bankofamerica', 'abc', 'ccb', 'boc', 'citigroup', 'fanniemae', 'pingan', 'morganstanley']):
        return '🏦 金融与银行'
    if any(k in fn for k in ['stategrid', 'csg']):
        return '⚡ 电网与公用事业'
    if any(k in fn for k in ['cscec', 'crec', 'crcc', 'powerchina']):
        return '🏗️ 建筑与工程'
    if any(k in fn for k in ['foxconn']):
        return '⚙️ 精密代工与制造'
    if any(k in fn for k in ['glencore', 'trafigura', 'reliance', 'chinaminmetals', 'chinabaowu', 'shandongenergy']):
        return '⛏️ 大宗商品与金属'
    return '🏢 综合产业'

dirs = sorted([d for d in os.listdir(founder_dir) if os.path.isdir(os.path.join(founder_dir, d)) and d[0].isdigit()])

companies = []
for d in dirs:
    rank = int(d.split('-')[0])
    parts = d.split('-')
    name_cn = parts[1] if len(parts) > 1 else d
    name_en = parts[2] if len(parts) > 2 else ''
    
    founder_file = os.path.join(founder_dir, d, 'founder.md')
    company_file = os.path.join(founder_dir, d, 'company.md')
    readme_file = os.path.join(founder_dir, d, 'README.md')
    
    founder_size = os.path.getsize(founder_file) if os.path.exists(founder_file) else 0
    company_size = os.path.getsize(company_file) if os.path.exists(company_file) else 0
    
    # Extract founder title from founder.md
    founder_title = "创始人全景传记"
    founder_quote = ""
    if os.path.exists(founder_file):
        with open(founder_file, 'r', encoding='utf-8') as f:
            lines = [f.readline() for _ in range(10)]
            for line in lines:
                if line.startswith('# '):
                    founder_title = line.replace('# ', '').strip()
                elif line.startswith('> **“') or line.startswith('> “'):
                    founder_quote = line.replace('> ', '').replace('**', '').strip()
    
    status = "🌟 大师级深度精修" if founder_size >= 20000 else ("✨ 详实传记" if founder_size >= 10000 else "📝 标准传记")
    
    companies.append({
        'rank': rank,
        'folder': d,
        'name_cn': name_cn,
        'name_en': name_en,
        'country': get_country(d),
        'industry': get_industry(d),
        'founder_title': founder_title,
        'founder_quote': founder_quote[:150] + ('...' if len(founder_quote) > 150 else ''),
        'founder_size': founder_size,
        'founder_size_kb': round(founder_size / 1024, 1),
        'company_size_kb': round(company_size / 1024, 1),
        'status': status
    })

output_data = {
    'total_companies': len(companies),
    'master_count': len([c for c in companies if c['founder_size'] >= 20000]),
    'total_bytes': sum([c['founder_size'] for c in companies]),
    'companies': companies
}

with open(os.path.join(base_dir, 'site_data.json'), 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Generated site_data.json with {len(companies)} companies! Total Master size: {output_data['total_bytes']:,} bytes")
