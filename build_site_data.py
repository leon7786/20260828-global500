# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = '/root/1CT-Share/20260828-global500'
founder_dir = os.path.join(base_dir, 'Founder')

curated_founders = {
    1: "杰夫·贝索斯 (Jeff Bezos)",
    2: "山姆·沃尔顿 (Sam Walton)",
    3: "刘振亚 (Liu Zhenya)",
    4: "理查德·伯克 (Richard Burke)",
    5: "马克斯·斯坦尼克 (Max Steineke)",
    6: "史蒂夫·乔布斯 (Steve Jobs)",
    7: "约翰·麦克森 (John McKesson)",
    8: "拉里·佩奇 (Larry Page) & 谢尔盖·布林 (Sergey Brin)",
    9: "斯坦利·戈德斯坦 (Stanley Goldstein)",
    10: "李四光 (Li Siguang) & 王进喜 (Wang Jinxi)",
    11: "沃伦·巴菲特 (Warren Buffett) & 查理·芒格 (Charlie Munger)",
    12: "陈锦华 (Chen Jinhua)",
    13: "费迪南德·保时捷 (Ferdinand Porsche)",
    14: "丰田喜一郎 (Kiichiro Toyoda)",
    15: "约翰·D·洛克菲勒 (John D. Rockefeller)",
    16: "吕西安·布伦斯威格 (Lucien Brunswig)",
    17: "陆佑九 (Lu Youjiu)",
    18: "比尔·盖茨 (Bill Gates) & 保罗·艾伦 (Paul Allen)",
    19: "J.P. 摩根 (J. Pierpont Morgan)",
    20: "吉姆·辛内格尔 (James Sinegal)",
    21: "信诺创始先驱团队 (Cigna Pioneers)",
    22: "马库斯·萨缪尔 (Marcus Samuel)",
    23: "郭台铭 (Terry Gou)",
    24: "马克·里奇 (Marc Rich)",
    25: "克劳德·多芬 (Claude Dauphin)",
    26: "李秉喆 (Lee Byung-chul) & 李健熙 (Lee Kun-hee)",
    27: "罗伯特·D·沃尔特 (Robert D. Walter)",
    28: "黄仁勋 (Jensen Huang)",
    29: "姜建清与工行奠基团队 (ICBC Leadership)",
    30: "马克·扎克伯格 (Mark Zuckerberg)",
    31: "Elevance 创始先驱团队 (Elevance Pioneers)",
    32: "伊丽莎白·布林 (Elizabeth Brinn)",
    33: "威廉·达西 (William D'Arcy)",
    34: "阿马迪奥·贾尼尼 (Amadeo Giannini)",
    35: "中国农行奠基先驱团队 (ABC Pioneers)",
    36: "德米特里厄斯·斯科菲尔德 (D.G. Scofield)",
    37: "中国建行奠基先驱团队 (CCB Pioneers)",
    38: "亨利·福特 (Henry Ford)",
    39: "威廉·杜兰特 (William Durant) & 斯隆 (Alfred Sloan)",
    40: "欧内斯特·梅西埃 (Ernest Mercier)",
    41: "刘强东 (Richard Liu)",
    42: "中国人寿奠基先驱团队 (China Life Pioneers)",
    43: "乔瓦尼·阿涅利 (Giovanni Agnelli) & 标致家族",
    44: "孙中山与张嘉璈 (Bank of China Pioneers)",
    45: "塞缪尔·奥斯古德 (Samuel Osgood) & 桑迪·威尔",
    46: "伯尼·马库斯 (Bernie Marcus) & 阿瑟·布兰克",
    47: "罗斯福与房利美奠基团队 (Fannie Mae Pioneers)",
    48: "马明哲 (Peter Ma)",
    49: "中国中铁开路先锋团队 (CREC Pioneers)",
    50: "卡尔·拉普 (Karl Rapp) & 匡特家族",
    51: "卡尔·本茨 (Carl Benz) & 戈特利布·戴姆勒",
    52: "伯纳德·克罗格 (Bernard Kroger)",
    53: "中国移动奠基先驱团队 (China Mobile Pioneers)",
    54: "埃米尔·博廷 (Emilio Botín) & 桑坦德家族",
    55: "本田宗一郎 (Soichiro Honda) & 藤泽武夫",
    56: "马云 (Jack Ma) & 蔡崇信 (Joe Tsai)",
    57: "铁道兵与中铁建先驱团队 (CRCC Pioneers)",
    58: "米歇尔·佩贝罗 (Michel Pébereau)",
    59: "荣毅仁 (Rong Yiren)",
    60: "伊万·塞登伯格 (Ivan Seidenberg)",
    61: "弗兰克·菲利普斯 (Frank Phillips)",
    62: "托马斯·萨瑟兰德 (Thomas Sutherland)",
    63: "唐奈尔家族 (Donnell Family)",
    64: "格尔曼·格列夫 (Herman Gref)",
    65: "施特凡 (Heinrich von Stephan)",
    66: "中国交建百年奠基团队 (CCCC Pioneers)",
    67: "卡尔·冯·蒂梅 (Carl von Thieme)",
    68: "华润红色先驱谱系 (China Resources Pioneers)",
    69: "索尔·斯通 (Saul Stone)",
    70: "乔治·J·梅切尔 (George J. Mecherle)",
    71: "房地美奠基先驱团队 (Freddie Mac Pioneers)",
    72: "郑周永 (Chung Ju-yung)",
    73: "大卫·A·琼斯 (David A. Jones Sr.)",
    74: "皮埃尔·梅斯梅尔与法电团队 (EDF Pioneers)",
    75: "亚历山大·贝尔 (Alexander Graham Bell)",
    76: "岩崎弥太郎 (Yataro Iwasaki)",
    77: "马库斯·高盛 (Marcus Goldman)",
    78: "陈建华 (Chen Jianhua) & 范红卫 (Fan Hongwei)",
    79: "拉尔夫·J·罗伯茨 (Ralph J. Roberts)",
    80: "亨利·韦尔斯 (Henry Wells) & 威廉·法戈",
    81: "任正非 (Ren Zhengfei)",
    82: "张忠谋 (Morris Chang)",
    83: "秦文彩与中海油奠基先驱 (CNOOC Pioneers)",
    84: "亨利·S·摩根 (Henry S. Morgan) & 哈罗德·斯坦利",
    85: "迪鲁巴伊·安巴尼 (Dhirubhai Ambani)",
    86: "袁懋振与南网奠基先驱 (CSG Pioneers)",
    87: "卜兆德与山东能源开拓者 (Shandong Energy Pioneers)",
    88: "比尔·格里希 (Bill Greehey)",
    89: "维克托·切尔诺梅尔金 (Viktor Chernomyrdin)",
    90: "迈克尔·戴尔 (Michael Dell)",
    91: "王传福 (Wang Chuanfu)",
    92: "印度人寿奠基先驱 (LIC Pioneers)",
    93: "亨利·雀巢 (Henri Nestlé) & 佩奇兄弟",
    94: "克劳德·贝贝阿 (Claude Bébéar)",
    95: "法鲁克·阿尔-卡西姆 (Farouk Al-Kasim)",
    96: "乔治·戴顿 (George Dayton)",
    97: "马化腾 (Pony Ma) 与腾讯创始团队",
    98: "阿尔伯特·海恩 (Albert Heijn) & 德尔海兹兄弟",
    99: "中国五矿奠基先驱团队 (Minmetals Pioneers)",
    100: "宝钢与武钢奠基开拓团队 (Baowu Pioneers)"
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
    
    founder_name = curated_founders.get(rank, f"{name_cn}创始团队")
    
    founder_title = "创始人全景传记"
    founder_quote = ""
    if os.path.exists(founder_file):
        with open(founder_file, 'r', encoding='utf-8') as f:
            lines = [f.readline() for _ in range(15)]
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
        'founder_name': founder_name,
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

print(f"Generated site_data.json with {len(companies)} companies! Included exact Chinese & English company & founder names.")
