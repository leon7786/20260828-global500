# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = '/root/1CT-Share/20260828-global500'
founder_dir = os.path.join(base_dir, 'Founder')

# Domain mapping for top 100 enterprises for official high-res logo fetching
domain_map = {
    'Amazon': 'amazon.com', 'Walmart': 'walmart.com', 'StateGrid': 'sgcc.com.cn', 'UnitedHealth': 'unitedhealthgroup.com',
    'SaudiAramco': 'aramco.com', 'Apple': 'apple.com', 'McKesson': 'mckesson.com', 'Alphabet': 'google.com',
    'CVSHealth': 'cvshealth.com', 'CNPC': 'cnpc.com.cn', 'BerkshireHathaway': 'berkshirehathaway.com', 'Sinopec': 'sinopec.com',
    'Volkswagen': 'volkswagen.com', 'Toyota': 'toyota-global.com', 'ExxonMobil': 'exxonmobil.com', 'Cencora': 'cencora.com',
    'CSCEC': 'cscec.com', 'Microsoft': 'microsoft.com', 'JPMorganChase': 'jpmorganchase.com', 'Costco': 'costco.com',
    'Cigna': 'cigna.com', 'Shell': 'shell.com', 'Foxconn': 'foxconn.com', 'Glencore': 'glencore.com',
    'Trafigura': 'trafigura.com', 'Samsung': 'samsung.com', 'CardinalHealth': 'cardinalhealth.com', 'NVIDIA': 'nvidia.com',
    'ICBC': 'icbc.com.cn', 'Meta': 'meta.com', 'ElevanceHealth': 'elevancehealth.com', 'Centene': 'centene.com',
    'BP': 'bp.com', 'BankOfAmerica': 'bankofamerica.com', 'ABC': 'abchina.com', 'Chevron': 'chevron.com',
    'CCB': 'ccb.com', 'Ford': 'ford.com', 'GM': 'gm.com', 'TotalEnergies': 'totalenergies.com',
    'JD': 'jd.com', 'ChinaLife': 'chinalife.com.cn', 'Stellantis': 'stellantis.com', 'BOC': 'boc.cn',
    'Citigroup': 'citigroup.com', 'HomeDepot': 'homedepot.com', 'FannieMae': 'fanniemae.com', 'PingAn': 'pingan.cn',
    'CREC': 'crecg.com', 'BMW': 'bmw.com', 'MercedesBenz': 'mercedes-benz.com', 'Kroger': 'kroger.com',
    'ChinaMobile': 'chinamobileltd.com', 'Santander': 'santander.com', 'Honda': 'honda.com', 'Alibaba': 'alibabagroup.com',
    'CRCC': 'crcc.cn', 'BNPParibas': 'bnpparibas.com', 'CITIC': 'citic.com', 'Verizon': 'verizon.com',
    'Phillips66': 'phillips66.com', 'HSBC': 'hsbc.com', 'MarathonPetroleum': 'marathonpetroleum.com', 'Sberbank': 'sberbank.ru',
    'DeutscheTelekom': 'telekom.com', 'CCCC': 'ccccltd.cn', 'Allianz': 'allianz.com', 'ChinaResources': 'crc.com.hk',
    'StoneX': 'stonex.com', 'StateFarm': 'statefarm.com', 'FreddieMac': 'freddiemac.com', 'Hyundai': 'hyundai.com',
    'Humana': 'humana.com', 'EDF': 'edf.fr', 'ATT': 'att.com', 'MitsubishiCorp': 'mitsubishicorp.com',
    'GoldmanSachs': 'goldmansachs.com', 'Hengli': 'hengli.com', 'Comcast': 'comcast.com', 'WellsFargo': 'wellsfargo.com',
    'Huawei': 'huawei.com', 'TSMC': 'tsmc.com', 'CNOOC': 'cnooc.com.cn', 'MorganStanley': 'morganstanley.com',
    'Reliance': 'ril.com', 'CSG': 'csg.cn', 'ShandongEnergy': 'shandong-energy.com', 'Valero': 'valero.com',
    'Gazprom': 'gazprom.com', 'Dell': 'dell.com', 'BYD': 'bydglobal.com', 'LIC': 'licindia.in',
    'Nestle': 'nestle.com', 'AXA': 'axa.com', 'Equinor': 'equinor.com', 'Target': 'target.com',
    'Tencent': 'tencent.com', 'AholdDelhaize': 'aholddelhaize.com', 'ChinaMinmetals': 'minmetals.com', 'ChinaBaowu': 'baowugroup.com'
}

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
        return '💻 科技芯片'
    if any(k in fn for k in ['amazon', 'walmart', 'costco', 'jd', 'target', 'homedepot', 'ahold']):
        return '🛒 零售电商'
    if any(k in fn for k in ['aramco', 'cnpc', 'sinopec', 'exxon', 'shell', 'bp', 'chevron', 'total', 'gazprom', 'cnooc', 'phillips', 'marathon', 'valero']):
        return '🛢️ 石油能源'
    if any(k in fn for k in ['unitedhealth', 'mckesson', 'cvs', 'cencora', 'cigna', 'cardinal', 'elevance', 'centene', 'humana']):
        return '🏥 医疗健康'
    if any(k in fn for k in ['volkswagen', 'toyota', 'ford', 'gm', 'stellantis', 'bmw', 'mercedes', 'byd', 'hyundai', 'honda']):
        return '🚗 汽车出行'
    if any(k in fn for k in ['jpmorgan', 'icbc', 'bankofamerica', 'abc', 'ccb', 'boc', 'citigroup', 'fanniemae', 'pingan', 'morganstanley', 'goldman', 'wellsfargo', 'santander', 'hsbc', 'sberbank', 'bnp', 'citic', 'stonex', 'statefarm', 'freddie', 'lic', 'axa']):
        return '🏦 金融银行'
    if any(k in fn for k in ['stategrid', 'csg', 'edf']):
        return '⚡ 电网公用'
    if any(k in fn for k in ['cscec', 'crec', 'crcc', 'powerchina', 'cccc']):
        return '🏗️ 建筑工程'
    if any(k in fn for k in ['foxconn', 'tsmc']):
        return '⚙️ 制造芯片'
    if any(k in fn for k in ['glencore', 'trafigura', 'reliance', 'chinaminmetals', 'chinabaowu', 'shandongenergy', 'hengli']):
        return '⛏️ 资源大宗'
    if any(k in fn for k in ['chinamobile', 'verizon', 'deutschetelekom', 'att', 'comcast']):
        return '📡 电信传媒'
    if any(k in fn for k in ['nestle', 'kroger']):
        return '🍞 食品消费'
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
    
    founder_size = os.path.getsize(founder_file) if os.path.exists(founder_file) else 0
    company_size = os.path.getsize(company_file) if os.path.exists(company_file) else 0
    
    founder_title = "创始人全景传记"
    founder_name = ""
    founder_quote = ""
    if os.path.exists(founder_file):
        with open(founder_file, 'r', encoding='utf-8') as f:
            lines = [f.readline() for _ in range(15)]
            for line in lines:
                if line.startswith('# '):
                    founder_title = line.replace('# ', '').strip()
                    m = re.match(r'#\s*([^：:\n]+)', line)
                    if m:
                        founder_name = m.group(1).strip()
                        founder_name = re.sub(r'的全景史诗传记.*', '', founder_name).strip()
                elif line.startswith('> **“') or line.startswith('> “'):
                    founder_quote = line.replace('> ', '').replace('**', '').strip()

    # Fallback founder name if empty
    if not founder_name:
        founder_name = f"{name_cn}创始团队"

    # Clean short founder name for display (max 18 chars)
    short_founder_name = founder_name
    if ' 与 ' in short_founder_name:
        short_founder_name = short_founder_name.split(' 与 ')[0] + '等'
    elif ' & ' in short_founder_name:
        short_founder_name = short_founder_name.split(' & ')[0] + '等'
    if len(short_founder_name) > 20:
        short_founder_name = short_founder_name[:18] + '...'

    domain = domain_map.get(name_en, f"{name_en.lower()}.com")
    logo_url = f"https://www.google.com/s2/favicons?domain={domain}&sz=64"
    
    status = "🌟 大师级深度精修" if founder_size >= 20000 else ("✨ 详实传记" if founder_size >= 10000 else "📝 标准传记")
    
    companies.append({
        'rank': rank,
        'folder': d,
        'name_cn': name_cn,
        'name_en': name_en,
        'domain': domain,
        'logo_url': logo_url,
        'country': get_country(d),
        'industry': get_industry(d),
        'founder_name': founder_name,
        'short_founder_name': short_founder_name,
        'founder_title': founder_title,
        'founder_quote': founder_quote[:150] + ('...' if len(founder_quote) > 150 else ''),
        'founder_size': founder_size,
        'founder_size_kb': round(founder_size / 1024, 1),
        'company_size_kb': round(company_size / 1024, 1),
        'status': status
    })

site_data = {
    'total_companies': len(companies),
    'master_count': len([c for c in companies if c['founder_size'] >= 20000]),
    'generated_at': '2026-08-29',
    'companies': companies
}

out_path = os.path.join(base_dir, 'site_data.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(site_data, f, ensure_ascii=False, indent=2)

print(f"Generated site_data.json with {len(companies)} companies! Included logo_url and founder_name.")
